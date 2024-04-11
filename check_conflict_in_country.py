"""This code reads the csv file that contains
a summary of the number of deaths between 1989 and 2022.
Creates a new csv file for the selected country
and a line chart for deaths in the country over the years"""

from time import sleep
import pandas as pd
import matplotlib.pyplot as plt


conflict_data = pd.read_csv('countries-in-conflict-data new.csv', encoding='ascii')

country_to_check = input('Enter name of the country: ')
# Filter the data for the conutry
country_data = conflict_data[conflict_data['Entity'] == f'{country_to_check}']

# Save the filtered data to a new CSV file
country_data.to_csv(f'{country_to_check}_conflict_data.csv', index=False)

sleep(10)
# Load the country conflict data from the CSV file
country_data = pd.read_csv(f'{country_to_check}_conflict_data.csv')

# Update the column name for deaths to match the DataFrame
country_data.rename(columns={'Deaths in ongoing conflicts in a country (best estimate)'
                             ' - Conflict type: all': 'Deaths'}, inplace=True)

# Create a line plot for the deaths in the country over the years
plt.figure(figsize=(10, 5), facecolor='white')
plt.plot(country_data['Year'], country_data['Deaths'], marker='o', linestyle='-', color='red')
plt.title(f'Deaths in Ongoing Conflicts in {country_to_check} (1989-2022)')
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.grid(True)
plt.savefig(f'{country_to_check}_conflict_trend.png')
plt.show()
