from pymeos.db import MobilityDB
from pymeos import Temporal, pymeos_initialize, pymeos_finalize
import pandas as pd

host = 'pymeos-demo-db'
port = 5432
db = 'demo'
user = 'docker'
password = 'docker'

pymeos_initialize()

connection = MobilityDB.connect(host=host, port=port, database=db, user=user, password=password)
cursor = connection.cursor()

trips = pd.read_csv('./trips.csv', converters={'trip': Temporal.from_hexwkb})

for trip in trips.iterrows():
    t = trip[1]
    cursor.execute(f"INSERT INTO Trips(vehicle, day, seq, trip) "
                   f"VALUES ({t['vehicle']}, '{t['day']}', '{t['seq']}', '{t['trip']}');")

connection.commit()
cursor.close()
pymeos_finalize()