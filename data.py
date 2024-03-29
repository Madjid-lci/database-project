import csv
import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="madjidlachichi"  # Replace 'your_password' with your actual MySQL password
)

# Create a new database
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS new_movies_database")
cursor.execute("USE new_movies_database")

# Create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (
                        Name VARCHAR(255) PRIMARY KEY,
                        Rating VARCHAR(50),
                        Genre VARCHAR(50),
                        Year INTEGER,
                        Released VARCHAR(50),
                        Score FLOAT,
                        Votes INTEGER,
                        Director VARCHAR(255),
                        Writer VARCHAR(255),
                        Star VARCHAR(255),
                        Country VARCHAR(50),
                        Budget FLOAT,
                        Gross FLOAT,
                        Company VARCHAR(255),
                        Runtime VARCHAR(20)
                    )''')

# Open the CSV file
with open('movies.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    # Skip the header row
    next(csv_reader)
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Convert appropriate columns to their respective data types
        row[3] = int(row[3])  # Year
        row[5] = float(row[5])  # Score
        row[6] = int(float(row[6]))  # Votes (converted to int)
        row[11] = float(row[11]) if row[11] else None  # Budget (handle empty values)
        row[12] = float(row[12]) if row[12] else None  # Gross (handle empty values)

        # Replace empty strings with None
        row = [None if x == '' else x for x in row]

        # Insert the row data into the Movies table
        cursor.execute('''INSERT INTO Movies (Name, Rating, Genre, Year, Released, Score, Votes,
                          Director, Writer, Star, Country, Budget, Gross, Company, Runtime)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', row)

# Commit changes and close connection
conn.commit()
conn.close()

print("Data has been imported successfully.")
