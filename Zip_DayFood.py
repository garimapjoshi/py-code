days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
foods_of_day = ['Manicotti', 'Tacos', 'Waffles', 'Raspberries', 'Franks', 'Salad', 'Soup']

for (day, food) in zip(days_of_week, foods_of_day):
    print "Today is {0} so obviously I'm having {1} for dinner.".format(day, food)