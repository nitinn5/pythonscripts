
######################### Dictionaries, ex.1 ################################################

names_by_rank = dict()
for rank, name in female_baby_names_2012.items():
    names_by_rank[rank] = name
    
# Sort the names_by_rank dict by rank in descending order and slice the first 10 items
for listitem in sorted(names_by_rank,reverse=True)[:10]:
    print(names_by_rank[listitem])

    
######################### Dictionaries, ex.2 ################################################
    
"""
if you attempt to access a key that isn't present in a dictionary, you'll get a KeyError. One option to handle this type of error is to use a try: except: block. Python provides a faster, more versatile tool to help with this problem in the form of the .get() method. The .get() method allows you to supply the name of a key, and optionally, what you'd like to have returned if the key is not found.
You'll be using same names dictionary from the previous exercise and will gain practice using the .get() method.
""" 

# Safely print rank 7 from the names dictionary
print(names.get(7,'Not found'))

# Safely print the type of rank 100 from the names dictionary
print(type(names.get(100)))

# Safely print rank 105 from the names dictionary or 'Not Found'
print(names.get(105,'Not Found'))

######################### Dictionaries, ex.3 ################################################

"""
Dealing with nested data: .keys() method returns dict_keys. I then use dict_keys as index to extract nested dictionaries. I use get method to safely return values from a nested dictionary.
"""

# Print a list of keys from the boy_names dictionary
print(boy_names.keys())

# Print a list of keys from the boy_names dictionary for the year 2013
print(boy_names[2013].keys())

# Loop over the dictionary
for year in boy_names:
    # Safely print the year and the third ranked name or 'Unknown'
    print(year, boy_names[year].get(3, 'Unknown'))

######################### Dictionaries, ex.4 ################################################

"""
Adding and updating dictionaries: add is very simple. Create a new key, and assign a value for that key. update() is used when the value is itself a dictionary/list. pass the dictionary or the list to be added as a parameter in the update() method. 
"""
# Assign the names_2011 dictionary as the value to the 2011 key of boy_names
boy_names[2011]= names_2011

# Update the 2012 key in the boy_names dictionary
boy_names[2012].update([(1,'Casey'),(2, 'Aiden')])

# Loop over the years in the boy_names dictionary 
for year in boy_names:
    # Sort the data for each year by descending rank and get the lowest one
    lowest_ranked =  sorted(boy_names[year], reverse=True)[0]
    # Safely print the year and the least popular name or 'Not Available'
    print(year, boy_names[year].get(lowest_ranked,'Not Available'))

######################### Dictionaries, ex.5 ################################################

"""
Popping and deleting from dictionaries: Often, you will want to remove keys and value from a dictionary. You can do so using the del Python instruction. It's important to remember that del will throw a KeyError if the key you are trying to delete does not exist. You can not use it with the .get() method to safely delete items; however, it can be used with try: catch:.

If you want to save that deleted data into another variable for further processing, the .pop() dictionary method will do just that. You can supply a default value for .pop() much like you did for .get() to safely deal with missing keys. It's also typical to use .pop() instead of del since it is a safe method.
"""

# Remove 2011 from female_names and store it: female_names_2011
female_names_2011 = female_names.pop(2011)

# Safely remove 2015 from female_names with an empty dictionary as the default: female_names_2015
female_names_2015 = female_names.pop(2015,{})

# Delete 2012 from female_names
del female_names[2012]

# Print female_names
print(female_names)


######################### Dictionaries, ex.6 ################################################

"""
Working with dictionaries more pythonically
So far, you've worked a lot with the keys of a dictionary to access data, but in Python, the preferred manner for iterating over items in a dictionary is with the .items() method.

This returns each key and value from the dictionary as a tuple, which you can unpack in a for loop. You'll now get practice doing this.
"""
# Iterate over the 2014 nested dictionary
for rank, name in baby_names[2014].items():
    # Print rank and name
    print(rank, name)
    
# Iterate over the 2012 nested dictionary
for rank, name in baby_names[2012].items():
    # Print rank and name
    print(rank, name)

######################### Dictionaries, ex.7 ################################################

