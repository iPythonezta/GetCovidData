from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import re

class CovidApi:
    def __init__(self):
        self.name = 'CovidApi'
        self.website = "https://www.worldometers.info/coronavirus/"
    
    def get_covid_info(self, display=True):
        """
        Optional args:

        display: True (prints Result + returns JSON object) if False it will return a JSON object only (will not print results)

        What it does:

        This function prints covid info like total covid cases, recovered cases, active cases, ... etc

        Return:

        A json object containing information

        """


        data = {}
        page =  requests.get(self.website)
        soup = BeautifulSoup(page.text, "html.parser")
        Cases = soup.find('div', attrs={'class':'maincounter-number'}).text.strip()
        Deaths =  soup.find_all('div', attrs={'class': 'maincounter-number'})[1].text.strip()
        Recovered =  soup.find_all('div', attrs={'class': 'maincounter-number'})[2].text.strip()
        Active =  soup.find('div', attrs={'class': 'number-table-main'}).text.strip()
        Critial = soup.find_all('span', attrs={'class':'number-table'})[1].text.strip()
        Mild = soup.find_all('span', attrs={'class':'number-table'})[0].text.strip()
        if display:
            print('Total Covid Cases : ', Cases)
            print('Deaths by Covid : ', Deaths)
            print('No of Recoveries : ', Recovered)
            print('Active Covid Cases : ', Active)
            print('Critical Cases : ', Critial)
            print('Mild Cases : ', Mild)
        
        data['Total Cases'] = Cases
        data['Death by Covid'] = Deaths
        data['Recovered'] = Recovered
        data['Active Covid Cases'] = Active
        data['Critical Covid Cases '] = Critial
        data['Mild Covid Cases'] = Mild

        data = json.dumps(data)
        return data


    def get_covid_by_continent(self):

        """
        Returns a pandas DataFrame containing information of Covid in different continents
        """



        url = self.website
        r = requests.get(url)
        r = re.sub(r'<.*?>', lambda g: g.group(0).upper(), r.text)
        df = pd.read_html(r)[0]
        df = df[['Country,Other', 'TotalCases', 'NewCases', 'TotalDeaths','NewDeaths','ActiveCases']]
        df['Continent'] = df['Country,Other'] 
        df.head()
        df = df[['Continent', 'TotalCases', 'NewCases', 'TotalDeaths','NewDeaths','ActiveCases']]
        index = 0
        for row in df.Continent:
            if row not in ['North America', 'Asia','Europe','South America','Oceania','Africa']:

                df = df.drop(index)
                index +=1

            else:
                index += 1
                continue
        for columns in df.columns:
            df[columns] = df[columns].fillna('-')
        
        df = df.reset_index()
        df = df.drop(['index'], axis=1)

        return df

    def get_covid_by_continentJSON(self):
        """
        Returns COVID DATA for each continent in JSON form
        """

        df = self.get_covid_by_continent()
        df = df.to_json()
        return df

    def get_covid_all_countries(self): 
        
        """
        Get Covid Data of all countries in the form of pandas dataframe
        """


        url = self.website
        r = requests.get(url)
        r = re.sub(r'<.*?>', lambda g: g.group(0).upper(), r.text)
        df = pd.read_html(r)[0]
        df = df[['Country,Other', 'TotalCases', 'NewCases', 'TotalDeaths','NewDeaths','ActiveCases']]
        df['Continent'] = df['Country,Other'] 
        df.head()
        df = df[['Continent', 'TotalCases', 'NewCases', 'TotalDeaths','NewDeaths','ActiveCases']]
        index = 0
        for row in df.Continent:
            if str(row).strip() in ['North America', 'Asia','Europe','South America','Oceania','Africa', 'nan','Total:']:
                df = df.drop(index)
                index +=1

            else:
                index += 1
                continue
        for columns in df.columns:
            df[columns] = df[columns].fillna('-')

        df['Country'] = df['Continent']
        df = df[['Country', 'TotalCases', 'NewCases', 'TotalDeaths','NewDeaths','ActiveCases']]
        
        df = df.reset_index()
        df = df.drop(['index'], axis=1)

        return df
    
    def get_covid_all_countriesJSON(self):

        """
        get covid data of all countries in the form of JSON objects
        """


        df = self.get_covid_all_countries()
        df = df.to_json()
        return df

    def get_covid_in_countries(self, *args, json=False):

        """
        Get Covid in specified countries

        Params:

        *args: Enter as many countries to get data of
        json: if True it will return a json object instead of PANDAS dataframe default = False

        """
        df = self.get_covid_all_countries()
        x = []
        for country in args:
            x.append(country.capitalize())
        

        new_df =  df[df['Country'].isin(x)]

        if json:
            return new_df.to_json()

        return new_df
            
            




