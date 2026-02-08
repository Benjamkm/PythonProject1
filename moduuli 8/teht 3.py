import mysql.connector
from geopy.distance import geodesic


def get_airport_coordinates(icao_code):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='benjamin',
        password='Anojiel1',
        autocommit=True
    )

    sql = f"select latitude_deg, longitude_deg from airport where ident = '{icao_code}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    if tulos:
        return tulos   # (latitude, longitude)
    else:
        return None


def run_airport_distance():
    icao1 = input("Enter the ICAO code of the first airport: ").upper()
    icao2 = input("Enter the ICAO code of the second airport: ").upper()

    koordinaatti_1 = get_airport_coordinates(icao1)
    koordinaatti_2 = get_airport_coordinates(icao2)

    if koordinaatti_1 is None or koordinaatti_2 is None:
        print("One or both ICAO codes were not found.")
        return

    distance_km = geodesic(koordinaatti_1, koordinaatti_2).kilometers
    print(f"Distance between {icao1} and {icao2}: {distance_km:.2f} kilometers")


run_airport_distance()
