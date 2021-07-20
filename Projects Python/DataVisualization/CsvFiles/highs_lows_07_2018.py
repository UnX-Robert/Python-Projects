import csv

from datetime import datetime
from matplotlib import pyplot as plt

# Get dates and high temperatures from file.
filename = 'DataVisualization\CsvFiles\data\sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='green', alpha=0.5)
ax.plot(dates, lows, c='red', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title('Daily high and low temperature, July 2018', fontsize=16)
plt.xlabel('', fontsize=8)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=8)
plt.tick_params(axis='both', which='major', labelsize=8)

plt.show()
