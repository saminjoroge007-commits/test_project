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
# (*nested if) Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"

student_score = float(input("Enter student score: "))
attendance = float(input("Enter attendance: "))

if student_score > 90:
    if attendance > 80:
        print("Excellent student")
    else:
        print("Good score, but attendance needs improvement")

#1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
#I#f start_date comes before end_date, print "Valid period",
#If start_date is after end_date, print "Invalid period".
#If both dates are the same, print "One-day period".
#2.Given two strings str1 and str2, write a conditional statement that checks:
#If str1 is longer than str2, print "str1 is longer".
#If str2 is longer than str1, print "str2 is longer".
#If both have equal length, print "Both are of equal length".

start_date = '2024-01-01'
end_date = '2024-12-31'
if start_date < end_date:
    print("valid Period")
elif start_date > end_date:
    print("Invalid period")
