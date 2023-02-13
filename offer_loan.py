userAge = int(input("Enter Your Age: "))
annualIncome = int(input("Enter Your Annual Income: "))
previousLoan = input("Have you received a loan before? Type Yes or No: ").lower()

if userAge >= 21:
    if annualIncome >= 21000:
        if previousLoan != "Yes":
            print("The loan can be offered:",bool("True"))
else:
    print("The loan can be offered:",bool("False"))