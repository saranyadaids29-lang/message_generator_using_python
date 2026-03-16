messages = []

def show_messages():
    if len(messages) == 0:
        print("No messages yet.")
    else:
        print("\nMessages:")
        for i, msg in enumerate(messages, 1):
            print(i, msg)

while True:
    print("\n1. Send Message")
    print("2. View Messages")
    print("3. Delete Message")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        msg = input("Enter your message: ")
        messages.append(msg)
        print("Message sent!")

    elif choice == "2":
        show_messages()

    elif choice == "3":
        show_messages()
        num = int(input("Enter message number to delete: "))
        if 0 < num <= len(messages):
            messages.pop(num-1)
            print("Message deleted!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
