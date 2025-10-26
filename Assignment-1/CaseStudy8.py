book_ids = list(range(101, 111))
print("Generated Book IDs:", book_ids)

print("\n--- Vowel Check in Book Title ---")

book_title = "Python Programming"
vowels = "aeiouAEIOU"
contains_vowel = False

for ch in book_title:
    if ch in vowels:
        contains_vowel = True
        break

if contains_vowel:
    print("The book title ",book_title," contains vowels.")
else:
    print("The book title ",book_title," does NOT contain vowels.")

print("\n--- List of Available Books ---")

books = ["Python Programming", "Data Structures", "Cloud", "SEPM"]
for book in books:
    print(book)

print("\n--- Book-Author Pairs ---")

book_authors = {
    "Python Programming": "Prof. Leena Deshmukh",
    "Data Structures": "Prof. Rajesh Jadav",
    "Cloud": "Prof. Nikita Phalak",
    "SEPM": "Prof Darshana Surwase"
}

for book, author in book_authors.items():
    print(book," is written by ",author)
