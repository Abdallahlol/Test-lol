def input_grades():
    grades = []
    print("Enter your grades for each subject. Type 'done' to stop.")
    while True:
        subject = input("Enter subject name: ")
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {subject}: "))
            if 0 <= grade <= 100:  # Ensure grade is valid (between 0 and 100)
                grades.append((subject, grade))
            else:
                print("Invalid grade. Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    return grades
