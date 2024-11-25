import mysql.connector

def create_database():
    """Create the database if it doesn't exist and return the connection and cursor."""
    db_connection = mysql.connector.connect(
        host="localhost",  # Change to your MySQL host
        user="root",       # Your MySQL username
        password="urlakalangu",  # Your MySQL password
    )
    cursor = db_connection.cursor()

    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS TechnoTest1")

    # Use the created database
    cursor.execute("USE TechnoTest1")

    return db_connection, cursor

def create_tables(cursor):
    """Create tables in the database."""
    # Create the admin table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            Sno INT PRIMARY KEY AUTO_INCREMENT,
            Name VARCHAR(50),
            Username VARCHAR(50),
            Password VARCHAR(50)
        )
    """)

    # Create the cart table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cart (
            Sno INT,
            Brand VARCHAR(255),
            Model VARCHAR(255),
            Price INT
        )
    """)

    # Create the devices table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            Sno INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50)
        )
    """)

    # Create the adapter table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS adapter (
            Sno INT PRIMARY KEY AUTO_INCREMENT,
            Brand VARCHAR(50),
            Model VARCHAR(100),
            OutputPower VARCHAR(50),
            PortModel VARCHAR(50),
            Price INT
        )
    """)

    # Create the monitor table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS monitor (
            Sno INT PRIMARY KEY AUTO_INCREMENT,
            Brand VARCHAR(50),
            Model VARCHAR(100),
            Price INT
        )
    """)

    # Create the keyboard table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS keyboard (
            Sno INT PRIMARY KEY AUTO_INCREMENT,
            Brand VARCHAR(50),
            Model VARCHAR(100),
            Price INT
        )
    """)

    # Create the mouse table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mouse (
            Sno INT PRIMARY KEY AUTO_INCREMENT,
            Brand VARCHAR(50),
            Model VARCHAR(100),
            Price INT
        )
    """)

    # Create the headphone table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS headphone (
            Sno INT PRIMARY KEY AUTO_INCREMENT,
            Brand VARCHAR(50),
            Model VARCHAR(100),
            Price INT
        )
    """)

    cursor.connection.commit()

def insert_sample_data(cursor):
    """Insert sample data into the tables."""
    # Insert sample data into the admin table
    cursor.executemany("""
        INSERT INTO admin (Name, Username, Password)
        VALUES (%s, %s, %s)
    """, [
        ('Shaariq', 'MuhammadShaariq', 'urlakalangu'),
        ('Keerthi', 'Truly', 'BlackCape'),
        ('Mani Kandan', 'ex1', 'ps1')
    ])

    # Insert categories into the devices table
    cursor.executemany("""
        INSERT INTO devices (name)
        VALUES (%s)
    """, [
        ('Adapter'),
        ('Monitor'),
        ('Keyboard'),
        ('Mouse'),
        ('Headphone')
    ])

    # Insert sample data into the adapter table
    cursor.executemany("""
        INSERT INTO adapter (Brand, Model, OutputPower, PortModel, Price)
        VALUES (%s, %s, %s, %s, %s)
    """, [
        ('Lenovo', 'U1000EA', '19W', 'USB Slim Tip', 1341),
        ('Dell', 'AC Adapter', '90W', 'Round', 2499),
        ('Dell', 'GaN Slim', '130W', 'USB-C', 11498),
        ('Lenovo', 'AC Adapter', '65W', 'USB Slim Port', 1021),
        ('Lenovo', 'AC Round Tip Adapter', '45W', 'Round Tip', 1041),
        ('HP', 'LC Power Adapter', '65W', 'USB-C', 2207),
        ('Acer', 'AC Power Adapter', '65W', 'USB-C', 2299),
        ('Acer', 'Small Pin Power Adapter', '65W', 'Small Pin', 1378)
    ])

    # Insert sample data into the monitor table
    cursor.executemany("""
        INSERT INTO monitor (Brand, Model, Price)
        VALUES (%s, %s, %s)
    """, [
        ('Asus', 'ProArt Display PA278CFRV 100Hz QHD IPS', 31878),
        ('HP', 'Z Display Z22i 21.5-inch IPS LED Backlit Monitor', 14093),
        ('Acer', 'KA222Q E0 54.6 cm (21.5") Full HD IPS Panel', 5599),
        ('Dell', '27 Monitor - S2721HN', 12499),
        ('Zebronics', 'MT52-ZEB A19HD 46.9 cm (18.5 inch)', 5599),
        ('Samsung', 'LS24C366EAWXXL 24-inch Full HD VA Panel', 7499)
    ])

    # Insert sample data into the keyboard table
    cursor.executemany("""
        INSERT INTO keyboard (Brand, Model, Price)
        VALUES (%s, %s, %s)
    """, [
        ('Zebronics', 'ZEBRONICS TRANSFORMER PRO Gaming Wireless Keyboard', 1800),
        ('Hp', 'HP 230 Wireless Black Keyboard', 1250),
        ('Lenovo', 'Lenovo 510 Wireless Keyboard', 1700),
        ('Asus', 'ASUS Membrane USB Gaming Keyboard for PC - TUF K1', 3400),
        ('Dell', 'Dell-KB700, Multi-Device Wireless Keyboard', 5260)
    ])

    # Insert sample data into the mouse table
    cursor.executemany("""
        INSERT INTO mouse (Brand, Model, Price)
        VALUES (%s, %s, %s)
    """, [
        ('Logitech', 'Logitech G304 Lightspeed Wireless Gaming Mouse', 2995),
        ('Zebronics', 'ZEBRONICS-Transformer-M High-Performance USB Mouse', 400),
        ('HP', 'HP M260 RGB Backlighting USB Wired Gaming Mouse', 472),
        ('Dell', 'Dell WM118 Wireless Mouse', 580)
    ])

    # Insert sample data into the headphone table
    cursor.executemany("""
        INSERT INTO headphone (Brand, Model, Price)
        VALUES (%s, %s, %s)
    """, [
        ('Boat', 'boAt Rockerz 450 Bluetooth On Ear Headphones with Mic', 1700),
        ('Zebronics', 'ZEBRONICS DUKE Wireless Headphone', 1400),
        ('Sony', 'Sony WH-CH520, Wireless On-Ear Bluetooth Headphones', 4500),
        ('Logitech', 'Logitech G733 Lightspeed Wireless Gaming Headset', 14900)
    ])

    cursor.connection.commit()

def setup_database():
    """Setup the database, create tables, and insert sample data."""
    db_connection, cursor = create_database()
    create_tables(cursor)
    insert_sample_data(cursor)

    # Close the connection after setting up the database
    cursor.close()
    db_connection.close()

    print("Database setup complete.")
