# Standard library imports
import csv
import json
import pathlib 


from collections import Counter, defaultdict


import requests  
import pandas as pd
# Local module imports
import MahammadHajiyev_projsetup
import utils_hajiyev

#####################################
# Declare Global Variables
#####################################

# Name the folder where you will store your fetched data files
fetched_folder_name = "fetched"

#####################################
# Define Functions to Fetch and Write Excel Data
#####################################

def fetch_excel_file(folder_name:str, filename:str, url:str) -> None:
    """Fetch Excel data from the given URL and write it to a file."""
    print(f"FUNCTION CALLED: fetch_excel_file with folder_name={folder_name}, filename={filename}, url={url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  
        write_excel_file(folder_name, filename, response.content)
        print(f"SUCCESS: Excel file fetched and saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Excel data: {e}")

def write_excel_file(folder_name:str, filename:str, binary_data:bytes) -> None:
    """Write Excel binary_data to a file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: write_excel_file with file_path={file_path}")
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('wb') as file:
            file.write(binary_data)
        print(f"SUCCESS: Excel data saved to {file_path}")
    except IOError as e:
        print(f"Error writing Excel data to {file_path}: {e}")

#####################################
# Define Functions to Fetch and Write JSON Data 
#####################################

def fetch_json_file(folder_name:str, filename:str, url:str) -> None:
    """Fetch JSON data from the given URL and write it to a file."""
    print(f"FUNCTION CALLED: fetch_json_file with folder_name={folder_name}, filename={filename}, url={url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  
        write_json_file(folder_name, filename, response.json())
        print(f"SUCCESS: JSON file fetched and saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching JSON data: {e}")

def write_json_file(folder_name:str, filename:str, data) -> None:
    """Write JSON data to a file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: write_json_file with file_path={file_path}")
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            json.dump(json_data, file, indent=4)
        print(f"SUCCESS: JSON data saved to {file_path}")
    except IOError as e:
        print(f"Error writing JSON data to {file_path}: {e}")

#####################################
# Define Functions to Fetch and Write Text Data
#####################################

def fetch_txt_file(folder_name:str, filename:str, url:str) -> None:
     try: 
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
     except requests.RequestException as e:
        print(f"Failed to fetch text data: {e}")

def write_txt_file(folder_name:str, filename:str, data) -> None:
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('w', encoding = 'utf-8') as file:
            file.write(data)
        print(f"Text data saved to {file_path}")
    except IOError as e:
        print(f"Error writing text file {file_path}: {e}")
   
  


#####################################
# Define Functions to Fetch and Write CSV Data
#####################################

def fetch_csv_file(folder_name:str, filename:str, url:str) -> None:
    try: 
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.text)
    except requests.RequestException as e:
        print(f"Failed to fetch CSV data: {e}")


def write_csv_file(folder_name:str, filename:str, data) -> None:
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('w', encoding = 'utf-8') as file:
            file.write(data)
        print(f"CSV data saved to {file_path}")
    except IOError as e:
        print(f"Error writing CSV file {file_path}: {e}")


########################################
# Define process functions
########################################

def process_txt_file(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        with file_path.open('r', encoding = 'utf-8') as file:
            text = file.read()
    except IOError as e:
        print(f"Error reading text file {file_path}: {e}")

    try:
        # Basic processing
        words = text.lower().split()
        unique_words = set(words)
        word_count = len(words)
        unique_word_count = len(unique_words)

        # Save the results
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding = 'utf-8') as file:
            file.write(f"Total words: {word_count}\n")
            file.write(f"Unique words: {unique_word_count}\n")
        print(f"Text data processed and results saved to {output_path}")
    except Exception as e: 
        print(f"Error processing text data: {e}")