"""
Checking dictionaries for data
You can check to see if a key exists in a dictionary by using the in expression.

For example, you can check to see if 'cookies' is a key in the dictionary by using if 'cookies' in recipes_dict: this allows you to safely react to data being present in the dictionary.

You can also use the in expression so see if data is in the value of a dictionary such as if 'cookies' in recipes_dict.values(). Remember you have to handle nested dictionaries differently as illustrated in the video and previous exercises, and use the in expression on each nested dictionary.
"""
# Check to see if 2011 is in baby_names
if 2011 in baby_names:
    print('Found 2011')
    
# Check to see if rank 1 is in 2012
if 1 in baby_names[2012]:
    print('Found Rank 1 in 2012')
else:
    # Print 'Rank 1 missing from 2012' if not found
    print('Rank 1 missing from 2012')
    
# Check to see if Rank 5 is in 2013
if 5 in baby_names[2013]:
   print('Found Rank 5')

######################### Dictionaries, ex.8 ################################################

"""
Reading from a file using CSV reader
Python provides a wonderful module called csv to work with CSV files. You can pass the .reader() method of csv a Python file object and use it as you would any other iterable. To create a Python file object, you use the open() function, which accepts a file name and a mode. The mode is typically 'r' for read or 'w' for write.
"""

# Import the python CSV module
import csv

# Create a python file object in read mode for the baby_names.csv file: csvfile
csvfile = open('baby_names.csv', 'r')

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):
    # Print each row 
    print(row)
    # Add the rank and name to the dictionary
    baby_names[row[5]]= row[3]

# Print the dictionary keys
print(baby_names.keys())

######################### Dictionaries, ex.8 ################################################

"""
Creating a dictionary from a file
The csv module also provides a way to directly create a dictionary from a CSV file with the DictReader class. If the file has a header row, that row will automatically be used as the keys for the dictionary. However, if not, you can supply a list of keys to be used. Each row from the file is returned as a dictionary. Using DictReader can make it much easier to read your code and understand what data is being used, especially when compared to the numbered indexes you used in the prior exercise.
"""
# Import the python CSV module
import csv

# Create a python file object in read mode for the `baby_names.csv` file: csvfile
csvfile = open('baby_names.csv','r')

# Loop over a DictReader on the file
for row in csv.DictReader(csvfile):
    # Print each row 
    print(row)
    # Add the rank and name to the dictionary: baby_names
    baby_names[row['RANK']] = row['NAME']

# Print the dictionary keys
print(baby_names.keys())

######################### Dictionaries, ex.9 ################################################


"""
Using Counter on lists
Counter is a powerful tool for counting, validating, and learning more about the elements within a dataset that is found in the collections module. You pass an iterable (list, set, tuple) or a dictionary to the Counter. You can also use the Counter object similarly to a dictionary with key/value assignment, for example counter[key] = value.
"""
# Import the Counter object
from collections import Counter

# Print the first ten items from the stations list
print(stations[:10])

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Print the station_count
print(station_count)

######################### Dictionaries, ex.10 ################################################
"""
Finding most common elements
Another powerful usage of Counter is finding the most common elements in a list. This can be done with the .most_common() method.
"""
# Import the Counter object
from collections import Counter

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Find the 5 most common elements
print(station_count.most_common(5))


######################### Dictionaries, ex.10 ################################################

"""
Creating dictionaries of an unknown structure
Occasionally, you'll need a structure to hold nested data, and you may not be certain that the keys will all actually exist. This can be an issue if you're trying to append items to a list for that key. You might remember the NYC data that we explored in the video. In order to solve the problem with a regular dictionary, you'll need to test that the key exists in the dictionary, and if not, add it with an empty list.
"""
# Create an empty dictionary: ridership
ridership = {}

# Iterate over the entries
for date, stop, riders in entries:
    # Check to see if date is already in the ridership dictionary
    if date not in ridership:
        # Create an empty list for any missing date
        ridership[date] = []
    # Append the stop and riders as a tuple to the date keys list
    ridership[date].append((stop,riders))
    
# Print the ridership for '03/09/2016'
print(ridership['03/09/2016'])

######################### Dictionaries, ex.11 ################################################

"""
Safely appending to a key's value list
Often when working with dictionaries, you will need to initialize a data type before you can use it. A prime example of this is a list, which has to be initialized on each key before you can append to that list.

A defaultdict allows you to define what each uninitialized key will contain. When establishing a defaultdict, you pass it the type you want it to be, such as a list, tuple, set, int, string, dictionary or any other valid type object.
"""
# Import defaultdict
from collections import defaultdict

