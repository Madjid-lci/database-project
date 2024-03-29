import mysql.connector

def create_database():
    # Connect to MySQL
    connection = mysql.connector.connect(
        user='root',
        password='madjidlachichi',
        host='localhost'
    )

    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS movies_database")

    # Switch to the created database
    cursor.execute("USE movies_database")

    # Create Movies table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (
                        Movie_ID INT AUTO_INCREMENT PRIMARY KEY,
                        Name VARCHAR(255),
                        Rating VARCHAR(50),
                        Genre VARCHAR(50),
                        Year INTEGER,
                        Released VARCHAR(255),
                        Score FLOAT,
                        Votes INTEGER,
                        Country VARCHAR(50),
                        Budget VARCHAR(20),
                        Gross VARCHAR(20),
                        Runtime VARCHAR(20)
                    )''')

    # Create Directors table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Directors (
                        Director_ID VARCHAR(255)  PRIMARY KEY,
                        Name VARCHAR(255)
                    )''')

    # Create Writers table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Writers (
                        Writer_ID VARCHAR(255) PRIMARY KEY,
                        Name VARCHAR(255)
                    )''')

    # Create Stars table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Stars (
                        Star_ID VARCHAR(255) PRIMARY KEY,
                        Name VARCHAR(255)
                    )''')

    # Create Companies table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS Companies (
                        Company_ID VARCHAR(255) PRIMARY KEY,
                        Name VARCHAR(255)
                    )''')

    # Create Movie_Crew table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Movie_Crew (
                    Movie_ID INT,
                    Person_ID VARCHAR(255),
                    Role VARCHAR(250),
                    FOREIGN KEY(Movie_ID) REFERENCES Movies(Movie_ID)
                        ON UPDATE CASCADE ON DELETE CASCADE,
                    FOREIGN KEY(Person_ID) REFERENCES Directors(Director_ID)
                        ON UPDATE CASCADE ON DELETE CASCADE,
                    PRIMARY KEY (Movie_ID, Person_ID, Role)
                )''')


    # Create Movie_Stars table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Movie_Stars (
                        Movie_ID INT,
                        Star_ID VARCHAR(255),
                        FOREIGN KEY(Movie_ID) REFERENCES Movies(Movie_ID)
                            ON UPDATE CASCADE ON DELETE CASCADE,
                        FOREIGN KEY(Star_ID) REFERENCES Stars(Star_ID)
                            ON UPDATE CASCADE ON DELETE CASCADE,
                        PRIMARY KEY (Movie_ID, Star_ID)
                    )''')

    # Create Movie_Companies table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Movie_Companies (
                        Movie_ID INT,
                        Company_ID VARCHAR(255),
                        FOREIGN KEY(Movie_ID) REFERENCES Movies(Movie_ID)
                            ON UPDATE CASCADE ON DELETE CASCADE,
                        FOREIGN KEY(Company_ID) REFERENCES Companies(Company_ID)
                            ON UPDATE CASCADE ON DELETE CASCADE,
                        PRIMARY KEY (Movie_ID, Company_ID)
                    )''')

    # Commit changes and close connection
    connection.commit()
    connection.close()

    print("Database and tables created successfully!")

if __name__ == "__main__":
    create_database()
