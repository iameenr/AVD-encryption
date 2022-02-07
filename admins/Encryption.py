import random

# Method 1
def EmultiplyRN(st, n):
        return [x*n for x in st]

def DmultiplyRN(st, n):
        return [x/n for x in st]

# Method 2
def EsubRN(st,n):
        return[(x-n) for x in st]

def DsubRN(st, n):
        return[(x+n) for x in st]

# Method 3
def ErangeMult(st, a):
        for i in range(len(st)):
                if st[i]>a:
                        st[i] = st[i]*2
        return st

def DrangeMult(st, a):
        for i in range(len(st)):
                var = st[i]/2
                if var >a:
                        st[i] = var                        
        return st

# Method 4
def ENextNoAdd(st, key):
        st[0]=st[0]+key
        for i in range(len(st)-1):
                st[i]=st[i]+st[i+1]
        return st

def DNextNoAdd(st, key):
        st[0]=st[0]-key
        for i in range(len(st)-1, 0, -1):
                st[i-1]=st[i-1]-st[i]
        return st

# Method 5
def ELeftMostEleSub(st,key):
        number=st[0]+key
        for i in range(1,len(st)):
                st[i]=st[i]-number
        return st

def DLeftMostEleSub(st,key):
        number=st[0]+key
        for i in range(1,len(st)):
             st[i]=st[i]+number
        return st

# Method 6
def EPenultimateEleSub(st,key): 
        number=st[len(st)-2]+key
        for i in range(0,len(st)-2):
                st[i]=st[i]-number
        return st

def DPenultimateEleSub(st,key): 
        number=st[len(st)-2]+key
        for i in range(0,len(st)-2):
                st[i]=st[i]+number
        return st

# Method 7
def ETransverseAddition(st,key):
        for i in range(int(len(st)/2)):
                st[i]=st[i]+st[len(st)-i-1]+key
        return st

def DTransverseAddition(st,key):
        for i in range(int(len(st)/2)):
                st[i]-=st[len(st)-i-1]+key
        return st

# Method 8
def EInverseTransverseSubtraction(st,key):
        for i in range(len(st), int(len(st)/2)+1,-1):
                st[i-1]=st[i-1]-st[len(st)-i]+key
        return st

def DInverseTransverseSubtraction(st,key):
        for i in range(len(st), int(len(st)/2)+1,-1):
                st[i-1]=st[i-1]+st[len(st)-i]-key
        return st

# Method 9
def ERandomPosSubtraction(st,pos,key):
        no=st[pos]
        st[pos]=st[pos]*2
        for i in range(len(st)):
                st[i]=st[i]-no
        return st

def DRandomPosSubtraction(st,pos,key):
        no=st[pos]
        st[pos]=0
        for i in range(len(st)):
                st[i]=st[i]+no
        return st

# Method 10
def EAddNextMod(st,key):
        for i in range(0, len(st)-1):
                st[i] = st[i]+(st[i+1]%10)
        st[len(st)-1] = st[len(st)-1]+key
        return st

def DAddNextMod(st,key):
        st[len(st)-1] = st[len(st)-1]-key
        for i in range(len(st)-2, -1, -1):
                st[i] = st[i]-(st[i+1]%10)
        return st

# Method 11
def EOddEven(st, oddkey, evenkey):
        for i in range(0, len(st)):
                if st[i]%2==1:
                        st[i] = st[i] + oddkey
                else:
                        st[i] = st[i] + evenkey
        return st

def DOddEven(st, oddkey, evenkey):
        for i in range(0, len(st)):
                if st[i]%2==1:
                        st[i] = st[i] - oddkey
                else:
                        st[i] = st[i] - evenkey
        return st

# Method 12
def ERevSub(st, key):
        st.reverse()
        for i in range(len(st)):
                st[i] = st[i] - (key+i)
        return st

def DRevSub(st, key):
        for i in range(len(st)):
                st[i] = st[i] + (key+i)
        st.reverse()
        return st

# Method 13
def EmultiplyRNfinal(st, n):
        return [x*n for x in st]

def DmultiplyRNfinal(st, n):
        return [x/n for x in st]

# Method 14
def EPenultimateEleSubFinal(st,key): 
        number=st[len(st)-2]+key
        for i in range(0,len(st)-2):
                st[i]=st[i]-number
        return st

def DPenultimateEleSubFinal(st,key): 
        number=st[len(st)-2]+key
        for i in range(0,len(st)-2):
                st[i]=st[i]+number
        return st
