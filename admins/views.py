from django.shortcuts import render, redirect
from enc.models import User
from dec.models import DecKey as Dk
from random import randrange
from .Encryption import *
# Create your views here.


def home(request):
    try:
        if(type(request.session['admin']) == str):
            return render(request, 'admins/home.html', {'title': 'Home'})
    except KeyError:
        return redirect('/auth/login')
    else:
        return redirect('/auth/login')


def create(request):
    try:
        context = {
            'title': 'Create Account'
        }

        if(type(request.session['admin']) == str):
            if(request.method == 'POST'):
                flag = False
                while not flag:
                    account_number = randrange(100000000, 999999999)
                    user = User.objects.filter(account_number=account_number)
                    if(len(user) > 0):
                        flag = False
                    else:
                        flag = True

                objects = User.objects.all()
                id = 1
                if(len(objects) == 0):
                    id = 1
                else:
                    id = objects[len(objects) - 1].odec + 1
                dec = Dk.objects.filter(id=(id % 1)+1).first()
                user = User(
                    account_number=account_number,
                    first_name=Encrypt(
                        request.POST["first_name"], dec.order, dec.keys, dec.r_seq),
                    last_name=Encrypt(
                        request.POST["last_name"], dec.order, dec.keys, dec.r_seq),
                    username=Encrypt(
                        request.POST["username"], dec.order, dec.keys, dec.r_seq),
                    email=Encrypt(
                        request.POST["email"], dec.order, dec.keys, dec.r_seq),
                    password=Encrypt(
                        request.POST["password"], dec.order, dec.keys, dec.r_seq),
                    aadhar_number=Encrypt(request.POST["aadhar_number"], dec.order, dec.keys, dec.r_seq), current_balance=Encrypt(request.POST["current_balance"], dec.order, dec.keys, dec.r_seq)
                )

                user.save()
                context["account_number"] = user.account_number
                # return render(request, 'admins/create.html', {"account_number": user.account_number})

            return render(request, 'admins/create.html')
    except Exception as e:
        print("Exception: ", e)
        return redirect('/auth/login')

    return redirect('/auth/login')


def deposit(request):
    try:
        context = {
            'title': 'Deposit'
        }

        if(type(request.session['admin']) == str):
            if(request.method == 'POST'):
                account_number = request.POST["account_number"]
                balance = request.POST["amount"]
                user = User.objects.filter(
                    account_number=account_number).first()

                order = (int(user.odec) % 1) + 1

                key = Dk.objects.filter(id=order).first()
                current_balance = Decrypt(
                    user.current_balance, key.order, key.keys, key.r_seq)
                current_balance = str(int(current_balance) + int(balance))

                user.current_balance = Encrypt(
                    current_balance, key.order, key.keys, key.r_seq)
                user.save()

                context["current_balance"] = current_balance

            return render(request, 'admins/deposit.html', context)
    except Exception:
        return redirect('/auth/login')
    else:
        return redirect('/auth/login')


def withdraw(request):
    try:
        context = {
            'title': 'withdraw'
        }
        if(type(request.session['admin']) == str):
            if(request.method == 'POST'):
                account_number = request.POST["account_number"]
                balance = request.POST["amount"]
                user = User.objects.filter(
                    account_number=account_number).first()

                order = (int(user.odec) % 1) + 1

                key = Dk.objects.filter(id=order).first()
                current_balance = Decrypt(
                    user.current_balance, key.order, key.keys, key.r_seq)
                bal = current_balance
                print("Current Balance: " + current_balance)
                current_balance = str(int(current_balance) - int(balance))

                if(int(current_balance) < 1000):
                    context = {"msg": "Please Enter Valid Amount! Your current Balance is: {}" . format(
                        int(bal))}
                else:
                    user.current_balance = Encrypt(
                        current_balance, key.order, key.keys, key.r_seq)
                    user.save()

                    context["msg"] = "Your Current Balance: {}" . format(
                        current_balance)

            # return render(request, 'admins/withdraw.html')
            return render(request, 'admins/withdraw.html', context)

    except Exception:
        return redirect('/auth/login')
    else:
        return redirect('/auth/login')


def showDetails(request):
    if(request.method == 'POST'):
        try:
            account_number = request.POST["account_number"]
            user = User.objects.filter(account_number=account_number).first()
            key = Dk.objects.filter(id=1).first()
            data = {}
            data["first_name"] = Decrypt(
                user.first_name, key.order, key.keys, key.r_seq)
            data["last_name"] = Decrypt(
                user.last_name, key.order, key.keys, key.r_seq)
            data["username"] = Decrypt(
                user.username, key.order, key.keys, key.r_seq)
            data["email"] = Decrypt(user.email, key.order, key.keys, key.r_seq)
            data["password"] = Decrypt(
                user.password, key.order, key.keys, key.r_seq)
            data["aadhar_number"] = Decrypt(
                user.aadhar_number, key.order, key.keys, key.r_seq)
            data["current_balance"] = Decrypt(
                user.current_balance, key.order, key.keys, key.r_seq)

            return render(request, 'admins/show.html', {'data': data})

        except Exception:
            return render(request, 'admins/show.html', {'data': data, 'error': "Invalid Account Number! Please Enter a Valid Account number..!"})

    return render(request, 'admins/show.html')