# Create a defaultdict with a default type of list: ridership
ridership = defaultdict(list)

# Iterate over the entries
for date, stop, riders in entries:
    # Use the stop as the key of ridership and append the riders to its value
    ridership[stop].append(riders)
    
# Print the first 10 items of the ridership dictionary
print(list(ridership.items())[:10])


######################### Dictionaries, ex.12 ################################################

"""
Working with OrderedDictionaries
Recently in Python 3.6, dictionaries were made to maintain the order in which the keys were inserted; however, in all versions prior to that you need to use an OrderedDict to maintain insertion order.

Let's create a dictionary of all the stop times by route and rider, then use it to find the ridership throughout the day.
"""

# Import OrderedDict from collections
from collections import OrderedDict

# Create an OrderedDict called: ridership_date
ridership_date = OrderedDict()

# Iterate over the entries
for date, riders in entries:
    # If a key does not exist in ridership_date, set it to 0
    if  date not in ridership_date:
        ridership_date[date] = 0
        
    # Add riders to the date key in ridership_date
    ridership_date[date] += riders
    
# Print the first 31 records
print(list(ridership_date.items())[:31])


######################### Dictionaries, ex.13 ################################################

"""
Powerful Ordered popping
Where OrderedDicts really shine is when you need to access the data in the dictionary in the order you added it. OrderedDict has a .popitem() method that will return items in reverse of which they were inserted. You can also pass .popitem() the last=False keyword argument and go through the items in the order of how they were added.

Here, you'll use the ridership_date OrderedDict you created in the previous exercise.
"""

# Print the first key in ridership_date
print(list(ridership_date.keys())[0])

# Pop the first item from ridership_date and print it
print(ridership_date.popitem(last=False))

# Print the last key in ridership_date
print(list(ridership_date.keys())[-1])

# Pop the last item from ridership_date and print it
print(ridership_date.popitem())


######################### Dictionaries, ex.14 ################################################

"""
Creating namedtuples for storing data
Often times when working with data, you will use a dictionary just so you can use key names to make reading the code and accessing the data easier to understand. Python has another container called a namedtuple that is a tuple, but has names for each position of the tuple. You create one by passing a name for the tuple type and a list of field names.
"""

# Import namedtuple from collections
from collections import namedtuple

