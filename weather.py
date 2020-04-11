from tkinter import *
# API weather key:
# a600a417c7c47c34b9f84894538fda7b
window = Tk()
window.geometry("600x300")

def lookWeather():
    import requests
    import json
    try:
        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?units=metric&q=" + city.get() + "&appid=a600a417c7c47c34b9f84894538fda7b")
        api = json.loads(api_request.content)
        city_ = api['name']
        country = api['sys']['country']
        weather = api['main']['temp']
        feels = api['main']['feels_like']
        weather1 = api['weather'][0]['main']

        myLabel = Label(window, text=f"City: {city_}, {country}\nWeather: {weather1}\nTemperature: {weather}\nFeels like: {feels}",font=("Helvetica", 20) )
        myLabel.pack()

    except Exception as e:
        api = "Error! "

def lookAir():
    import requests
    import json
    try:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + city.get() + "&distance=5&API_KEY=C8FA690B-81D3-438B-802D-68E31F34316C")
        api = json.loads(api_request.content)
        city_ = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        myLabel = Label(window, text=city_ + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20))
        myLabel.pack()

    except Exception as e:
        api = "Error..."

lookup_frame = LabelFrame(window, text="Enter city name to look up weather or zipcode for air quality", padx=5, pady=5)
lookup_frame.pack()

city = Entry(lookup_frame)
city.pack()


submit1Button = Button(lookup_frame, text="Lookup Weather", command=lookWeather)
submit1Button.pack()

submit2Button = Button(lookup_frame, text="Lookup Air Quality", command=lookAir)
submit2Button.pack()



window.mainloop()





