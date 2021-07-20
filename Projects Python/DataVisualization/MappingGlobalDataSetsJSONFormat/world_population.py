import json

import pygal
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from country_codes import get_country_code

# Load the data into a list
filename = 'DataVisualization\MappingGlobalDataSetsJSONFormat\data\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

def print_population(year):
    '''
    Print the population in a specific
    year for each country(1960-2010)
    '''
    for pop_dict in pop_data:
        if pop_dict['Year'] == str(year):
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code: 
                print('{}: {}'.format(code, population))
            else:
                print('Error: {}'.format(country_name))

def world_population():
    '''Build a dictionary of population data 2010'''
    cc_populations = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
                country_name = pop_dict['Country Name']
                population = int(float(pop_dict['Value']))
                code = get_country_code(country_name)
                if code:
                    cc_populations[code] = population
    return cc_populations

cc_populations = world_population()

# Group the countries into 3 population levels
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# See how many countries are in each level
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')