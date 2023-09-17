import datetime

def add_time(start_time, hours=0, minutes=0):
    try:
        start_time = datetime.datetime.strptime(start_time, '%H:%M')
        delta = datetime.timedelta(hours=hours, minutes=minutes)
        result_time = start_time + delta
        return result_time.strftime('%I:%M %p')
    except ValueError:
        return "Invalid time format. Please use 'HH:MM' format."

def subtract_time(start_time, hours=0, minutes=0):
    try:
        start_time = datetime.datetime.strptime(start_time, '%H:%M')
        delta = datetime.timedelta(hours=hours, minutes=minutes)
        result_time = start_time - delta
        return result_time.strftime('%I:%M %p')
    except ValueError:
        return "Invalid time format. Please use 'HH:MM' format."

def main():
    print("Time Calculator")
    while True:
        print("1. Add time")
        print("2. Subtract time")
        choice = input("Enter your choice (add/sub): ")

        if choice == 'add':
            start_time = input("Enter the start time (HH:MM): ")
            hours = int(input("Enter the number of hours to add: "))
            minutes = int(input("Enter the number of minutes to add: "))
            new_time = add_time(start_time, hours, minutes)
            print(f"New time: {new_time}")
            break  # Exit the loop if a valid choice is made
        elif choice == 'sub':
            start_time = input("Enter the start time (HH:MM): ")
            hours = int(input("Enter the number of hours to subtract: "))
            minutes = int(input("Enter the number of minutes to subtract: "))
            new_time = subtract_time(start_time, hours, minutes)
            print(f"New time: {new_time}")
            break  # Exit the loop if a valid choice is made
        else:
            print("Invalid choice. Please select add or sub.")

if __name__ == "__main__":
    main()