# Create the namedtuple: DateDetails
DateDetails = namedtuple('DateDetails', ['date', 'stop', 'riders'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the entries list
for date, stop, riders in entries:
    # Append a new DateDetails namedtuple instance for each entry to labeled_entries
    details = DateDetails(date, stop, riders)
    labeled_entries.append(details) 
    
# Print the first 5 items in labeled_entries
print(labeled_entries[:5])

######################### Dictionaries, ex.15 ################################################

"""
Leveraging attributes on namedtuples
Once you have a namedtuple, you can write more expressive code that is easier to understand. Remember, you can access the elements in the tuple by their name as an attribute. 
"""

# Iterate over the first twenty items in labeled_entries
for item in labeled_entries[:20]:
    # Print each item's stop
    print(item.stop)

    # Print each item's date
    print(item.date)

    # Print each item's riders
    print(item.riders)

######################### Dictionaries, ex.16 ################################################

"""
Strings to DateTimes
Time to begin your DateTime journey! You'll start by using the .strptime() method from the datetime object as shown in the video, passing it both the string and the format. Strings to DateTimes
Time to begin your DateTime journey! You'll start by using the .strptime() method from the datetime object as shown in the video, passing it both the string and the format. 
visit link: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
"""

# Import the datetime object from datetime
from datetime import datetime

# Iterate over the dates_list 
for date_str in dates_list:
    # Convert each date to a datetime object: date_dt
    date_dt = datetime.strptime(date_str,'%m/%d/%Y')
    
    # Print each date_dt
    print(date_dt)

######################### Dictionaries, ex.17 ################################################

"""
Converting to a String
Converting from a datetime object to a string is done with the .strftime() method on a instance of the datetime object. You pass a format string just like the ones used in the prior exercise.

There is also a widely used string output standard called ISO-8601. It has a shortcut method named .isoformat(). I encourage you to use it anytime you write out to a file.
"""

# Loop over the first 10 items of the datetimes_list
for item in datetimes_list[:10]:
    # Print out the record as a string in the format of 'MM/DD/YYYY'
    print(item.strftime('%m/%d/%Y'))

    # Print out the record as an ISO standard string
    print(item.isoformat())

######################### Dictionaries, ex.18 ################################################

"""
Converting to a String
Converting from a datetime object to a string is done with the .strftime() method on a instance of the datetime object. You pass a format string just like the ones used in the prior exercise.

There is also a widely used string output standard called ISO-8601. It has a shortcut method named .isoformat(). I encourage you to use it anytime you write out to a file.
"""
# Loop over the first 10 items of the datetimes_list
for item in datetimes_list[:10]:
    # Print out the record as a string in the format of 'MM/DD/YYYY'
    print(item.strftime('%m/%d/%Y'))

    # Print out the record as an ISO standard string
    print(item.isoformat())
    

######################### Dictionaries, ex.19 ################################################

"""
Pieces of Time
When working with datetime objects, you'll often want to group them by some component of the datetime such as the month, year, day, etc. Each of these are available as attributes on an instance of a datetime object.

You're going to work with the summary of the CTA's daily ridership. It contains the following columns, in order: service_date, day_type, bus, rail_boardings, and total_rides. The modules defaultdict and datetime have already been imported for you.
"""
# Create a defaultdict of an integer: monthly_total_rides
monthly_total_rides = defaultdict(int)

# Loop over the list daily_summaries
for daily_summary in daily_summaries:
    # Convert the service_date to a datetime object
    service_datetime = datetime.strptime(daily_summary[0],'%m/%d/%Y')

    # Add the total rides to the current amount for the month
    monthly_total_rides[service_datetime.month] += int(daily_summary[4]) # Be careful! month is not a method but attribute for the datetime instance. Don't use ()
    
# Print monthly_total_rides
print(monthly_total_rides)


######################### Dictionaries, ex.20 ################################################

"""
Creating DateTime Objects... Now
Often when working with datetime objects, you'll want to work on windows or ranges that start from the current date and time. You can do this using the datetime now functions. There is a .now() method on the datetime object in the datetime module and a .utcnow() method. The .now() method returns the current local time on the machine on which it is run, and .utcnow() does the same thing but returns the value in UTC time. You'll need to be very familiar with these methods.Creating DateTime Objects... Now
Often when working with datetime objects, you'll want to work on windows or ranges that start from the current date and time. You can do this using the datetime now functions. There is a .now() method on the datetime object in the datetime module and a .utcnow() method. The .now() method returns the current local time on the machine on which it is run, and .utcnow() does the same thing but returns the value in UTC time. You'll need to be very familiar with these methods.
"""
# Import datetime from the datetime module
from datetime import datetime

# Compute the local datetime: local_dt
local_dt = datetime.now()

# Print the local datetime
print(local_dt)

# Compute the UTC datetime: utc_dt
utc_dt = datetime.utcnow()

# Print the UTC datetime
print(utc_dt)

######################### Dictionaries, ex.21 ################################################

"""
Timezones
In order to work effectively with other timezones, you can use the pytz library. To use timezones, you need to import the timezone object from the pytz module. Then you can use the timezone constructor and pass it a name of a timezone, such as CT = timezone('US/Central'). You can get a full list of timezone names at Wikipedia. In Python 3, you can make a datetime object "aware" by passing a timezone as the tzinfo keyword argument to the .replace() method on a datetime instance.

An "aware" datetime object has an .astimezone() method that accepts a timezone object and returns a new datetime object in the desired timezone. If the tzinfo is not set for the datetime object it assumes the timezone of the computer you are working on.
"""
# Create a Timezone object for Chicago
chicago_usa_tz = timezone('US/Central')

# Create a Timezone object for New York
ny_usa_tz = timezone('US/Eastern')

# Iterate over the daily_summaries list
for orig_dt, ridership in daily_summaries:

    # Make the orig_dt timezone "aware" for Chicago
    chicago_dt = orig_dt.replace(tzinfo=chicago_usa_tz)
    
    # Convert chicago_dt to the New York Timezone
    ny_dt = chicago_dt.astimezone(ny_usa_tz)
    
    # Print the chicago_dt, ny_dt, and ridership
    print('Chicago: %s, NY: %s, Ridership: %s' % (chicago_dt, ny_dt, ridership))

######################### Dictionaries, ex.22 ################################################

"""
inding a time in the future and from the past
Another common case when working with times is to get a date 30, 60, or 90 days in the past from some date. In Python, the timedelta object from the datetime module is used to represent differences in datetime objects. You can create a timedelta by passing any number of keyword arguments such as days, seconds, microseconds, milliseconds, minutes, hours, and weeks to timedelta().

Once you have a timedelta object, you can add or subtract it from a datetime object to get a datetime object relative to the original datetime object.
"""
# Import timedelta from the datetime module
from datetime import timedelta

# Build a timedelta of 30 days: glanceback
glanceback = timedelta(days=30)

# Iterate over the review_dates as date
for date in review_dates:
    # Calculate the date 30 days back: prior_period_dt
    prior_period_dt = date - glanceback
    
    # Print the review_date, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
         (date,
          daily_summaries[date]['day_type'],
          daily_summaries[date]['total_ridership']))

    # Print the prior_period_dt, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
          (prior_period_dt, 
          daily_summaries[prior_period_dt]['day_type'], 
          daily_summaries[prior_period_dt]['total_ridership']))

