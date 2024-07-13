#practice Question for File Handling:
#Q1: Create a new file "practice.txt" using python. Add the following data in it:
#Hi everyone
#we are learning File I/O:
#using Java:
# I like programming in java:

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe learning File I/O.\n")
    f.write("using java.\nI like programming in java")
#Q2:  Write that replace all occurance at "java" with "python" in above file:

with open("practice.txt","r") as f:
    data=f.read()
    new_data=data.replace("java","python")
    print(new_data)
# override data:
with open("practice.txt","w") as f:
    f.write(new_data)

#Q3: search if the world "learning" exist in the file or not.
word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("Found:")
    else:
         print("Not Found")
#Q3: search if the world "learning" exist in the file or not.(using function):
def check_forword():
    word="learning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(data.find(word)!=-1):
            print("Found:")
        else:
            print("Not found:")

check_forword()#Q3: search if the world "learning" exist in the file or not.(using function):
def check_forword():
    word="learning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(data.find(word)!=-1):
            print("Found:")
        else:
            print("Not found:")

check_forword()
# 3RD Method:
#Q3: search if the world "learning" exist in the file or not.(using function):
def check_forword():
    word="learning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(word in data): #easy condition
            print("Found:")
        else:
            print("Not found:")

check_forword()

#Q4:Write to find in which line of the file does the word "learning" occure first print -1 if word not found:
def check_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
          while data:
              data=f.readline()
              if(word in data):
                  print(line_no)
                  return
              line_no+=1
    return -1

print(check_line())

#Q5: from a file containing number separated by comma, print the count of even number:
count=0
with open("Number.txt","r") as f:
        data=f.read()
        num=data.split(",")
        print(num)
for val in num:
        if(int(val)%2==0):
            count+=1

print("count the EVEN number:",count)






