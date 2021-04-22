from models import *

if __name__ == '__main__':

    data = (
        'Sania Kovalenko',
        'Male',
        '+79184958482',
        '11.11.2000',
        "23213213",
        '1',
        'No',
        '10 rub',
        '15',
        '09.03.2021',
        '10.03.2021',
        '23'
    )

    tmp = Carsharing()
    print(tmp.add_record(data))
    res = tmp.get_all_tuples()
    #tmp.delete_by_id(7)
    tmp.change_record(data,8)
    print(res)
