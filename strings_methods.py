#methods- Functions inside a class are called methods. Methods are used to define the behaviors of an object. They can access and modify the attributes of the class. Methods are defined using the 'def' keyword, just like regular functions, but they must have 'self' as their first parameter to refer to the instance of the class.
#functions inside class str that are used to manipulate strings are called string methods. These methods can be called on string objects to perform various operations, such as changing case, searching for substrings, replacing characters, and more.

# clean sentence to "Python programming"
sentence="    PYThon ProgrammING"
sentence1=sentence.strip().capitalize()
print(sentence1)


#clean sentence2 to "SOFTWARE DEVELOPMENT"
sentence2 = "Software Development     "
sentence2_cleaned = sentence2.strip().upper()
print(sentence2_cleaned)

#clean sentence3 to "computer science"
sentence3 = "      COMputer ScieNCE   "
sentece3_cleaned = sentence3.strip().lower()
print(sentece3_cleaned)

#clean sentence4 to "Techcamp Kenya"
sentence4 = "TECHcamp Kenya    "
sentence4_cleaned = sentence4.strip().title()
print(sentence4_cleaned)

sentence6 = "Alex Kimani"
sentence6 = sentence6.replace("Kimani", "Mwangi")
print(sentence6)

sentence7 = "Python programming"
sentence7 = sentence7.count("o")
print(sentence7)

sentence8 = "Alex:Brian:Mike:Kevin"
sentence8 = sentence8.split(":")
print(sentence8)
