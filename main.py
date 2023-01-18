# Importing the modules
import urllib.request
from data import temp
from data import precipitation
from data import humidity
from data import wind
import datetime

# updating the data file.
data = "https://raw.githubusercontent.com/ChristianHiland/PyKorean/main/files/data.py"
filename, headers = urllib.request.urlretrieve(data, filename="data.py")

# Getting the time
x = datetime.datetime.now()
day = x.strftime("%d")

# The weather
print("////////////////////////////////////////////////////////////////")
print("The weather for today. /////////////////////////////////////////")
print("")
print("Temp: ", temp[day], "Precipitation: ", precipitation[day], "Humidity: ", humidity[day], "Wind Speed: ", wind[day])
print("////////////////////////////////////////////////////////////////")
print("")

# The plant growth thing.
print("Do you want to measure the growth rate of your plant?")
print(" ")
user = input("Yes/No: ")

if user.lower == str("yes"):
  s1 = input("The 2 measurement: ")
  s2 = input("The 2 measurement: ")
  days = input("The number of days between each measurement: ")
  s12 = s1-s2
  print(s12/days)
else:
  exit
