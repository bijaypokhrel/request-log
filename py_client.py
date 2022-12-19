from time import gmtime, strftime
import datetime
import requests


response = requests.get('https://google.com/')

print(response.text)


# using simple format of showing time
# s = strftime("%a, %d %b %Y %H:%M:%S + 1010", gmtime())
# print("Example 1:", s)

# Sun, 18 Dec 2022 06: 42: 17 GMT


# Function to convert string to datetime

# def convert(date_time):
# 	format = '%a, %d %b %Y %H:%M:%S %Z'
# 	datetime_str = datetime.datetime.strptime(date_time, format)

# 	return datetime_str


# Driver code
# date_time = response.headers['Date']
# print(convert(date_time))
# printed in default format