'''
def EAlternateMultSub(st,key1,key2):
        for i in range(len(st,2)):
                st[i]=st[i]-key1
'''
scrambler = {
        '0':['@','#','$', 'G', 'V', 'D', '9'],
        '1':['5','!','x', 'm'],
        '2':['1','/','C', '+'],
        '3':['y',':','<', 'K'],
        '4':['>',';',']', '_'],
        '5':['S','z','?', '3'],
        '6':['~','N','j', 'L'], 
        '7':['f','q','P', '6'],
        '8':['t','W','h', 'M'],
        '9':['H','w','k', '.'],
        '-':['%', '^', '&', 'r', 'b', 'X'],
        ',':['2','7','0', '(', '=', '`'], 
        '\n':'',
        '':'',
        ' ':' ',
        '.':['B', 'F', 'a']
        }

def EnScramble(st):
        global scrambler
        st=[x for x in st]
        for i in range(len(st)):
                st[i] = scrambler[st[i]][random.randrange(len(scrambler[st[i]]))]
        return_val = ''.join(st)
        return return_val

def DeScramble(st):
        global scrambler
        st=[x for x in st]
        dt=[]
        for i in range(len(st)):
                for key, value in scrambler.items():
                        if st[i] in value:
                                dt.append(key)
        return_val = ''.join(dt)
        print("Return: ", return_val)
        return return_val

ls = []

# ENCRYPTION FUNCTION
def EncryptionFinal(order, keys, repeatSequence):
        global ls
        for i in range(12):
                if order[i] == 1:
                        for x in range(repeatSequence[i]):
                                ls = EmultiplyRN(ls, keys[i])
                elif order[i] == 2:
                        for x in range(repeatSequence[i]):
                                ls = ErangeMult(ls, keys[i])
                elif order[i] == 3:
                        for x in range(repeatSequence[i]):
                                ls = EsubRN(ls, keys[i])
                elif order[i] == 4:
                        for x in range(repeatSequence[i]):
                                ls = ENextNoAdd(ls, keys[i])
                elif order[i] == 5:
                        for x in range(repeatSequence[i]):
                                ls = ELeftMostEleSub(ls, keys[i])
                elif order[i] == 6:
                        for x in range(repeatSequence[i]):
                                ls = EPenultimateEleSub(ls, keys[i])
                elif order[i] == 7:
                        for x in range(repeatSequence[i]):
                                ls = ETransverseAddition(ls, keys[i])
                elif order[i] == 8:
                        for x in range(repeatSequence[i]):
                                ls = EInverseTransverseSubtraction(ls, keys[i])
                elif order[i] == 9:
                        a, b = keys[i][0], keys[i][1]
                        for x in range(repeatSequence[i]):
                                ls = ERandomPosSubtraction(ls,a,b)
                elif order[i] == 10:
                        for x in range(repeatSequence[i]):
                                ls = EAddNextMod(ls, keys[i])
                elif order[i] == 11:
                        a, b = keys[i][0], keys[i][1]
                        for x in range(repeatSequence[i]):
                                ls = EOddEven(ls, a, b)
                elif order[i] == 12:
                        for x in range(repeatSequence[i]):
                                ls = ERevSub(ls, keys[i])
        EmultiplyRNfinal(ls, 9)
        EPenultimateEleSubFinal(ls, 52)
        print("Encrypted Data:\n",ls,"\n")

# DECRYPTION FUNCTION
def DecryptionFinal(order, keys, repeatSequence):
        global ls
        DPenultimateEleSubFinal(ls, 52)
        DmultiplyRNfinal(ls, 9)
        for i in range(11, -1, -1):
                if order[i] == 1:
                        for x in range(repeatSequence[i]):
                                ls = DmultiplyRN(ls, keys[i])
                elif order[i] == 2:
                        for x in range(repeatSequence[i]):
                                ls = DrangeMult(ls, keys[i])
                elif order[i] == 3:
                        for x in range(repeatSequence[i]):
                                ls = DsubRN(ls, keys[i])
                elif order[i] == 4:
                        for x in range(repeatSequence[i]):
                                ls = DNextNoAdd(ls, keys[i])
                elif order[i] == 5:
                        for x in range(repeatSequence[i]):
                                ls = DLeftMostEleSub(ls, keys[i])
                elif order[i] == 6:
                        for x in range(repeatSequence[i]):
                                ls = DPenultimateEleSub(ls, keys[i])
                elif order[i] == 7:
                        for x in range(repeatSequence[i]):
                                ls = DTransverseAddition(ls, keys[i])
                elif order[i] == 8:
                        for x in range(repeatSequence[i]):
                                ls = DInverseTransverseSubtraction(ls, keys[i])
                elif order[i] == 9:
                        a, b = keys[i][0], keys[i][1]
                        for x in range(repeatSequence[i]):
                                ls = DRandomPosSubtraction(ls,a,b)
                elif order[i] == 10:
                        for x in range(repeatSequence[i]):
                                ls = DAddNextMod(ls, keys[i])
                elif order[i] == 11:
                        a, b = keys[i][0], keys[i][1]
                        for x in range(repeatSequence[i]):
                                ls = DOddEven(ls, a, b)
                elif order[i] == 12:
                        for x in range(repeatSequence[i]):
                                ls = DRevSub(ls, keys[i])
        print("Decrypted Data:\n",ls,"\n")

