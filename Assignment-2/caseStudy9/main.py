import Science.subjects as science_sub
import Arts.subjects as arts_sub
import commerce.subjects as commerce_sub

print("--- University Department Subjects ---")

# Import and display subjects from different namespaces
science_list = science_sub.get_science_subjects()
print("\nScience Subjects:")
for subject in science_list:
    print("- ",subject)

arts_list = arts_sub.get_arts_subjects()
print("\nArts Subjects:")
for subject in arts_list:
    print("- ",subject)

commerce_list = commerce_sub.get_commerce_subjects()
print("\nCommerce Subjects:")
for subject in commerce_list:
    print("- ",subject)