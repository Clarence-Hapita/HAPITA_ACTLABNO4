print("Hello! how are you? Can I know your name?")

name = input("Enter your name:")
print("Hello,"+name,"can you insert your grade and I'll tell if you failed or not!")


while True:
    try:
        assign_grade = int(input("Your Grade:"))
        if assign_grade>=90:
            print("Grade A")
            print("WOOOOW GREATTT!")
        elif assign_grade>=80:
            print("Grade B")
            print("Nice!")
        elif assign_grade>=70:
            print("Grade C")
            print("meh at least you passed.")
        elif assign_grade<=60:
            print("Grade F")
            print("Awww you failed.")
        else:
            print("Input your Grades in numbers, please:")
            break
    except: 
        print("Input your Grades in numbers, please:")