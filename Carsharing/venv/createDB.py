import sqlite3

con = sqlite3.connect(
    "/home/dolph/Документы/GitHub/IPIS/Carsharing/Carsharing.db"
)
cur = con.cursor()
sql = """
    CREATE TABLE IF NOT EXISTS carsharing
    (
        ID_Client INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Surname TEXT,
        Gender TEXT,
        BirthDate DATE,
        DriverLicenseNumber TEXT,
        DrivingExperience INTEGER,
        PhoneNumber TEXT,
        Status TEXT,
        Tariff TEXT,
        TripEndTime DATE,
        TripStartTime DATE,
        DistanceToCar FLOAT,
        OrderDate DATE
    );"""
cur.executescript(sql)
