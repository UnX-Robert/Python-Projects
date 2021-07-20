import pygal

countries =  pygal.maps.world.COUNTRIES

for country_code in sorted(countries.keys()):
    print(country_code, countries[country_code])