fruits =['mango', 'oranges', 'banana', 'grapes', 'kiwi']
print(fruits)
print(type(fruits))

#indexing and slicing 
print(fruits[2])
print(fruits[-2])

# slicing used to extract a part of a list using index [start_index:end_index=1]
print(fruits[1:4])

#$updating itsms in the list
fruits[2]='pineapples'
print (fruits)

#create a list of days of the week
week=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#display day today
print(week[1])
#display wednesday to saturday 
print(week[2:6])

#append- add an item to the end of the list
fruits.append('watermelon')
print(fruits)

#insert- add an item at a specific index
fruits.insert(3, "passionafruit")
print(fruits)

#update thursday to thur
week[3]='Thur'
print(week)

#add jan at the end of the list
week.append('January')
print("week")

#add December btn wed and thursday
week.insert(3, 'December')
print(week)

# remove(item) an item from the list
fruits.remove('grapes')
print(fruits)

#pop(index) removes the last item from the list if no idex is specified
fruits.pop()
print (fruits)

fruits.pop(1)
print(fruits)


# clear-removes all the items in the list
fruits.clear()