######################### Dictionaries, ex.22 ################################################

"""
Finding differences in DateTimes
Just like you were able to subtract a timedelta from a datetime to find a date in the past, you can also calculate the difference between two dates to get the timedelta between in return. Here, you'll find out how much time has elapsed between two transit dates.
"""

# Iterate over the date_ranges
for start_date, end_date in date_ranges:
    # Print the End and Start Date
    print(end_date, start_date)
    # Print the difference between each end and start date
    print(end_date - start_date)


######################### Dictionaries, ex.23 ################################################

"""
Localizing time with pendulum
Here, you're going to use pendulum to practice doing some common datetime operations!
"""
# Import the pendulum module
import pendulum
# Create a now datetime for Tokyo: tokyo_dt

tokyo_dt = pendulum.now( tz = 'Asia/Tokyo')

# Covert the tokyo_dt to Los Angeles: la_dt
la_dt = tokyo_dt.in_timezone(tz = 'America/Los_Angeles')

# Print the ISO 8601 string of la_dt
print(la_dt.to_iso8601_string())


######################### Dictionaries, ex.24 ################################################

"""
Humanizing Differences with Pendulum
Pendulum provides a powerful way to convert strings to pendulum datetime objects via the .parse() method. Just pass it a date string and it will attempt to convert into a valid pendulum datetime. By default, .parse() can process dates in ISO 8601 format. To allow it to parse other date formats, pass strict = False.

It also has a wonderful alternative to timedelta. When calculating the difference between two dates by subtraction, pendulum provides methods such as .in_days() to output the difference in a chosen metric. These are just the beginning of what pendulum can do for you.

visit link: https://pendulum.eustace.io/docs/ 
"""

# Iterate over date_ranges
for start_date, end_date in date_ranges:

    # Convert the start_date string to a pendulum date: start_dt 
    start_dt = pendulum.parse(start_date, strict = False)
    
    # Convert the end_date string to a pendulum date: end_dt 
    end_dt = pendulum.parse(end_date, strict = False)
    
    # Print the End and Start Date
    print(end_dt, start_dt)
    
    # Calculate the difference between end_dt and start_dt: diff_period
    diff_period = end_dt - start_dt
    
    # Print the difference in days
    print(diff_period.in_days())

######################### Data Types for Data Science in Python: Project on Chicago Crime Data ################################################

######################### Task 1 ################################################
#Your job in this exercise is to use a CSV Reader to load up a list to hold the data you're going to analyze.

# Import the csv module
import csv

# Create the file object: csvfile
csvfile = open('crime_sampler.csv','r')

# Create an empty list: crime_data
crime_data = []

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):

    # Append the date, type of crime, location description, and arrest
    crime_data.append((row[0], row[2], row[4], row[5]))
    
# Remove the first element from crime_data
crime_data.pop(0)

# Print the first 10 records
print(crime_data[:10])

######################### Task 2 ################################################
# Find the Months with the Highest Number of Crimes
# Using the crime_data list from the prior exercise, you'll answer a common question that arises when dealing with crime data: How many crimes are committed each month?

# Import necessary modules
from collections import Counter
from datetime import datetime


# Create a Counter Object: crimes_by_month
crimes_by_month = Counter()

