# import required modules
import pandas as pd
import requests, json
import matplotlib.pyplot as plt
import numpy as np
import os

# Enter your API key here
api_key=os.environ["OPENWEATHERMAP"]
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
def previsao_dia(city_name):
	
# Give city name
# complete_url variable to store
# complete url address
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name
# get method of requests module
# return response object
	response = requests.get(complete_url)
	x = response.json()

	if x["cod"] != "404":
		y = x["main"]
		current_temperature = y["temp"]
		current_pressure = y["pressure"]
		current_humidity = y["humidity"]
		z = x["weather"]
		weather_description = z[0]["description"]

		print(" Temperature (Cº) = " +
						str(current_temperature - 273.15) +
			"\n Pressão atmosférica (in hPa unit) = " +
						str(current_pressure) +
			"\n Humidade (em percentual) = " +
						str(current_humidity) +
			"\n Descrição do tempo = " +
						str(weather_description))

	else:
		return("Cidade não encontrada")


def previsao_tempo(city_name):
	complete_url_forecast = "https://api.openweathermap.org/data/2.5/forecast?q="+ city_name +"&cnt=16&appid="+api_key
	response = requests.get(complete_url_forecast)
	x = response.json()
	if x["cod"] == "200":
		normalized_data = pd.json_normalize(x["list"])
		df = pd.DataFrame(normalized_data)

		# convertar valores para celsius
		df['main.temp_min'] = (df['main.temp_min'] - 273.15).round(2)
		df['main.temp_max'] = (df['main.temp_max'] - 273.15).round(2)
		df['dt_txt'] = pd.to_datetime(df['dt_txt'])

		df = df[['dt_txt', 'main.temp_min', 'main.temp_max']] 
		df = df.rename(columns={'dt_txt': 'data', 'main.temp_min': 'temp_min','main.temp_max': 'temp_max' })

		# Criando o gráfico e passando o dataframe
		plt.figure(figsize=(10, 6))
		plt.plot(df['data'], df['temp_max'], color='red', linestyle='-', marker='o', label='Temperatura Maxima')
		plt.plot(df['data'], df['temp_min'], color='blue', linestyle='-', marker='o', label='Temperatura Mínima')

		plt.title('Variação da Temperatura para os próximos dias')
		plt.xlabel('Hora do Dia')
		plt.ylabel('Temperatura (°C)')
		plt.legend()
		plt.grid(True)
		plt.show()
	else:
		print(" Cidade não encontrada ")	

def temperatura(city_name):
	
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name
	response = requests.get(complete_url)
	x = response.json()
	if x["cod"] != "404":
		y = x["main"]
		current_temperature = y["temp"]
		# fazer conversão de kelvin para celsius
		current_temperature = current_temperature - 273.15
		return current_temperature
	else:
		print(" Cidade não encontrada ")