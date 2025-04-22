from users import register_user, login_user
from medicines import add_medicine, view_medicines, delete_medicine

def user_menu(username):
    while True:
        print("\n--- Medicine Tracker Menu ---")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Delete Medicine")
        print("4. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Medicine name: ")
            dosage = input("Dosage (e.g. 500mg): ")
            frequency = input("Frequency (e.g. twice daily): ")
            notes = input("Notes (optional): ")
            add_medicine(username, name, dosage, frequency, notes)
            print("✅ Medicine added.")

        elif choice == "2":
            view_medicines(username)

        elif choice == "3":
            view_medicines(username)
            try:
                index = int(input("Enter number of medicine to delete: ")) - 1
                success, msg = delete_medicine(username, index)
                print(msg)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Logging out.")
            break
        else:
            print("Invalid choice.")

def main():
    print("🔐 Welcome to Smart MedVault!")
    choice = input("Do you want to [register] or [login]? ").strip().lower()

    username = input("Username: ")
    password = input("Password: ")

    if choice == "register":
        success, message = register_user(username, password)
    elif choice == "login":
        success, message = login_user(username, password)
    else:
        success, message = False, "Invalid choice."

    print(message)
    if success and choice == "login":
        user_menu(username)

if __name__ == "__main__":
    main()
