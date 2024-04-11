import sqlite3
import pandas as pd

# Load the CSV data into a DataFrame
file_path = 'countries-in-conflict-data new.csv'
df = pd.read_csv(file_path, encoding='ascii')


# Connect to a new SQLite database
conn = sqlite3.connect('conflict_data.db')

# Create a table with the appropriate structure
create_table_query = '''
CREATE TABLE IF NOT EXISTS conflict_data (
    Entity TEXT,
    Code TEXT,
    Year INTEGER,
    Deaths_in_ongoing_conflicts INTEGER
);
'''

# Execute the create table query
conn.execute(create_table_query)

# Insert the data from the DataFrame into the SQLite table
df.to_sql('conflict_data', conn, if_exists='replace', index=False)

# Close the connection to the database
conn.close()
