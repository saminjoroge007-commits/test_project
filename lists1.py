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
#task pg. 35


#create a new file list_task.py
trainees = ["John", [2, ["James","Mary"]]]
#1. Display 2 from the list.
trainees = ["John", [2, ["James","Mary"]]]
print(trainees[1][0])
#2. Output James  from the list.
print(trainees)
#3. Using a method add 56 at the end of the list.
trainees.append('56')
print(trainees)
#4. Using a method add the name Mike between James and Mary(instert
trainees[1][1].insert(1, 'Mike')
print(trainees)
#5. Change the value of 2 to 8
trainees[1][0]=8
print(trainees)
#6. Remove John and Mary from the list.
trainees.remove('John')
print(trainees)

# Mary removal
trainees[0][1].pop()
print(trainees)
#7. Using a function, determine the length of the list
print(len(trainees))

employees = ["TechElar",[4, ["Kevin", "Brian", "Alice"]]]

# 1. Display the number 4.

# 2. Display "Brian" from the list.

# 3. Display "Alice" from the list.

# 4. Using a list method, add the number 7 at the end of the outer list.

# 5. Add "David" between "Brian" and "Alice".

# 6. Change the number 4 to 10.

# 7. Change "Kevin" to "James".

# 8. Remove "TechElar" from the list.

# 9. Remove "Alice" from the nested list.

# 10. Add "Mary" at the beginning of the nested list.

# 11. Using len(), find the number of items
#     in the nested employee list.

# 12. Print the final list.