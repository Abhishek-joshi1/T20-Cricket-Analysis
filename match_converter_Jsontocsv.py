import json
import csv

def json_to_csv(json_file, csv_file):
    # Read JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Extract match summary data
    match_summary = data[0]['matchSummary']
    
    # Define CSV fieldnames
    fieldnames = ['team1', 'team2', 'winner', 'margin', 'ground', 'matchDate', 'scorecard']
    
    # Write to CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header
        writer.writeheader()
        
        # Write data
        for match in match_summary:
            writer.writerow(match)

# Example usage
json_file = 'JSON FILES/t20_wc_match_results.json'
csv_file = 't20_wc_matche_results.csv'
json_to_csv(json_file, csv_file)