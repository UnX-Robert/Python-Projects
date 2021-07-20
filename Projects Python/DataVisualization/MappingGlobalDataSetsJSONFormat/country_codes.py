import pygal

def get_country_code(country_name):
    '''Return the Pygal 2-digit country code for the given country'''
    countries = pygal.maps.world.COUNTRIES

    for code, name in countries.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return country_name[:2]

# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))