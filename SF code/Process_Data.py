#---------------------------------------------------
#------ Created  : 01/01/2025 - Sulman Qudeer
#------ Modified : 10/02/2025 by Sulman Qudeer
#------ Description : Software Foundation Module - Python File Handling Tutorial 
#------ Description : Computational Reasoning Module (Excel Tutorials Week 2-7)
#----------------------------------------------------

import csv  # Import CSV module for handling file reading & writing

#---------------------------------------------------
#------ Define Functions for Calculations ---------
#---------------------------------------------------

def calculate_average(scores):
    """
    Calculate the average score from a list of subject scores.
    Returns the computed average.
    """
    return sum(scores) / len(scores) if scores else 0  # Avoids division by zero

def assign_grade(average):
    """
    Assigns a grade based on the calculated average score.
    """
    if average >= 85:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 65:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

#---------------------------------------------------
#------ Read Student Data from CSV File -----------
#---------------------------------------------------

students = []  # List to store processed student data

try:
    # Attempt to open the students.csv file for reading
    with open('Students.csv', 'r') as file:
        reader = csv.reader(file)  # Create CSV reader object
        
        header = next(reader)  # Read the header row
        
        for row in reader:
            try:
                # Extract student details from each row
                name, art, english, maths = row
                scores = [int(art), int(english), int(maths)]  # Convert scores to integers
                average = calculate_average(scores)  # Compute average score
                grade = assign_grade(average)  # Determine the grade
                
                # Append processed student record to list
                students.append([name, art, english, maths, average, grade])
            
            except ValueError:
                print(f"⚠️ Warning: Invalid data found in row {row}. Skipping this entry.")

except FileNotFoundError:
    print("❌ Error: 'Students.csv' not found. Please check the file location.")
    exit(1)  # Gracefully exit the program if the file is missing

#---------------------------------------------------
#------ Write Processed Data to Results File ------
#---------------------------------------------------

try:
    with open('Student_Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)  # Create CSV writer object
        
        # Write header row to the output CSV file
        writer.writerow(['Name', 'Art', 'English', 'Maths', 'Average', 'Grade'])
        
        # Write all processed student records
        writer.writerows(students)

    print("✅ Results successfully saved to 'Student_Results.csv'.")

except Exception as e:
    print(f"❌ Error: Unable to write to 'Student_Results.csv' - {e}")
