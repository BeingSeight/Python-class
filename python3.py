# Creatinglist from string... using list function
s="Python Programming"
l=list(s)
print(l)

## Traversingthe list using whie loop
ls3 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
i=0
while i<len(ls3):
    print(ls3[i], end= " ")
    i+=i+1


# to display elements throough index
l=["A","B","C"]
x=len(l)
for i in range(x):
    print(l[i], "is available at positive index: ")

# Modifying elemnts of list
id = [1, 2, 3]
emp_name = ["Sam", "Ram", "Tom"]
num_emp = 3
emp_list = [id, emp_name, num_emp]
print(emp_list)
emp_list[2] = 2
emp_list[1][1] = "Karan"
print(emp_list)
emp_list[1][0:2]=["Hari", 'Geeta']
print(emp_list)

# Values being assigned must be sequence (list, tuple or string)
x=[20, 40, 40, 'a', 'z']
x[0:4]="bc"
print(x)
x[0:10]=(11,22)
print(x)
x[0:10]=[3,4,5]
print(x)

# 1. list_name.append(element) adding at the end of the list
list1=[]
list1.append("A")
list1.append("B")
list1.append("C")
print(list1)

# Loop can be used to add multiple elemnts in the list.
#  To add elements to list upto 100 which are divisible by 10

list2=[]
for i in range(101):
    if(i%10==0):
        list2.append(i)
print(list2)

# Adding Tuples to List
list1=[1,2,3]
list1.append((5,6))
print("\nList after Addition of a Tuple:")
print(list1)

# Addition of List to a List
list3 = ['abc', 'def']
list1.append(list3)
print("\nList after Addition of List:")
print(list1)

# Appending element to end of a nested list
emp_list = [[1,2,3],['Ram','John','Sam'],3]
print("Original emp_list",emp_list)
emp_list[0].append(4)
print("After appending 4 to empid", emp_list)
emp_list[1].append('Karan')
print("After appending 'Karan' to empname", emp_list)
emp_list.append([27, 32, 44, 35])
print("After appending another list ", emp_list)

# Inserting elements into a list at specified position
list4=[10,20,30]
print(list4)
# inserting element 40 at index 1
list4.insert(1,40)
print(list4)
# inserting element 50 at index 10
list4.insert(10,50)
print(list4)
# inserting element 150 at index -10
list4.insert(-10,150)
print(list4)

# Access elements of a Nested Dictionary
people = {'name':'John','age':'27'},{'name':'Marie','age':'22'},
print(people)

# Add another dictionary to the nested dictionary
people = {'name':'Peter','age':'29','married':'Yes'}
print(people)
del people['married']
print(people)

# Accessing elements of a Nested Dictionary
for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    for key in p_info:
      print(key + ":", p_info[key])