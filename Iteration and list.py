#for loops
vegetables=['Carrot','Onions','Tomatoes']
for vegetable in vegetables:
    print(vegetable)

#For loops in addition
nums=[1,2,3]
s=0
for num in nums:
    s=s+num
    print(s)

#For loops in password
def password_controller(password):
    if len(password)>8:
        return True
    else:
        return False
password_list=["qwer","123456","098765432","abcdefgh"]
for password in password_list:
    result=password_controller(password)
    print(password,result)

#For loops in range
total=0
for numbers in range(1,100):
    total +=numbers
    print(total)

#While Loops
number_of_hurdles=6
while number_of_hurdles>0:
    number_of_hurdles -=1
    print(number_of_hurdles)

#Print all numbers between 1-11 except 5
for num in range(1,11):
    if num==5:
        continue
        print(num)

#print all numbers between 1-11 except 5 using while loop
num=11
while num>0:
    num -=1
    if num ==10:
        break
        print(num)