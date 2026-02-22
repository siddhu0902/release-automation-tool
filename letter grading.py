#Calculate the letter grades of students based on their average marks in 5 subjects

student_count = int(input("Enter the number of students: "))
count = 0

while(count<student_count):
    english_marks = int(input("Enter the marks of English: "))
    math_marks = int(input("Enter the marks of Math: "))
    physics_marks = int(input("Enter the marks of Physics: "))
    chemistry_marks = int(input("Enter the marks of Chemistry: "))
    computer_marks = int(input("Enter the marks of Computer: "))
    average_marks = (english_marks + math_marks + physics_marks + chemistry_marks + computer_marks) / 5
    print(average_marks)

    if(average_marks>=90):
        letter_grade = "A"
        print("The letter grade is A")
    elif(average_marks>=80):
        letter_grade = "B"
        print("The letter grade is B")
    elif(average_marks>=70):
        letter_grade = "C"
        print("The letter grade is C")
    elif(average_marks>=60):
        letter_grade = "D"
        print("The letter grade is D")
    elif(average_marks>=50):
        letter_grade = "E"
        print("The letter grade is E")
    elif(average_marks<50):
        letter_grade = "F"
        print("The letter grade is F")
    else:
        print("Invalid input")

    print("Letter Grade", letter_grade)
    count+=1