# Loop over the crime_data list
for item in crime_data:
    
    # Convert the first element of each item into a Python Datetime Object: date
    date = datetime.strptime(item[0], '%m/%d/%Y %I:%M:%S %p')
    
    # Increment the counter for the month of the row by one
    crimes_by_month[date.month] += 1
    
# Print the 3 most common months for crime
print(crimes_by_month.most_common(3))

######################### Task 3 ################################################
"""
Transforming your Data Containers to Month and Location
Now let's flip your crime_data list into a dictionary keyed by month with a list of location values for each month, and filter down to the records for the year 2016. Remember you can use the shell to look at the crime_data list, such as crime_data[1][4] to see the location of the crime in the second item of the list (since lists start at 0).
"""
# Import necessary modules
from collections import defaultdict
from datetime import datetime

# Create a dictionary that defaults to a list: locations_by_month
locations_by_month = defaultdict(list)

# Loop over the crime_data list
for row in crime_data:
    # Convert the first element to a date object
    date = datetime.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')
    
    # If the year is 2016 
    if date.year == 2016:
        # Set the dictionary key to the month and append the location (fifth element) to the values list
        locations_by_month[date.month].append(row[4])
    
# Print the dictionary
print(locations_by_month)

######################### Task 4 ################################################
"""
Find the Most Common Crimes by Location Type by Month in 2016
Using the locations_by_month dictionary from the prior exercise, you'll now determine common crimes by month and location type. Because your dataset is so large, it's a good idea to use Counter to look at an aspect of it in an easier to manageable size and learn more about it.
"""
# Import Counter from collections
from collections import Counter

# Loop over the items from locations_by_month using tuple expansion of the month and locations
for month, locations in locations_by_month.items():
    # Make a Counter of the locations
    location_count = Counter(locations)
    # Print the month 
    print(month)
    # Print the most common location
    print(location_count.most_common(5))

######################### Task 5 ################################################
"""
Reading your Data with DictReader and Establishing your Data Containers
Your data file, crime_sampler.csv contains in positional order: the date, block where it occurred, primary type of the crime, description of the crime, description of the location, if an arrest was made, was it a domestic case, and city district.
"""

# Create the CSV file: csvfile
csvfile = open('crime_sampler.csv','r')

# Create a dictionary that defaults to a list: crimes_by_district
crimes_by_district = defaultdict(list)

# Loop over a DictReader of the CSV file
for row in csv.DictReader(csvfile):

    # Pop the district from each row: district
    district = row.pop('District')

    # Append the rest of the data to the list for proper district in crimes_by_district
    crimes_by_district[district].append(row)

######################### Task 6 ################################################    
    
"""
Determine the Arrests by District by Year
Using your crimes_by_district dictionary from the previous exercise, you'll now determine the number arrests in each City district for each year. Counter is already imported for you. You'll want to use the IPython Shell to explore the crimes_by_district dictionary to determine how to check if an arrest was made.
"""
# Loop over the crimes_by_district using expansion as district and crimes
for district, crimes in crimes_by_district.items():
    # Print the district
    print(district)
    
    # Create an empty Counter object: year_count
    year_count = Counter()
    
    # Loop over the crimes:
    for crime in crimes:
         # If there was an arrest
        if crime['Arrest'] == 'true':
            # Convert the Date to a datetime and get the year
            year = datetime.strptime(crime['Date'], '%m/%d/%Y %I:%M:%S %p').year
            # Increment the Counter for the year
            year_count[year] += 1
            
    # Print the counter
    print(year_count)


######################### Task 7 ################################################

"""
Unique Crimes by City Block
You're in the home stretch!

Here, your data has been reshaped into a dictionary called crimes_by_block in which crimes are listed by city block. Your task in this exercise is to get a unique list of crimes that have occurred on a couple of the blocks that have been selected for you to learn more about. You might remember that you used set() to solve problems like this in Chapter 1.
"""

# Create a unique list of crimes for the first block: n_state_st_crimes
n_state_st_crimes = set(crimes_by_block['001XX N STATE ST'])

# Print the list
print(n_state_st_crimes)

# Create a unique list of crimes for the second block: w_terminal_st_crimes
w_terminal_st_crimes = set(crimes_by_block['0000X W TERMINAL ST'])

# Print the list
print(w_terminal_st_crimes)

# Find the differences between the two blocks: crime_differences
crime_differences = n_state_st_crimes - w_terminal_st_crimes
# Print the differences
print(crime_differences)





