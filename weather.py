import csv
from datetime import datetime
from statistics import mean

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """

    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    dt = datetime.fromisoformat(iso_string)
    formatted_date = dt.strftime("%A %d %B %Y")
    return formatted_date



def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    result = (float(temp_in_farenheit) - 32) * 5/9
    return round(result, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    result=mean([float(x) for x in weather_data])
    if (result % 2) == 0:
        return int(result)
    else:
        return round(result, 1)
    


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, 'r') as my_file:
        csv_reader = csv.reader(my_file)
        for row in csv_reader:
            data.append(row)
    return data



def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    for element in weather_data:
        if isinstance(element, str):
            weather_data = ([float(x) for x in weather_data])

    if not weather_data:
        return ()
    else:
        min_value = min(weather_data)
        weather_data.reverse()
        index = len(weather_data) - weather_data.index(min_value) - 1
        return min_value, index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    for element in weather_data:
        if isinstance(element, str):
            weather_data = ([float(x) for x in weather_data])

    if not weather_data:
        return ()
    else:
        max_value = max(weather_data)
        weather_data.reverse()
        index = len(weather_data) - weather_data.index(max_value) - 1
        return max_value, index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    list_of_dates = []
    list_of_lows = []
    list_of_highs = []
        
    for row in weather_data:
        list_of_dates.append(convert_date(row[0]))
        list_of_lows.append(convert_f_to_c(row[1]))
        list_of_highs.append(convert_f_to_c(row[2]))

    date_lowest = list_of_dates[find_min(list_of_lows)[1]]
    date_highest = list_of_dates[find_max(list_of_highs)[1]]


    return f"{len(weather_data)} Day Overview\n"\
    f"  The lowest temperature will be {format_temperature(find_min(list_of_lows)[0])}, and will occur on {date_lowest}.\n"\
    f"  The highest temperature will be {format_temperature(find_max(list_of_highs)[0])}, and will occur on {date_highest}.\n"\
    f"  The average low this week is {format_temperature(calculate_mean(list_of_lows))}.\n"\
    f"  The average high this week is {format_temperature(calculate_mean(list_of_highs))}.\n"



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
