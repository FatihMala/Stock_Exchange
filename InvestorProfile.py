import os

PROFILE_DIR = "YOUR OWN FILE PATH"  # Update your own file path

# If the folder does not exist, create it
os.makedirs(PROFILE_DIR, exist_ok=True)

def manage_profile():
    while True:
        print("1. Add Profile")
        print("2. View Profile")
        print("3. Update Profile")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_profile()
        elif choice == "2":
            view_profile()
        elif choice == "3":
            update_profile()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def get_profile_file(portfolio_number):
    return os.path.join(PROFILE_DIR, f"{portfolio_number}.txt")

def add_profile():
    try:
        name = input("Enter Name: ").strip()
        surname = input("Enter Surname: ").strip()
        user_id = input("Enter ID: ").strip()
        portfolio_number = input("Enter Portfolio Number: ").strip()
        
        profile_file = get_profile_file(portfolio_number)
        with open(profile_file, "w", encoding="utf-8") as file:
            file.write(f"{name},{surname},{user_id},{portfolio_number}\n")
            print(f"Profile for portfolio {portfolio_number} added successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def view_profile():
    portfolio_number = input("Enter Portfolio Number to view: ").strip()
    profile_file = get_profile_file(portfolio_number)
    
    try:
        if not os.path.exists(profile_file):
            print("No profile found for this portfolio number.")
            return
        
        with open(profile_file, "r", encoding="utf-8") as file:
            profile = file.readline().strip()
            if profile:
                details = profile.split(",")
                print(f"Name: {details[0]}")
                print(f"Surname: {details[1]}")
                print(f"ID: {details[2]}")
                print(f"Portfolio Number: {details[3]}")
            else:
                print("No profile found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def update_profile():
    portfolio_number = input("Enter Portfolio Number to update: ").strip()
    profile_file = get_profile_file(portfolio_number)
    
    if not os.path.exists(profile_file):
        print("No profile found for this portfolio number.")
        return
    
    try:
        name = input("Enter New Name: ").strip()
        surname = input("Enter New Surname: ").strip()
        user_id = input("Enter New ID: ").strip()
        new_portfolio_number = input("Enter New Portfolio Number: ").strip()
        
        new_profile_file = get_profile_file(new_portfolio_number)
        with open(new_profile_file, "w", encoding="utf-8") as file:
            file.write(f"{name},{surname},{user_id},{new_portfolio_number}\n")
            print(f"Profile for portfolio {portfolio_number} updated successfully.")
        
        if new_portfolio_number != portfolio_number:
            os.remove(profile_file)  # Delete old file
    except Exception as e:
        print(f"Error updating file: {e}")

if __name__ == "__main__":
    manage_profile()
