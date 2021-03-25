from models import *



if __name__ == '__main__':
    try:
        db.connect()
        Carsharing.create_table()
    except:
        print("Error")

