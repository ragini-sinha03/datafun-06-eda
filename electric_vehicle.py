import pandas as pd
import sqlite3

def create_database():
    # Read the CSV file into a DataFrame with error handling
    try:
        df = pd.read_csv('electric_vehicle.csv')
    except FileNotFoundError:
        print("The file 'electric_vehicle.csv' was not found.")
        return
    except pd.errors.EmptyDataError:
        print("The file 'electric_vehicle.csv' is empty.")
        return
    except pd.errors.ParserError:
        print("The file 'electric_vehicle.csv' could not be parsed.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Connect to SQLite database (or create it if it doesn't exist)
    try:
        conn = sqlite3.connect('electric_vehicle.db')
        cursor = conn.cursor()

        # Create a table named "electric_vehicles" based on the DataFrame structure
        cursor.execute('''CREATE TABLE IF NOT EXISTS electric_vehicles (
                            VIN TEXT PRIMARY KEY,
                            County TEXT,
                            City TEXT,
                            State TEXT,
                            Postal_Code TEXT,
                            Model_Year INTEGER,
                            Make TEXT,
                            Model TEXT,
                            Electric_Vehicle_Type TEXT,
                            Electric_Utility TEXT
                        )''')

        # Insert data from the DataFrame into the SQLite table
        for index, row in df.iterrows():
            cursor.execute('''INSERT INTO electric_vehicles (VIN, County, City, State, Postal_Code, Model_Year, Make, Model, Electric_Vehicle_Type, Electric_Utility)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                           (row['VIN'], row['County'], row['City'], row['State'], row['Postal Code'], row['Model Year'], row['Make'], row['Model'], row['Electric Vehicle Type'], row['Electric Utility']))
            
            conn.commit()
        # Commit changes and close the connection
        
        conn.close()
        print("DONE")
    except sqlite3.Error as e:
        print(f"An error occurred with the SQLite database: {e}")
        return

def main():
    try:
        create_database()
        print("Database created successfully!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
