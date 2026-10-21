HELP_TEXT = """Commands:
  hello | help               - show this help
  add [name] [phone]         - add a contact
  change [name] [new phone]  - update a contact's phone
  phone [name]               - show a contact's phone
  all | list                 - show all contacts
  exit | close               - quit"""


def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.strip().lower(), args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Usage: change [name] [new phone]"
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone [name]"
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts):
    if not contacts:
        return "No contacts."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello", "help"]:
            print("How can I help you?")
            print(HELP_TEXT)
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command in ["all", "list"]:
            print(show_all(contacts))
        else:
            print("Unknown command.")
            print(HELP_TEXT)


if __name__ == "__main__":
    main()
