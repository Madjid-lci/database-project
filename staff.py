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
with open('movies.csv', 'r', encoding='utf-8-sig') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    # Skip the header row
    next(csv_reader)
    # Iterate over each row in the CSV file
    for row in csv_reader:
        try:
            # Extract data from the row
            name, rating, genre, year, released_date, released_country, score, votes_str, _, _, country, budget, gross, _, runtime = row

            # Convert necessary columns to their respective data types
            year = int(year)
            score = float(score)
            votes = int(float(votes_str))  # Convert string to float first, then to integer
            budget = float(budget) if budget else None
            gross = float(gross) if gross else None
            runtime = float(runtime) if runtime else None

            # Insert data into the Movies table
            cursor.execute('''INSERT INTO Movies (Name, Rating, Genre, Year, Released_date, Released_country, Score, Votes, Country, Budget, Gross, Runtime)
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                           (name, rating, genre, year, released_date, released_country, score, votes, country, budget, gross, runtime))
            movie_id = cursor.lastrowid  # Get the ID of the last inserted row (movie)

            # Extract director, writer, and star names from the row
            directors = [director.strip() for director in _.split('/') if director.strip()]
            writers = [writer.strip() for writer in _.split('/') if writer.strip()]
            stars = [star.strip() for star in _.split('/') if star.strip()]

            # Insert directors into Directors table and create relationships
            for director in directors:
                cursor.execute("INSERT INTO Directors (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=Name", (director,))
                cursor.execute("INSERT INTO Movie_Crew (Movie_ID, Person_ID, Role) VALUES (%s, LAST_INSERT_ID(), 'Director')", (movie_id,))
            
            # Insert writers into Writers table and create relationships
            for writer in writers:
                cursor.execute("INSERT INTO Writers (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=Name", (writer,))
                cursor.execute("INSERT INTO Movie_Crew (Movie_ID, Person_ID, Role) VALUES (%s, LAST_INSERT_ID(), 'Writer')", (movie_id,))

            # Insert stars into Stars table and create relationships
            for star in stars:
                cursor.execute("INSERT INTO Stars (Name) VALUES (%s) ON DUPLICATE KEY UPDATE Name=Name", (star,))
                cursor.execute("INSERT INTO Movie_Stars (Movie_ID, Star_ID) VALUES (%s, LAST_INSERT_ID())", (movie_id,))
        
        except ValueError as e:
            print(f"Skipped row due to error: {e}")
            continue

# Commit changes and close connection
conn.commit()
conn.close()

print("Data has been imported successfully.")
