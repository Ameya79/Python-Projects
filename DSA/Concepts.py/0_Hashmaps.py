#dics or hashmaps are key value pairs
#think of it as an actual dictionary where a word is a key and its definition is like the value
#so like that they are key value pairs
#used to hod multiple key value pair all can be of different datatypes
#SYNTAX
Student = {
'name': 'Ameya'
,'height': 5.11
, 'Marks': [12,19,18]
}

print(Student) #prints entire dic
print(Student['name']) #way to print only desired value 

#note keys can also be an integer
#error caused when key does not exist : key error

#method1
#to avoid this error we can use .get method cuz by using .get we wont get this error if the key is not in the dic
print(Student.get('height')) #gets ht
print(Student.get('weight')) #gets none as non existing key
print(Student.get('weight','not found')) #gets nothing but instead shows a message not found instead of none as it is non existing key

#method2
Student['Phone'] = '5555-5555' #to add key to the dictionary
print(Student.get('Phone','not found'))

#method3
Student['height'] = '5.7' #to update a single key to the dictionary
print(Student.get('Height','not found'))
print(Student)

#method4b update multiple stuff at a time and add to if wished
Student.update({'name':'Aron','Age':31,'height': 5.2}) #this upades the current fields while adds new one
print(Student)

#method4
del Student['Age']  #deletes the age of the student
print(Student)

#method 5 
print(len(Student)) #length of dic
#to print all keys
print(Student.keys())
#to print all values
print(Student.values())

#looping
for key, values in Student.items():
    print(key, values)


