print("hello World")
print("hello World")
print("hello World")
print("hello World")
print("hello World")
print("hello World")
print("hello World")


def greet(name):
    print("Hello, " + name + ". Good morning!")


sum=0

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]


for val in numbers:
    sum = sum+val

print("The sum is", sum)


print(range(10))

print(list(range(10)))

print(list(range(2, 8)))

print(list(range(2, 20, 3)))


genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])
    
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")
    
    
# program to display student's marks from record
student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')
    


# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum_while = 0
i = 1

while i <= n:
    sum_while = sum_while + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum_while)


'''Example to illustrate
the use of else statement
with the while loop'''

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
    
    
    
# Use of break statement inside the loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")



for i in numbers:
    greet('Lova Chittumuri')
    
    
    
    