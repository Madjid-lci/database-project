import csv
import mysql.connector

# Connect to your MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="madjidlachichi",
    database="movies_database"
)
cursor = conn.cursor()

# Open the CSV file
with open('movies.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    # Skip the header row
    next(csv_reader)
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Extract only the required columns from the row
        name, rating, genre, year, released, score, votes_str, _, _, _, country, budget, gross, _, runtime = row

        # Convert necessary columns to their respective data types
        year = int(year)
        score = float(score)
        votes = int(float(votes_str))  # Convert string to float first, then to integer
        budget = float(budget) if budget else None
        gross = float(gross) if gross else None
        runtime = float(runtime) if runtime else None

        # Insert the row data into the Movies table
        cursor.execute('''INSERT INTO Movies (Name, Rating, Genre, Year, Released, Score, Votes, Country, Budget, Gross, Runtime)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                       (name, rating, genre, year, released, score, votes, country, budget, gross, runtime))

# Commit changes and close connection
conn.commit()
conn.close()

print("Data has been imported successfully.")
