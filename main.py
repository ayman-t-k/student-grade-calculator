
def get_mark(subject):
    while True:
        try:
            mark = float(input("Enter " + subject + " mark: "))

            if 0 <= mark <= 100:
                return mark
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


# Get student details
name = input("Enter student name: ")

mark1 = get_mark("first")
mark2 = get_mark("second")
mark3 = get_mark("third")

# Calculate average
average = (mark1 + mark2 + mark3) / 3

# Display results
print("\n----- STUDENT RESULT -----")
print("Student Name:", name)
print("Average Marks:", format(average, ".2f"))

# Calculate grade
if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
