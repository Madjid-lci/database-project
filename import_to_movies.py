import pandas as pd
import mysql.connector
import numpy as np  # Import numpy library for handling NaN values

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

# Replace NaN values with appropriate placeholders
usefulData = usefulData.replace({np.nan: None})

# Iterate over the rows of the DataFrame and insert data into the Movies table
for index, row in usefulData.iterrows():
    cursor.execute('''INSERT INTO Movies (Name, Rating, Genre, Year, Released, Score, Votes, Country, Budget, Gross, Runtime) 
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                      (row['name'], row['rating'], row['genre'], row['year'], row['released'], 
                       row['score'], row['votes'], row['country'], row['budget'], 
                       row['gross'], row['runtime']))

# Commit changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
