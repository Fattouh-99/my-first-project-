import json  # Importing a tool to read and write data in JSON format
import matplotlib.pyplot as plt  # Importing a tool for making graphs

# Function to load student data from a file
def load_data(file_name):
    try:
        with open(file_name, 'r') as file:  # Open the file in read mode
            return json.load(file)  # Load the data from the file in JSON format
    except FileNotFoundError:  # If the file is not found
        print(f"File '{file_name}' not found. Creating a new file.")
        return []  # Return an empty list

# Function to save student data to a file
def save_data(students, file_name):
    try:
        with open(file_name, 'w') as file:  # Open the file in write mode
            json.dump(students, file, indent=4)  # Write the data to the file in JSON format with indentation
    except Exception as e:  # Catch any exception that occurs
        print(f"An error occurred while saving data to '{file_name}': {e}")

# Function to add students
def add_students(students, subjects):
    try:
        num_students = int(input("Enter the number of students to add: "))  # Asking the user how many students they want to add
        for _ in range(num_students):  # Loop for each student
            name = input("Enter student name: ")  # Asking for the student's name
            grades = {}  # Creating an empty dictionary for grades
            for subject in subjects:  # Looping through each subject
                if subject == "Math":  # If subject is Math
                    subject_name = "Computer Architecture"  # Change it to Computer Architecture
                elif subject == "Science":  # If subject is Science
                    subject_name = "Intro to Programming"  # Change it to Intro to Programming
                elif subject == "English":  # If subject is English
                    subject_name = "Object Oriented Programming"  # Change it to Object Oriented Programming
                else:
                    subject_name = subject  # Otherwise, keep the subject name as it is
                grade = float(input(f"Enter {subject_name} grade (0-100) for {name}: "))  # Asking for the student's grade in each subject
                grades[subject_name] = grade  # Adding the grade to the dictionary
            students.append({"name": name, "grades": grades})  # Adding the student's name and grades to the list of students
        print("Students added successfully.")  # Confirming that students have been added
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to calculate average grades for all students
def calculate_averages(students):
    for student in students:  # Looping through each student
        grades = student["grades"].values()  # Extracting the grades of the student
        avg_grade = sum(grades) / len(grades)  # Calculating the average grade
        student["average_grade"] = avg_grade  # Adding the average grade to the student's data

# Function to sort students based on average grades
def sort_students(students):
    return sorted(students, key=lambda x: x.get("average_grade", 0), reverse=True)  # Sorting the students based on their average grades in descending order

# Function to display bar graph of student averages
def display_graph(students):
    names = [student["name"] for student in students]  # Extracting student names
    avg_grades = [student["average_grade"] for student in students]  # Extracting their average grades

    plt.figure(figsize=(10, 6))  # Setting the size of the graph
    plt.bar(names, avg_grades, color='skyblue')  # Creating a bar graph
    plt.xlabel('Students')  # Labeling the x-axis
    plt.ylabel('Average Grade')  # Labeling the y-axis
    plt.title('Average Grades of Students')  # Setting the title of the graph
    plt.xticks(rotation=45, ha='right')  # Rotating the x-axis labels for better readability
    plt.tight_layout()  # Adjusting layout
    plt.show()  # Displaying the graph

# Main function
def main():
    file_name = "student_data.json"  # Name of the file to store student data
    students = load_data(file_name)  # Loading existing student data from the file
    new_students = []  # Track students added in the current session
    subjects = ["intro to programing", "object oriented programing", "computer architechture"]  # List of subjects

    while True:  # Loop until the user chooses to exit
        print("\nStudent Grade Tracker")  # Displaying the main menu
        print("1. Add Students")
        print("2. Calculate Averages")
        print("3. Sort Students")
        print("4. Display Graph")
        print("5. Exit")

        choice = input("Enter your choice: ")  # Asking the user to enter their choice

        if choice == "1":  # If the user chooses to add students
            add_students(new_students, subjects)  # Calling the function to add students
        elif choice == "2":  # If the user chooses to calculate averages
            calculate_averages(new_students)  # Calling the function to calculate averages
            print("Averages calculated successfully.")  # Confirming that averages have been calculated
        elif choice == "3":  # If the user chooses to sort students
            sorted_students = sort_students(new_students)  # Sorting the students based on average grades
            for i, student in enumerate(sorted_students, start=1):  # Looping through each student
                print(f"{i}. {student['name']}: {student.get('average_grade', 'N/A')}")  # Displaying the student name and average grade
        elif choice == "4":  # If the user chooses to display the graph
            if not new_students:  # If no new students have been added
                print("No new student data available. Please add students and calculate averages first.")  # Informing the user
            else:
                display_graph(new_students)  # Calling the function to display the graph
        elif choice == "5":  # If the user chooses to exit
            students.extend(new_students)  # Adding new students to the main list
            save_data(students, file_name)  # Saving student data to the file
            print("Exiting program...")  # Informing the user
            break  # Exiting the loop
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")  # Informing the user if an invalid choice is entered

if __name__ == "__main__":
    main()  # Calling the main function to start the program
