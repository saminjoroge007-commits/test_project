name="  JOHn  ." #Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 

name = "  JOHn  ."
name=name.lstrip().lower()
name=name.rstrip(".")

print(name)


#Slice the below string to get you the resulting sentence:
 #This will give you the starting index of the substring "Clinton forces" in the sentence_two string.

sentence_one = "The Dog Breed is German Shepherd" # only display "Breed is German"

sentence_one = sentence_one[8:23]

print(sentence_one)

#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two.index("Clinton forces"))
sentence_two = sentence_two[16:30]
print(sentence_two)

#Split the below sentence using a semicolon i.e ; And display length of the result. 
#The lazy dog; ran so fast; it hit the wall.
sentence_three = "The lazy dog; ran so fast; it hit the wall."
sentence_three = sentence_three.split(";")
print(len(sentence_three))

#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name = "  Joh.n"
last_name = "   Do,e"
first_name = first_name.strip().replace(".","")
last_name = last_name.strip().replace(",","")
print(first_name + " " + last_name)

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r = '["E","W","C"]'
r=r.replace("[","").replace("]","").replace('"',"").replace(",","")
print(r)