
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







