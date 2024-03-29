import pandas as pd
import mysql.connector

# Connect to your MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="madjidlachichi",
    database="movies_database"
)

# Create a cursor object
cursor = conn.cursor()

# Read data from CSV
usefulData = pd.read_csv("movies.csv")

# Replace NaN values in the 'company' column with an appropriate placeholder
usefulData['company'] = usefulData['company'].fillna(value='Unknown')

# Extract unique companies
companies = usefulData['company'].unique()

# Iterate over companies and insert them into the Companies table
for idx, company in enumerate(companies):
    company_id = f"cp{idx+1}"  # Generate company ID in the format cpX
    cursor.execute('''INSERT INTO Companies (Company_ID, Name) 
                      VALUES (%s, %s)''', (company_id, company))

# Commit changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
