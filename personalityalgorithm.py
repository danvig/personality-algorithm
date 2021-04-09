import sqlite3
import time

# Function to connect to database and print test data
def database_test():
    conn = None
    try:
        conn = sqlite3.connect("people.db")
        print("Database connection successful!")
    except Error as e:
        print("Database connection refused... ",str(e))

    time.sleep(10)

    # Test data
    results = conn.execute("SELECT fullname FROM people")
    print("\n> analysis subject.match[parameters]-dateRange.locationRange:")

    time.sleep(5)

    for row in results:
        print("# " + str(row))
        time.sleep(5)
    
    print("\nLIST COMPLETE!")

    # Disconnect from database
    try:
        conn.close()
        print("\nDatabase connection closed!")
    except Error as e:
        print("\nError closing connection to database... ",str(e))

# CALL FUNCTIONS
database_test()