''' Iteration 5 - with my own variables and statistics

Module: Mo is doing Analytics

Process:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
2. I'll declare a global variable for my byline string and just set it to some simple text.
3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.
4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

I'll test it in an online interpreter to ensure this version runs correctly before continuing.
'''
#import necessary modules in order to be able to use mean and standart Deviation
import statistics

#####################################
#Declare Global Variables
#####################################

#Check whether company has international clients
has_international_clients: bool = True

#Create a variable that shows the number of years of operation
years_in_operation: int = 10

#String list of skills offered by the company
skills_offered: list = ["Data Analysis","Machine Learning", "Business Intelligence"]

#Client Satisfaction Scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#The number of employees in the company
number_of_employees: int = 124

#Ranking among competitors
company_ranking: int = 6

#Does the company offer insurance benefits
has_insurance_benefits: bool = True

#Quarterly Profit Rate in sequence for 2023 (in millions)
profit: list = [34, 28, 56, 43]




#####################################
#Calculating basic statistics using min,max,mean and stdev
#####################################

min_score: float = min(client_satisfaction_scores)
max_score: float = max(client_satisfaction_scores)
mean_score: float = statistics.mean(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)
min_quarterly_profit: int = min(profit)
max_quarterly_profit: int = max(profit)
mean_quarterly_profit: float = statistics.mean(profit)
stdev_quarterly_profit: float = statistics.stdev(profit)

#####################################
# Declare a global variable named byline.
#####################################

byline: str = f"""
-----------------------------
Mo is doing Analytics: the stats that you need...
-----------------------------
Has International Clients:  {has_international_clients}
Years in Operation:  {years_in_operation}
Skills Offered:  {skills_offered}
Client Satisfaction Scores:  {client_satisfaction_scores}
Number of Employees:  {number_of_employees}
Company Ranking:  {company_ranking}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score: {mean_score:.2f}
Standard Deviation of Satisfaction Scores: {stdev_score:.2f}
Maximum of Quarterly Profits: {max_quarterly_profit}
Minimum of Quarterly Profits: {min_quarterly_profit}
Mean of Quarterly profits: {mean_quarterly_profit:.2f}
Standart Deviation of Quarterly Profits: {stdev_quarterly_profit:.2f}
"""

#####################################
#Define the get_byline() function
#####################################

def get_byline() -> str:
    '''Return the byline for my analytics project'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()


