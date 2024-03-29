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

# Extract unique directors
directors = usefulData['director'].unique()

# Iterate over directors and insert them into the Directors table
for idx, director in enumerate(directors):
    director_id = f"dr{idx+1}"  # Generate director ID in the format drX
    cursor.execute('''INSERT INTO Directors (Director_ID, Name) 
                      VALUES (%s, %s)''', (director_id, director))

# Commit changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
