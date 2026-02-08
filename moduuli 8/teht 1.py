import mysql.connector

def hae_lentokentta_nimi_sijainti(ICAO):
    sql = f"select name, municipality from airport where ident = '{ICAO}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Airport name: {rivi[0]} \nLocation: {rivi[1]}")
    else:
        print(f"No airport found with ICAO code {ICAO}")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='benjamin',
         password='Anojiel1',
         autocommit=True
         )
ICAO = input("Enter the ICAO code of an airport: ").upper()
hae_lentokentta_nimi_sijainti(ICAO)