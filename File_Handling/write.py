s = open("resume.txt","w")
#Open function is called to open a file
#open("file_name","mode")  Modes : Read(r),Write(w),Append(a)

#input data and store data in the file dynamic
name = input("Enter your name: ")  #Dynamic: Taking everything from user
s.write("Name : "+name+"/n")   #/n : new line → Thise will store code in Practise.txt

mobile = input("Enter your mobile no. : ")
s.write("Mobile : "+mobile+"/n")

experience = input("Enter your Experience : ")
s.write("Experience : "+experience+"/n")

s.close()  #Close the file
