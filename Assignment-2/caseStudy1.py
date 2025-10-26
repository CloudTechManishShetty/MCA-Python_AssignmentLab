def calculate_grade(marks):
    remarks = "No remarks available."

    def grade_category():
        nonlocal remarks

        if marks >= 75:
            grade = 'A'
            remarks = "Pass with Distiniction"
        elif marks >= 60:
            grade = 'B'
            remarks = "First Class"
        elif marks >= 50:
            grade = 'C'
            remarks = "Second Class"
        elif marks >= 40:
            grade = 'D'
            remarks = "Pass"
        else:
            grade = 'F'
            remarks = "Fail"
        
        return grade

    final_grade = grade_category()

    print("Marks: ",marks)
    print("Grade: ",final_grade)
    print("Remarks: ",remarks)
    print("-" * 20)

marks = int(input("Enter the Total Marks Obtained: "))
calculate_grade(marks)