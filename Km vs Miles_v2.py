def miles_to_km(miles):
    # Conversion factor: 1 mile is approximately 1.60934 kilometers
    km = miles * 1.60934
    return round(km, 2)

def km_to_miles(km):
    # Conversion factor: 1 kilometer is approximately 0.621371 miles
    miles = km * 0.621371
    return round(miles, 2)

# Main function to interact with the user
def main():
    print("Welcome to the distance converter!")
    print("1. Miles to Kilometers")
    print("2. Kilometers to Miles")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        miles = float(input("Enter distance in miles: "))
        result = miles_to_km(miles)
        print(f"{miles} miles is equal to {result} kilometers.")
    elif choice == 2:
        km = float(input("Enter distance in kilometers: "))
        result = km_to_miles(km)
        print(f"{km} kilometers is equal to {result} miles.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
