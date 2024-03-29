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

# Replace NaN values in the 'writer' column with an appropriate placeholder
usefulData['writer'] = usefulData['writer'].fillna(value='Unknown')

# Extract unique writers
writers = usefulData['writer'].unique()

# Iterate over writers and insert them into the Writers table
for idx, writer in enumerate(writers):
    writer_id = f"wr{idx+1}"  # Generate writer ID in the format wrX
    cursor.execute('''INSERT INTO Writers (Writer_ID, Name) 
                      VALUES (%s, %s)''', (writer_id, writer))

# Commit changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()