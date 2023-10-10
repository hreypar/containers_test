#!/usr/bin/env python

import requests
import json

# input and output file paths
api_endpoint = snakemake.params.api_endpoint
output_file = snakemake.output[0]

# Function to fetch data from the API
def fetch_data(api_endpoint, output_file_path):
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        data = response.json()
        with open(output_file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"Data fetched and saved as {output_file_path}.")
    else:
        print("Failed to fetch data from the API.")
        sys.exit(1)

# call the function to fetch and save data
fetch_data(api_endpoint, output_file)

