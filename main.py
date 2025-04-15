# Function to convert letter grade to grade points
def letter_to_points(grade):
    grade_map = {
        'A': 5.0,
        'B': 4.0,
        'C': 3.0,
        'D': 2.0,
        'E': 1.0,
        'F': 0.0
    }
    return grade_map.get(grade.upper(), None)


def calculate_gpa():
    try:
        num_courses = int(input("Enter the number of courses: "))

        total_grade_points = 0.0
        total_credits = 0

        # Collect information for each course
        for course_number in range(num_courses):
            print(f"\n> For Course {course_number + 1}:")

            # Loop to get a valid letter grade
            while True:
                grade = input("Enter the letter grade (A, B, C, D, E, F): ").strip().upper()
                points = letter_to_points(grade)
                if points is not None:
                    break  # Exit the loop when the grade is valid
                print(f"Invalid grade '{grade}' entered. Please enter a valid grade.")

            # Get credit hours and ensure a numeric value
            while True:
                try:
                    credit_hours = int(input("Enter the credit hours for this course: "))
                    break  # Exit the loop when the input is valid
                except ValueError:
                    print("Invalid input. Credit hours must be an integer. Please try again.")

            # Accumulate results
            total_grade_points += points * credit_hours
            total_credits += credit_hours

        # Calculate GPA
        gpa = total_grade_points / total_credits
        print(f"\nYour GPA is: {gpa:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for the number of courses and credit_hours.")


# Run the program
calculate_gpa()
