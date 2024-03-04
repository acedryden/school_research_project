import requests
import json

url = "http://127.0.0.1:5000/api/v1.0/amy_test"

# Make a GET request to the Flask API endpoint
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data
    data = json.loads(response.text)

    # Separate data into 'Elementary' and 'Secondary'
    elementary_data = [record for record in zip(*[data[key] for key in data.keys()]) if record[data['School Level']] == 'Elementary']
    secondary_data = [record for record in zip(*[data[key] for key in data.keys()]) if record[data['School Level']] == 'Secondary']

    # Print the results
    print("Elementary Data:")
    for record in elementary_data:
        print(record)

    print("\nSecondary Data:")
    for record in secondary_data:
        print(record)
else:
    # Print an error message if the request was not successful
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")

