#Update in "resume.txt" file
s = open("resume.txt","a")  #a → append/update
email = input("Enter your email adress: ")
s.write("Email : "+email+"/n")