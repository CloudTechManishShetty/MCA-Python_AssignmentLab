import library.books
import library.members

def simulate_library_operations():
    print("\n--- Welcome to the Library System ---")
    
    library.books.add_book("Python Crash Course", "Eric Matthes")
    library.books.add_book("The Lord of the Rings", "J.R.R. Tolkien")
    library.members.register_member("System Admin")
    print("\n(System initialized with a few books and one member.)")
    print("-" * 40)

    while True:
        print("\n--- Main Menu ---")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Register a New Member")
        print("4. Update Member Status (e.g., Suspended)")
        print("5. Display All Books and Members")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            title = input("Enter the book title: ").strip()
            author = input("Enter the author's name: ").strip()
            if title and author:
                library.books.add_book(title, author)
            else:
                print("Title and Author cannot be empty.")
            
        elif choice == '2':
            search_term = input("Enter title/keyword to search: ").strip()
            library.books.search_book(search_term)

        elif choice == '3':
            name = input("Enter the new member's name: ").strip()
            if name:
                library.members.register_member(name)
            else:
                print("Member name cannot be empty.")

        elif choice == '4':
            if not library.members.member_list:
                print("No members registered yet.")
                continue

            print("\nCurrent Members:")
            for mid, details in library.members.member_list.items():
                 print("  ID: ",mid," - Name: ",details['name']," (Status: ",details['status'],")")
            
            try:
                member_id = int(input("Enter the Member ID to update: ").strip())
                new_status = input("Enter the new status (e.g., Active, Suspended, Lost): ").strip()
                library.members.update_member_status(member_id, new_status)
            except ValueError:
                print("Invalid input. Please enter a valid number for the Member ID.")
            
        elif choice == '5':
            print("\n" + "=" * 40)
            print("--- Current Library Status ---")
            
            print("\nAll current books:")
            if library.books.book_list:
                for b in library.books.book_list:
                    print("  Title: ",b['title']," | Author: ",b['author']," | Status: ",b['status'])
            else:
                print("  (No books in the library.)")

            print("\nAll current members:")
            if library.members.member_list:
                for mid, details in library.members.member_list.items():
                    print("  ID: ",mid," | Name: ",details['name']," | Status: ",details['status'])
            else:
                print("  (No members registered.)")
            print("=" * 40)
            
        elif choice == '6':
            print("\nThank you for using the Library Management System. Goodbye! 👋")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            
simulate_library_operations()