def process_csv_file(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        row_count = 0
        column_summaries = []
        data = []

        with file_path.open('r', encoding = 'utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            column_summaries = ['Column summary:'] + headers

            # Count rows
            for row in reader:
                row_count += 1 
                data.append(tuple(row))

        # Summarize columns
        column_counts = [0] * len(headers)
        for row in data:
            for i, value in enumerate(row):
                if value:
                    column_counts[i] += 1
        
        # Save the results
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding = 'utf-8') as file:
            file.write(f"Total rows: {row_count}\n")
            file.write(f"\nColumn summaries:\n")
            for header, count in zip(headers, column_counts):
                file.write(f"{header}: {count} entries\n")
        print(f"CSV data processed and results saved to {output_path}")
    except IOError as e:
        print(f"Error reading or writing CSV file: {e}")
    except csv.Error as e:
        print(f"Error processing CSV data: {e}")

def process_excel_file(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        df = pd.read_excel(file_path)
        summary = {
            'Total rows': len(df),
            'Total columns': len(df.columns),
            'Column names': list(df.columns),
            'Numeric column statistics': df.describe().to_string()
        }

        # Save the results
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding = 'utf-8') as file:
            file.write(f"Summary of excel data:\n")
            for key, value in summary.items():
                if isinstance(value, str):
                    file.write(f"{key}:\n{value}\n\n")
                else:
                    file.write(f"{key}: {value}\n")
        print(f"Excel data processed and results saved to {output_path}")
    except IOError as e:
        print(f"Error reading Excel file {file_path}: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Excel file is empty or not readable: {file_path}")
    except pd.errors.ExcelFileError as e:
        print(f"Error reading Excel file {file_path}: {e}")

def process_json_file(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        with file_path.open('r', encoding = 'utf-8') as file:
            json_data = json.load(file)

        # Summarize the data
        summary = {'Number of items': len(json_data)}

        if isinstance(json_data, list) and len(json_data) > 0 and isinstance(json_data[0], dict):
            summary['Keys in JSON objects'] = list(json_data[0].keys())
        
        # Save the results
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding = 'utf-8') as file:
            file.write(f"Summary of JSON data:\n")
            for key, value in summary.items():
                if isinstance(value, str):
                    file.write(f"{key}:\n{value}\n\n")
                else:
                    file.write(f"{key}: {value}\n")
        print(f"JSON data processed and results saved to {output_path}")
    except IOError as e:
        print(f"Error reading JSON file {file_path}: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data: {e}")

#####################################
# Define main() function for this module.
#####################################

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # URL definitions
    txt_url = 'https://github.com/denisecase/datafun-03-spec/raw/main/data.txt'
    csv_url = 'https://github.com/denisecase/datafun-03-spec/raw/main/data.csv'
    excel_url = 'https://github.com/denisecase/datafun-03-spec/raw/main/data.xls'
    json_url = 'https://github.com/denisecase/datafun-03-spec/raw/main/data.json'

    # Reuse get_byline() from imported module
    print(f"Byline: {utils_hajiyev.get_byline()}")

    # Reuse  create_folders_from_list() from imported module to make a folder for fetched files
    # We set the name as a global variable so the whole module can use it. 
    # Make sure we provide a LIST when using our function
    MahammadHajiyev_projsetup.create_folders_from_list([fetched_folder_name])

    # Web locations of different types of data to fetch
    # TODO: Optional find different urls for 4 different types of data                               
    excel_url:str = 'https://raw.githubusercontent.com/denisecase/datafun-03-analytics/main/hosted/Feedback.xlsx' 
    json_url:str = 'https://github.com/denisecase/datafun-03-spec/blob/main/data.json'
    txt_url:str = 'https://raw.githubusercontent.com/denisecase/datafun-03-analytics/main/hosted/romeo.txt'
    csv_url:str = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel'
    json_folder_name = 'data-json'

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls'
    json_filename = 'data.json'


    pathlib.Path(txt_folder_name).mkdir(exist_ok=True)
    pathlib.Path(csv_folder_name).mkdir(exist_ok=True)
    pathlib.Path(json_folder_name).mkdir(exist_ok=True)
    pathlib.Path(excel_folder_name).mkdir(exist_ok=True)

    # Fetch data files - provide the fetched file names
    fetch_excel_file(fetched_folder_name, "feedback.xlsx", excel_url)
    fetch_json_file(fetched_folder_name, "astros.json", json_url)
    fetch_txt_file(fetched_folder_name, "romeo.txt", txt_url)
    fetch_csv_file(fetched_folder_name, "2020_happiness.csv", csv_url)
    

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')


    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

