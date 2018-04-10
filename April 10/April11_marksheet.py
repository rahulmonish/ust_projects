from operator import itemgetter
import operator

def flatten(seq):
  for el in seq:
    if isinstance(el, list):
      yield from flatten(el)
    else:
      yield el


student=[[" ",0,0,0,0],
[" ",0,0,0,0],
[" ",0,0,0,0],
[" ",0,0,0,0],[" ",0,0,0,0],
[" ",0,0,0,0],[" ",0,0,0,0]]

for i in range(2):
        student[i][0]= input("enter the name ")
        student[i][1]= int(input("enter mark1 "))
        student[i][2]= int(input("enter mark2 "))
        student[i][3]= int(input("enter mark3 "))
        student[i][4]= int(input("enter mark4 "))
        
maxm=0
total=0
total_max=0
for i in range(2):
    maxm=0
    total=0
    for j in range(1,5):
        total+= student[i][j]

        if maxm<student[i][j]:
            maxm= student[i][j]
    
    if(total_max<total):
        total_max= total
        index=i
    print("The max mark of ",student[i][0], " is ", maxm)
print("The topper is ",student[index][0]," with marks ",total_max)

print("The marks of first 2 roll numbers are " )

for i in range(2):
    print("for ",student[i][0])
    for j in range(1,5):
        print(student[i][j])
        
'''       
name_sort = sorted(student, key =itemgetter(0))
print(name_sort)
'''
for i in range(5,7):
        student[i][0]= input("enter the name ")
        student[i][1]= int(input("enter mark1 "))
        student[i][2]= int(input("enter mark2 "))
        student[i][3]= int(input("enter mark3 "))
        student[i][4]= int(input("enter mark4 "))