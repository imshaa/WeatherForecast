import requests
import json
import pyttsx3
if __name__ == '__main__':
    engine = pyttsx3.init()

    engine.setProperty('rate', 150)

    engine.say("Welcome to the weather Forecast ! ")
    engine.runAndWait()
    engine.say("Enter the name of your city ")
    engine.runAndWait()
    city = input("Enter the name of the city: ")
    
    

    url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY_HERE={city}"
    try:
        r = requests.get(url)
        weather_dic = json.loads(r.text)
        if "error" in weather_dic:
            engine.say("Sorry, I couldn't fetch the weather data. Please check the city name and try again.")
            engine.runAndWait()
            print("Error:", weather_dic["error"]["message"])
        else:
            name = weather_dic["location"]["name"]
            region = weather_dic["location"]["region"]
            contry = weather_dic["location"]["country"]
            localtime= weather_dic["location"]["localtime"]
            temperature = weather_dic["current"]["temp_c"]
            Humidity = weather_dic["current"]["humidity"]
            engine.say(f"Here the Weather information About {city}")
            engine.runAndWait()
            print(f"Here the Weather information About {city}")
            engine.say(f"The Name of City is {name}")
            engine.runAndWait()
            print(f"The Name of City is {name}")
            engine.say(f"The Region of {city} is {region}")
            engine.runAndWait()
            print(f"The Region of {city} is {region}")
            engine.say(f"The Country is {contry}")
            engine.runAndWait()
            print(f"The Country is {contry}")
            engine.say(f"The Local Time of {city} is {localtime}")
            engine.runAndWait()
            print(f"The Local Time of {city} is {localtime}")
            engine.say(f"The Temperature of {city} is {temperature} degree Celsius")
            engine.runAndWait()
            print(f"The Temperature of {city} is {temperature} °C")
            engine.say(f"The Humidity of {city} is {Humidity} percent")
            engine.runAndWait()
            print(f"The Humidity of {city} is {Humidity}% ")
            engine.say("Thank You For Choosing Me As your Weather Forecast. Have a nice Day !")
            engine.runAndWait()
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        engine.say("Network error. Please check your connection and try again.")
        engine.runAndWait()
