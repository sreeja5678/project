import json

def get_user_input():
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the category (e.g., food, transportation, entertainment): ")
    return amount, description, category

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_categories(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []


def add_category_if_not_exists(categories, category):
    if category not in categories:
        categories.append(category)
        save_categories(categories)

def save_categories(categories, filename=None):
    if filename is None:
        filename = 'categories.json'
    with open(filename, 'w') as f:
        json.dump(categories, f)

def analyze_data(data):
    monthly_summary = {}
    category_summary = {}

    for entry in data:
        amount, description = entry
        month = description.split()[0]
        category = description.split('(')[-1][:-1]  # Extract category from description

        if month not in monthly_summary:
            monthly_summary[month] = 0
        monthly_summary[month] += amount

        if category not in category_summary:
            category_summary[category] = 0
        category_summary[category] += amount

    return monthly_summary, category_summary


def display_menu():
    print("\nExpense Tracker Menu")
    print("1. Add expense")
    print("2. View monthly summary")
    print("3. View category summary")
    print("4. Exit")

def main():
    data = load_data('data.json')
    categories = load_categories('categories.json')

    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount, description, category = get_user_input()
            add_category_if_not_exists(categories, category)
            data.append([amount, f"{description} ({category})"])
            save_data('data.json', data)
        elif choice == 2:
            monthly_summary, _ = analyze_data(data)
            for month, total in monthly_summary.items():
                print(f"{month}: {total:.2f}")
        elif choice == 3:
            _, category_summary = analyze_data(data)
            for category, total in category_summary.items():
                print(f"{category}: {total:.2f}")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
