import json
import csv

def json_to_csv():
    # Take input JSON file path from user
    json_file = input("Enter the path of the JSON file: ")

    # Read JSON file
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: JSON file not found.")
        return
    
    # Extract column names from the first item in the list
    columns = list(data[0].keys())

    # Take input from user for columns to include in CSV file
    print("Available columns in the JSON file:", ', '.join(columns))
    columns_input = input("Enter column names separated by comma (e.g., name,team,playingRole): ")
    selected_columns = [col.strip() for col in columns_input.split(',')]

    # Take output CSV file name from user
    csv_file = input("Enter the name for the output CSV file: ")

    # Write to CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=selected_columns)
        
        # Write header
        writer.writeheader()
        
        # Write data
        for item in data:
            item_data = {col: item[col] for col in selected_columns if col in item}
            writer.writerow(item_data)

# Call the function
json_to_csv()
