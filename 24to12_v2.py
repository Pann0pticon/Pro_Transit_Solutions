def convert_to_12_hour_clock(hour, minute):

    if not (0 <= hour < 24 and 0 <= minute < 60):
        return "Invalid input"

    # Determine AM or PM
    period = "AM" if 0 <= hour < 12 else "PM"

    # Convert to 12-hour format
    hour_12 = hour % 12
    hour_12 = 12 if hour_12 == 0 else hour_12

    # Format the result
    result = "{:02d}:{:02d} {}".format(hour_12, minute, period)
    return result

if __name__ == "__main__":
    # Replace these values with the desired 24-hour time
    input_hour = 22
    input_minute = 22

    # Convert and print the result
    result = convert_to_12_hour_clock(input_hour, input_minute)
    print(f"Converted time: {result}")

