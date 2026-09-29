if 20>10:
    print('20 is greater')

age=30
if age>18:
    print("Adult")

if age>=18 and age<=60:
    print('Access Granted')

#temp=18
    # if statement application
#if temp>30:
    print('too hot')
    # else statement application\
else:
    print('warm')

#   if-else statement=>    else executes the else block when the condition is false(otherwise of if)\
#  syntax
#  if statement

# print access granted if password is similar with Admin@254! otherwise access denied

password=input("Enter a password: ")
correct_password= 'Admin@2541!'
if password==correct_password:
      print('access granted')
else:
    print('access denied')


# if-elif-else=>Elif is used when we have a multiple conditions with different outcomes
#syntax
#if condition:
   # if block 
# elif condition:
#elfit block2
#else:
   #else block

   ##temparature
temp=45
if temp>30:
    print('too hot!')
elif temp>15:
    print("moderate temparature")
else:
    print('cold temparature!')

marks= 45

if marks>80:
    print("A")
elif marks>70:
    print("B")
elif marks>60:
    print("c")
elif marks>50:
    print("D")
else:
    print("E")