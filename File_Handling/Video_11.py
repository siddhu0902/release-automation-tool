#Video_11

'''
file handling
-file contains data.
-file can be .txt,.pdf,.doc etc.
In python we can perform, few operations:
  → Create a new file
  → Store some data in a file
  → Update data in File
  → Read file
  → Delete file
These operations can be performed by using built-in functions!

Task:
Wap to create a Resume/CV using file handling
1. Create a "Practise.txt
2. We will write code in py. 
3. insert the data in practise.txt

'''
 
s = open("resume.txt","w")
#Open function is called to open a file
#open("file_name","mode")  Modes : Read(r),Write(w),Append(a)
name = input("Enter your name: ")  #Dynamic: Taking everything from user
s.write("Name : "+name+"/n")   #/n : new line → Thise will store code in resume.txt