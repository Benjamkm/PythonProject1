import mysql.connector

def get_airports_by_country(country_code):
    yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='benjamin',
         password='Anojiel1',
         autocommit=True
         )
    sql = f"select airport.type from airport, country where airport.iso_country = country.iso_country and country.iso_country = '{country_code}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        tyypit = {}
        for rivi in tulos:
            tyyppi = rivi[0]
            tyypit[tyyppi] = tyypit.get(tyyppi, 0) + 1
        jarjestys = ['small_airport', 'medium_airport', 'heliport', 'large_airport']

        print(f"Airports in {country_code}:")
        for tyyppi in jarjestys:
            if tyyppi in tyypit:
                print(f"{tyypit[tyyppi]} {tyyppi} airports")
    else:
        print(f"No airports found for country code {country_code}.")
    return
def run_country_program():
    country_code = input("Enter the country code (e.g., FI for Finland): ").upper()
    get_airports_by_country(country_code)
run_country_program()