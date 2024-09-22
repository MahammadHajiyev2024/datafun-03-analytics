""""
-------------------------------------
Mo is doing Analytics: Creating a Python module with utilities to create different types of project folders
-------------------------------------
"""

"""
----------------------------------------------------------------------
Importing necessary modules from the library and my own modules
----------------------------------------------------------------------
"""
import pathlib
import utils_hajiyev
import time
import os


"""
-----------------------------------------
Declaring Global Variables
-----------------------------------------
"""
#Creating a path object
project_path = pathlib.Path.cwd()

#Creating a project data path object 
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

# Duration of time between folders
duration_secs = 5


"""" 
------------------------------------------------------------------------
Defining function 1 that will create folders from a range
------------------------------------------------------------------------
"""
def create_folders_for_range(start_year: int, end_year: int) -> None:
    start_year = 2020
    end_year = 2023
    for year in range(start_year , end_year+1):
        year_path = project_path.joinpath(str(year))
        year_path.mkdir(exist_ok=True)
        time.sleep(duration_secs)

    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")


"""
---------------------------------------------------------------------
Defining function 2 where we will create folders from a list
---------------------------------------------------------------------
"""
def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:

    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "_")
        os.makedirs(folder_name, exist_ok = True)
        print(f"FUNCTION CALLED: create_folders_from_list with '{folder_name}'")



"""
---------------------------------------------------------------------
Defining function 3 in which we will create a function to create prefixed folders we will create folders from a list
---------------------------------------------------------------------
"""
def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    # TODO: Implement this function professionally and remove the temporary pass
    for folder_name in folder_list:
        prefixed_name = f"{prefix}{folder_name}"
        folder_path = data_path.joinpath(prefixed_name)
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")



"""
---------------------------------------------------------------------
Defining function 4 that will help us write a function to create folders periodically
---------------------------------------------------------------------
"""
def create_folders_periodically(duration_seconds: int) -> None:

    count = 1
    while count <= 5:  
        folder_path = data_path.joinpath(f"periodic_folder_{count}")
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")
        time.sleep(duration_seconds)
        count += 1



"""
---------------------------------------------------------------------
Defining main function to help us show module capabilities
---------------------------------------------------------------------
"""

def main() -> None:

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(f"Byline: {utils_hajiyev.get_byline()}")


    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)


    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)


    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)


    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  
    create_folders_periodically (duration_secs)


    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]

    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")



"""
---------------------------------------------------------------------
Conditional Execution
---------------------------------------------------------------------

"""
if __name__ == '__main__':
    main()
