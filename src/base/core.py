import os
import glob
import json
import csv
from datetime import datetime, timedelta

def buildMacroToCSV(data, name="output", inGCal = True, fmTracking = False):

    # Parse the start date
    start_date = datetime.strptime(data["startDate"], "%m/%d/%y")

    # Initialize variables
    current_weight = data["startingWeight"]
    current_bf = data['startingBF']
    current_date = start_date

    # Parse cycle prefix numbering scheme
    cycle_number_prefix = data["cycleNumberPrefix"]
    cycle_number = 1

    # Macrocycle week counter
    macro_week = 1

    # Create a list to store the CSV rows
    csv_rows = []

    # Iterate through each mesocycle
    for cycle in data["mesocycles"]:
        cycle_name = cycle["name"]
        weeks = cycle["weeks"]
        deload_weeks = cycle["deload"]
        rate = cycle["rate"]

        # Iterate through each week in the mesocycle
        for week in range(1, weeks + 1):
            # Check if the current week is a deload week
            if week in deload_weeks:
                week_number = f"{week}D"
            else:
                week_number = str(week)
            
            # Check if there is a manual weight for the current week
            manual_weight_entry = next((entry for entry in data["manualWeights"] if entry["week"] == macro_week), None)
            if manual_weight_entry:
                current_weight = manual_weight_entry["weight"]
                
                # Adds bf to the current week if greater than 0
                if fmTracking == True and manual_weight_entry['bf'] >0:
                    current_bf = manual_weight_entry["bf"]

            # Check if cycle week needs it's name printed in notes
            if week != 1:
                cycle_name = ""


            # Creates microcycle row
            microcycle_row = [cycle_number_prefix+str(cycle_number),week_number, str(rate)+'%', round(current_weight, 2), cycle_name, macro_week]

            # Creates the weekly calendar for the said week based on timedelta
            if inGCal == True:
                microcycle_row.append(current_date.strftime("%b"))
                for day in range(0,7):
                    microcycle_row.append((current_date + timedelta(days=day)).strftime("%-d"))


            # Append the row to the CSV rows list
            csv_rows.append(microcycle_row)

            
            # Update the weight for the next week if it's not a deload week
            if week not in deload_weeks:
                current_weight += current_weight * (rate/100)
            
            # Update the date for the next week
            current_date += timedelta(weeks=1)

            # Update the week number
            macro_week += 1

        # Update cycle count
        cycle_number +=1

    macrocycle_headerrow = ["Cycle", "Cycle Week", "Gain (%)", "Weight Predictions", "Notes", "Week"]
    if inGCal == True:
        macrocycle_headerrow.extend(['Month','Mon','Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'])


    # Write the CSV rows to a file
    with open(name+".csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(macrocycle_headerrow)
        writer.writerows(csv_rows)

    
    print(f"CSV file '{name}.csv' has been created successfully.")

def main():#
    print("Test complete")

def listMacros():
    """
    Scan all files in cwd and find any applicable "xxx.mesocal.json" files
    FIXME: allow to insert file paths
    Open each file and load the names of each
    """
    # Get the current working directory
    cwd = os.getcwd()
    print(cwd)

    # Use glob to find all files with ".mesocal.json" in their name
    files = glob.glob(os.path.join(cwd, '*mesocal.json'))

    # Print the list of files
    x = 1
    for file in files:
        print(str(x)+". "+str(file))
        x+=1

    try:
        selection = int(input('Please select option: '))
    except:
        print('Invalid Option')

    return files[selection-1]
    

def viewMacro():
    print('Sorry, this is WIP')


def buildMacro():
    # Build Macrocycle

    print("\n\nOptions:")
    print("1. Build from JSON file")
    print("2. Build manually (WIP/Not Built)")

    try:
        command = int(input("Please type an option: "))
        if command == 1:
            macroSample = listMacros()
            print(macroSample)
            file = open(macroSample)
            jsonData = json.load(file)
            file.close()
            json_name = macroSample.split('/')[-1].replace('.mesocal.json', '')
            file_name = input(f'Enter file name [default: {json_name}]: ') or json_name

            buildMacroToCSV(jsonData, file_name)
    except:
        raise Exception("Error has occured")

def editMacro():
    print('Sorry, this is WIP')

def delMacro():
    print('Sorry, this is WIP')


def menu():
    # Main menu screen
    while True:
        print("\n\nWelcome to MesoCal!")
        print("1. View Macrocycle")
        print("2. Build Macrocycle")
        print("3. Edit Macrocycle")
        print("4. Delete Macrocycle")
        print("0. Exit")
        
        try:
            command = int(input("Please type an option: "))

            if command == 1:
                viewMacro()
            elif command == 2:
                buildMacro()
            elif command == 3:
                editMacro()
            elif command == 4:
                delMacro()
            elif command == 0:
                break
            else:
                raise Exception("Not an option")
        except:
            print("Please select valid option")
        
        



menu()
