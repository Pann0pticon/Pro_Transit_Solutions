from datetime import timedelta

def add_time(time_str1, time_str2):
    time1 = timedelta(hours=int(time_str1.split(':')[0]), minutes=int(time_str1.split(':')[1]))
    time2 = timedelta(hours=int(time_str2.split(':')[0]), minutes=int(time_str2.split(':')[1]))
    result = time1 + time2
    return str(result)

def subtract_time(time_str1, time_str2):
    time1 = timedelta(hours=int(time_str1.split(':')[0]), minutes=int(time_str1.split(':')[1]))
    time2 = timedelta(hours=int(time_str2.split(':')[0]), minutes=int(time_str2.split(':')[1]))
    result = time1 - time2
    return str(result)

def multiply_time(time_str, factor):
    time1 = timedelta(hours=int(time_str.split(':')[0]), minutes=int(time_str.split(':')[1]))
    result = time1 * factor
    return str(result)

def divide_time(time_str, divisor):
    time1 = timedelta(hours=int(time_str.split(':')[0]), minutes=int(time_str.split(':')[1]))
    result = time1 / divisor
    return str(result)

while True:
    print("Time Calculator Menu:")
    print("1. Add Time")
    print("2. Subtract Time")
    print("3. Multiply Time")
    print("4. Divide Time")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        break

    time_str1 = input("Enter the first time (HH:MM): ")
    if choice != '3' and choice != '4':
        time_str2 = input("Enter the second time (HH:MM): ")

    if choice == '1':
        result = add_time(time_str1, time_str2)
        print("Result:", result)
    elif choice == '2':
        result = subtract_time(time_str1, time_str2)
        print("Result:", result)
    elif choice == '3':
        factor = float(input("Enter the multiplication factor: "))
        result = multiply_time(time_str1, factor)
        print("Result:", result)
    elif choice == '4':
        divisor = float(input("Enter the division divisor: "))
        result = divide_time(time_str1, divisor)
        print("Result:", result)
    else:
        print("Invalid choice. Please select a valid option.")
