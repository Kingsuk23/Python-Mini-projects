import random
import string

punctuations = string.punctuation
digits=string.digits
letters='abcdefghijklmnopqrstuvwxyz'

gen_pass=[]

howManyLatter=int(input("How many letter you want: "))
howManyNumer=int(input("How many number you want: "))
howManySpacialCharacter=int(input("How many spacial character you want: "))

def gen_method(length,array,is_alpha=False):
    for i in range(length):
        index=random.randint(0,len(array)-1)
        value=array[index]
        if is_alpha:
            case=random.randint(0,1)
            if case==1:
                value=value.upper()
        gen_pass.append(value)

gen_method(howManyLatter,letters,True)
gen_method(howManyNumer,digits)
gen_method(howManySpacialCharacter,punctuations)
random.shuffle(gen_pass)
str_password=""
for pass_value in gen_pass:
    str_password=str_password+str(pass_value)
print(str_password)