def Encrypt(strls, order, keys, repeatSequence):
        global ls
        order = order.split(',')
        order = [int(x) for x in order]
        repeatSequence = repeatSequence.split(',')
        repeatSequence = [int(x) for x in repeatSequence]
        keys = keys.split('.')
        for i in range(len(keys)):
                if '(' in keys[i]:
                        f = keys[i].split(',')
                        a = int(f[0].replace('(', ''))
                        # print(f)
                        b = int(f[1].replace(')', ''))
                        keys[i] = (a,b)
                else:
                        keys[i] = int(keys[i])
        # ORIGINAL DATA
        stv = str(strls)
        # To convert character to ASCII number
        ls = [float(ord(x)) for x in stv]
        
        # print("Original Data:\n",ls,"\n")
        EncryptionFinal(order, keys, repeatSequence)
        mst = ",".join([str(x) for x in ls])
        ls=[]
        print(mst)
        mst = EnScramble(mst)
        print("MST: ", mst)
        return mst

def Decrypt(strs, order, keys, repeatSequence):
        global ls
        strs = DeScramble(strs)
        print("Descramble: ", strs)
        ls = strs.split(',')
        ls = [float(x) for x in ls]
        # print("Order: ", order)
        order = order.split(',')
        order = [int(x) for x in order]
        repeatSequence = repeatSequence.split(',')
        repeatSequence = [int(x) for x in repeatSequence]
        keys = keys.split('.')
        for i in range(len(keys)):
                if '(' in keys[i]:
                        f = keys[i].split(',')
                        a = int(f[0].replace('(', ''))
                        b = int(f[1].replace(')', ''))
                        keys[i] = (a,b)
                else:
                        keys[i] = int(keys[i])
        DecryptionFinal(order, keys, repeatSequence)
        # VERIFICATION
        # flag = True
        # for i in range(len(strs)):
        #         if ls[i] != b[i]:
        #                 flag = False
        #                 break
        # print(flag)

        # Print Back Information
        print("Value: ", ls)
        strls = [chr(int(i)) for i in ls]
        test = ''.join(strls)
        # print('\nDecrypted Information: ')
        # print(test)
        return test

# Decryption Key from the Database
order = [6, 9, 4, 3, 2, 1, 5, 7, 8, 12, 10, 11]
keys = [72, (2, 23), 10, 44, 300, 7, 25, 1000, 390, 14, 15, (14, 78)]
repeatSequence = [1, 3, 1, 2, 1, 1, 3, 2, 1, 1, 2, 3]

















# def EMagnitudeSwap(st,key,length):
#         for i in range(0,length,2):
#                 if(st[i]>key):
#                         temp=st[i]
#                         st[i]=st[i+1]
#                         st[i+1]=temp
#         return st

# def DMagnitudeSwap(st,key,length):
#         for i in range(1,length,2):
#                 if(st[i]>key):
#                         temp=st[i]
#                         st[i]=st[i-1]
#                         st[i-1]=temp
#         return st

##def ErangeSub(st,a=100):
##        for i in range(len(st)):
##                  if st[i]<a:
##                        st[i] = st[i]-25
##        return st
##
##def DrangeSub(st, a=100):
##        for i in range(len(st)):
##                var = st[i]+25
##                if var < a:
##                        st[i] = var                        
##        return st
# def ENextNoSub(st):p
#         for i in range(len(st)):
#                 st[i]=st[i]-st[i+1]
#         return st

# def DNextNoSub(st):
#         for i in range(len(st)-1,0,-1):
#                 st[i]=st[i]+st[i+1]
#         return st
