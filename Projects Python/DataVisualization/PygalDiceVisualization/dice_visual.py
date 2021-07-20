import pygal

from dice import Dice

# Create two dice
dice_1 = Dice()
dice_2 = Dice(10)
r = 10000

max_result = dice_1.num_sides + dice_2.num_sides

def roll(rolls):
    '''Make some rolls, and return results in a list'''
    results = []
    for roll_num in range(rolls):
        result = dice_1.roll() + dice_2.roll()
        results.append(result)
    return results

def frequency():
    '''Analyze the results, and return frequencies in a list'''
    frequencies = []
    results = roll(r)

    for value in range(2, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)
    return frequencies

def get_hist_title(num_sides1, num_sides2, rolls):
    '''Get the title for the histogram, and return a string'''
    if num_sides1 == num_sides2:
        title = 'Results of rolling two D{} {} times'.format(num_sides1, rolls)
    else:
        title = 'Results of rolling a D{} and a D{} {} times'.format(num_sides1, num_sides2, rolls)
    return title

frequencies = frequency()

# Visualize the results
hist = pygal.Bar()

hist.title = get_hist_title(dice_1.num_sides, dice_2.num_sides, r)
hist.x_labels = [i for i in range(2, max_result + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D{} + D{}'.format(dice_1.num_sides, dice_2.num_sides), frequencies)
hist.render_to_file('dice_visual.svg')


