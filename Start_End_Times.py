import pandas as pd


def search_transit_schedule(schedule_file, start_station, finish_station):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(schedule_file)

    # Initialize lists to store times
    start_times = []
    finish_times = []
    other_times = []

    # Iterate through the DataFrame
    for index, row in df.iterrows():
        station = row['Station']
        time = row['Time']

        if station == start_station:
            start_times.append(time)
        elif station == finish_station:
            finish_times.append(time)
        else:
            other_times.append((station, time))

    return start_times, finish_times, other_times


if __name__ == "__main__":
    excel_file = "transit_schedule.xlsx"  # Update with your Excel file path
    start_station = "Start Station"  # Update with the name of your start station
    finish_station = "Finish Station"  # Update with the name of your finish station

    start_times, finish_times, other_times = search_transit_schedule(excel_file, start_station, finish_station)

    print(f"Start Times: {start_times}")
    print(f"Finish Times: {finish_times}")
    print(f"Other Times: {other_times}")

#Make sure to update excel_file, start_station, and finish_station with your actual Excel file path and station names.
#This script reads the Excel file, iterates through its rows, and categorizes the times based on the start and finish stations.
#It also stores other times in a list along with their corresponding stations.
#Remember to format your Excel spreadsheet with appropriate columns for 'Station' and 'Time'.
#The script assumes these column names, so adjust them as needed for your spreadsheet.

