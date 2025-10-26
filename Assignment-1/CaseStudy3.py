marks = [44,35,48,47,50];
details = (60,"01-01-2005");
subjects = {"Python","DS","Cloud","SEPM","Data"};

student_profile = {
    "Name": "Manish Shetty",
    "Roll-no": details[0],
    "Date of Birth": details[1],
    "Marks": marks,
    "Subjects": subjects
};


total_marks = sum(student_profile["Marks"]);
number_of_subjects = len(student_profile["Marks"]);
average_marks = total_marks / number_of_subjects;


highest_score = max(student_profile["Marks"]);

is_enrolled_in_BS = "Business" in student_profile["Subjects"];
is_enrolled_in_math = "Mathematics" in student_profile["Subjects"];


# --- Display Results ---
print("Displaying Students Profile and Report...");
print("--- Student Profile ---");
print("Name: ",student_profile['Name']);
print("Roll Number: ",student_profile['Roll-no']);
print("Date of Birth: ",student_profile['Date of Birth']);
print("-" * 25)

print("\n--- Academic Details ---");
print("Marks: ",student_profile['Marks']);
print("Unique Subjects : ",student_profile['Subjects']);

print("\n--- Analytical Results ---");
print(f"Total Marks: {total_marks}");
print(f"Average Marks: {average_marks:.2f}");
print(f"Highest Score: {highest_score}");

print("\n--- Set Operations Example ---");
print("Is ",student_profile["Name"]," enrolled in BS?", is_enrolled_in_BS);
print("Is ",student_profile["Name"]," enrolled in Mathematics?", is_enrolled_in_math);