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

# Replace NaN values in the 'star' column with an appropriate placeholder
usefulData['star'] = usefulData['star'].fillna(value='Unknown')

# Extract unique stars
stars = usefulData['star'].unique()

# Iterate over stars and insert them into the Stars table
for idx, star in enumerate(stars):
    star_id = f"st{idx+1}"  # Generate star ID in the format stX
    cursor.execute('''INSERT INTO Stars (Star_ID, Name) 
                      VALUES (%s, %s)''', (star_id, star))

# Commit changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
