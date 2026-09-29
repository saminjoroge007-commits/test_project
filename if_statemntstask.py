#Take three inputs from a user, separately. Print the largest of the numbers.
#   Hint: Determine what type of data is taken in as input.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

#Temparature check
temp = float(input("Enter temperature in °C: "))

if temp > 30:
    print("The temperature is too high")
elif temp > 15:
    print("Normal temperature")
else:
    print("Cold temperature")

# Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
#and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if 10 <= x <= 20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")




#Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password = input("Enter password: ")

if password == "secret123":
    print("Access granted")
else:
    print("Access denied")
# Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"

student_score = float(input("Enter student score: "))
attendance = float(input("Enter attendance: "))

if student_score > 90:
    if attendance > 80:
        print("Excellent student")
    else:
        print("Good score, but attendance needs improvement")