# GetCovidData

You can use this API to access basic `Covid Data` with simple commands. <br>
This package makes it easy for you to get Covid Data. You can use it in the backend to get covid data and display it on your website or use this data in your python scripts!

<h1> Installation </h1>

This API can be installed by using <b> pip </b> in the following way: <br>
<code> pip install GetCovidData </code>
 
 <h1>Usage:</h1>

Here is how to use this package (for more details about <b> syntax</b> and <b> functions </b>  you can take a look at the <code>examples.py</code> file)

<table>
<tr><th>Function</th><th>Params:</th><th>What it does!</th></tr>
<tr><td><b>get_covid_info ()</b></td><td> display (True/False), default=True</td><td>Return a JSON object with the latest info of Covid like "Active cases". If diplay=True it will also print the covid info.</td></tr>
<tr><td><b>get_covid_by_continent ()</b></td><td>None</td><td>Returns a pandas dataframe containing the Covid Info in all continents!</td></tr>
<tr><td><b>get_covid_by_continentJSON()</b></td><td>None</td><td>Retuens a JSON object with Covid Situation in all continents</td></tr>
<tr><td><b>get_covid_all_countries()</b></td><td>None</td><td>Returns a pandas DataFrame containing Covid Info in all countries</td></tr>
<tr><td><b>get_covid_all_countriesJSON()</b></td><td>None</td><td>Retuens a JSON object with Covid Info in all countries</td></tr>
<tr><td><b>get_covid_in_countries()</b></td><td>*args countries(countries to get covid data of), json= False</td><td>Return a pandas dataframe containing covid info in given countries. You can pass as many countries as you want. If json=True it will return a JSON object instead</td></tr>
</table>

<h1> Example of USE </h1>

![Covid Api Use case example](https://user-images.githubusercontent.com/87518251/190380274-8b21e9ca-fbb6-4a37-8b35-79bb02e6d203.png)

 
 ## Output 
 
 ![Out put of the above code snippet](https://user-images.githubusercontent.com/87518251/190379958-d57e4ed5-4d9c-4580-841d-9cd7586ef6c5.png)

<p> For more information on <b> how to use this package </b> refer to the <b><i> eamples.py</i></b> file! You can alse get details of each function by using this code snippet <p>

![Use this code snippet for help](https://user-images.githubusercontent.com/87518251/190381383-0d8b2737-7df1-42b6-92d6-cec1474044f9.png)



<h1> Future Plan </h1>

In future we plan  to add more functionality to the API giving you access to more data. <br>

