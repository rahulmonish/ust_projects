word=input("enter the string")
count=0
n= len(word) - word.count(' ')
for i in word:
    if i.isdigit()==True:
        count+=1
print("no of letters : ", n)
print("no of digits : ", count)