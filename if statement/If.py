degree_passed = float(input("Enter the degree passed: "))
degree_student = float(input("Enter the degree student: "))

# Check if the degree_student is a valid number between 0 and 100
if degree_student < 0 or degree_student > 100:
    print("Invalid input, please enter a valid degree value.")
elif degree_passed > degree_student:
    print("The student failed in the exam.")
else:
    print("The student passed with distinction in the exam.")
