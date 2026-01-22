def get_marks():
    while True:
        try:
            marks = int(input("Enter your marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Please try again.")
        except ValueError:
         print("Please enter a valid integer.")

def calculate_grade(marks):
    if marks >= 90:
        return 'A', "Excellent work! Keep shining."
    elif marks >- 80:
        return 'B', "Great job! You're doing well."
    elif marks >= 70:
        return 'C', "Good effort! You can do even better."      
    elif marks >= 60:
        return 'D', "You passed, but there's room for improvement." 
    else:
        return 'F', "Don't give up!"


def main():
    name = input("Enter student name:")
    marks = get_marks()
    grade, message = calculate_grade(marks)

    print(f"\nStudent Name: {name}")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}  ")
    print(f"Message: {message}")

main()    