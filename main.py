
contacts = {}



def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"

    return wrapper


@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Added {name} with phone {phone}"



@input_error
def change_phone(command):
    _, name, phone = command.split()
    if name in contacts:
        contacts[name] = phone
        return f"Changed phone for {name} to {phone}"
    else:
        return f"Contact {name} not found"



@input_error
def get_phone(command):
    _, name = command.split()
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"Contact {name} not found"



def show_all():
    if contacts:
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "No contacts found"


def exit_bot():
    return "Good bye!"



def main():
    print("How can I help you?")

    while True:
        command = input().strip().lower()

        if command.startswith("add"):
            response = add_contact(command)
        elif command.startswith("change"):
            response = change_phone(command)
        elif command.startswith("phone"):
            response = get_phone(command)
        elif command == "show all":
            response = show_all()
        elif command in ["good bye", "close", "exit"]:
            response = exit_bot()
            print(response)
            break
        elif command == "hello":
            response = "How can I help you?"
        else:
            response = "Invalid command"

        print(response)


if __name__ == "__main__":
    main()

