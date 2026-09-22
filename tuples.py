# Tuples - store multiple items that can be of any datatype. They are ordered(have index)
# They cannot be changed
# items are enclosed with normal brackets()
# All tuples belong to class tuple
# Commas make them a tuple
fruits =('mango', 'oranges', 'banana', 'grapes', 'kiwi')
print(fruits)
print(type(fruits))
# Display bananas
print (fruits[2])
#display all except to lemon
print (fruits[1:4])

# convert to list using list() function
fruits=list(fruits)
print (fruits)

# Update the list
fruits[2]= "strawberries"
print(fruits)

#add guava to the end of the list
fruits.append("guava")
print (fruits)

#convert back into tuples
fruits=tuple(fruits)
print (fruits)

#task
days=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
#1. Find wednesday using an index
print (days[2])
#2. using a function find the lendt of the tuple
print(len(days))
#3. Replace Thursday with Thur
days=list(days)
days[3]='Thur'
print(days)
days=tuple(days)
print (days)