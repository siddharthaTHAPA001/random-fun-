# # Student Marks Analyzer

# # taking number of students
# n = int(input("Enter number of students: "))

# marks = []

# # taking marks input
# for i in range(n):
#     m = float(input(f"Enter marks of student {i+1}: "))
#     marks.append(m)

# # calculations
# total = sum(marks)
# average = total / n
# highest = max(marks)
# lowest = min(marks)

# # result
# print("\n--- Result ---")
# print("Total Marks:", total)
# print("Average Marks:", average)
# print("Highest Marks:", highest)
# print("Lowest Marks:", lowest)

# # pass or fail (assuming pass mark = 40)
# if average >= 40:
#     print("Result: PASS ")
# else:
#     print("Result: FAIL ")





#NUMBER GUSSING GAME:
# import random
# secret = random.randint(1,50)
# attempts = 0
# print("guess the number between 1 and 5")
# while True :
#     guess = int(input("Enter the guess:"))
#     attempts +=1
#     if guess >secret:
#         print("high")
#     elif guess< secret:
#         print("low")
#     else:
#         print("The guess is correct!")
#         print("you guessed it in,",attempts,"attempts")
#         break
    

#lets create a Atm menu:
balance = 50000
while True:
    print("\n---ATM MENU----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = input("Enter your choice (1-4):")
    if choice == "1":
        print("Your balance is :",balance)
    elif choice == "2":
        amount = int(input("Enter amount to deposit"))
        balance += amount
        print("Deposit sucessful")
    elif choice == "3":
        amount = int(input("Enter the amount to withdraw"))
        if amount >balance:
            print("insufficient balance")
        else:
            balance -= amount
            print("please collect your cash")
            print(f"the remaining balance is:${balance}")
    elif choice == "4":
        print("Thank you for using the ATM")
        break
    else:
        print("Invalid choice! Try again")