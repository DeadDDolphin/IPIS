from peewee import *
from connectToDB import *

class Carsharing(BaseModel):
    birth_date = DateField(column_name='BirthDate')
    car_number = CharField(column_name='CarNumber')
    distance_to_car = FloatField(column_name='DistanceToCar', null=True)
    driver_license_number = CharField(column_name='DriverLicenseNumber')
    driving_experience = IntegerField(column_name='DrivingExperience')
    id_client = AutoField(column_name='ID_Client')
    gender = CharField(column_name="Gender")
    name = CharField(column_name='Name')
    order_date = DateField(column_name='OrderDate', null=True)
    phone_number = CharField(column_name='PhoneNumber')
    status = CharField(column_name='Status')
    surname = CharField(column_name='Surname')
    tariff = CharField(column_name='Tariff')
    trip_end_time = DateField(column_name='TripEndTime', null=True)
    trip_start_time = DateField(column_name='TripStartTime', null=True)

    #Функция для добавления ОДНОГО элемента в модель и в базу данных
    #На вход подается словарь вида {"field_name":"field_value"}
    def insertOne(self, data):
        self.create(data)

    #Функция для добавления МНОГИХ элементов в модель и в базу данных
    #На вход подается словарь вида {"field_name":"field_value"}
    def insertMany(self, data):
        with database.atomic():
            for every_row in data:
                self.create(**every_row)

    #Заготовка под редактирование. Это еще необходимо
    #обкашлять, что именно будем редачить и т.д.
    def update(self, data):
        query = self.update().where
    class Meta:
        table_name = 'carsharing'
