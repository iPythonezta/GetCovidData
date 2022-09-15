from GetCovidData.src import CovidApi
import json



# initialize an api
api = CovidApi()

#Get brief detail of Covid Situation

covid_info = api.get_covid_info(display=True) 
# Will return a JSON object and will print the details. Set display = False if you dont want it to print details
# It will still return a JSON object
covid_info =  json.loads(covid_info) # Convert Json object to python dictionary
print("Total Covid Cases: ", covid_info['Total Cases']) #Access total Covid Cases


# You can also get covid by continent
data_by_continent = api.get_covid_by_continent() 
# This will return Covid data of all continents in the form of Pandas DataFrame
# If you want data in JSON format use api.get_covid_by_continentJSON()
print(data_by_continent)


# You can get details of Covid in all countries in the form of pandas dataframe
data_by_countries = api.get_covid_all_countries() 
#Similar to get_covid_by_continent() function it gives you details of covid in all countries
# Also you can get this data in JSON format using api.get_covid_all_countriesJSON() function
print(data_by_countries)

# You can get details of Covid in a specific country or group of countries like this
# if JSON = False it will return a pandas Dataframe
# id JSON = True it returns a JSON object
covid_in_specific_countries =  api.get_covid_in_countries('Pakistan','India','Afghanistan','Australia', json=False)
print(covid_in_specific_countries)


