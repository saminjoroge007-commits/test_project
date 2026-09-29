# Nested If Statements
# => series of conditional statements inside another conditional statement
# Nested if can only be executed based on the result of the previous condition

# if condition1:
   #if condition2:
      # if block2  *both conditions are true
    #else:
        #else block2  *condition2 is not true
#else:
    #else block1   *only condition1 is correct

1.# write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive

age=input("Enter your age: ")
age=int(age)

if age>=18:
    license=input("Do you have a Drivers license? Yes/No: ")
    if license=='Yes':
       print("You are eligdible to Drive")
    else:
       print("You are not Elidgible to Drive")
else:
   print("You are too young to drive")


2.# Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."

credit_score=input("Enter your Credit Score: ")
credit_score=int(credit_score)
annual_income=input("Enter your annual income: ")
annual_income=float(annual_income)

if credit_score>700:
   #annual_income=input("Is your annual income above 50,000? Yes/No: ")
   if annual_income>50000:
   
  # if annual_income=='Yes':
    print("Loan approved.")
   else:
      print("Income requirements not met.")
else:
   print("Credit score too low.")