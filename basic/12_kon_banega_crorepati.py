question = [
    ["what is my name ?",
     "A. Maitri","B. Hasti","C. Riyen","D. Deep","A"],

     ["What is my age ?",
     "A. 21","B. 22","C. 23","D. 24","A"],

     ["What is my weight ?",
      "A. 45kg","B. 50kg","C. 55kg","D. 60kg","B"]

]
prizes =[1000,5000,10000]
safe_level = {}
print("Welcome to Kon Banega Crorepati")
print("...............................")

winning = 0
for i in range(len(question)):
    print(f"Your question for Rs.{prizes[i]} is:")
    print(question[i][0])
    print(question[i][1])
    print(question[i][2])
    print(question[i][3])
    print(question[i][4])
    answer = input("Enter your answer (A/B/C/D): ")
    if answer.upper() == question[i][5]:
        winning = prizes[i]
        print(f"Correct answer! You have won Rs.{winning}")
        print("\n")
        if winning == 5000:
            safe_level[1] = winning
        elif winning == 10000:
            safe_level[2] = winning
    else:
        print("Wrong answer!")
        print("\n")
        if len(safe_level) == 0:
            winning = 0
        elif len(safe_level) == 1:
            winning = safe_level[1]
        elif len(safe_level) == 2:
            winning = safe_level[2]
        break
print(f"You are leaving with Rs.{winning}")
