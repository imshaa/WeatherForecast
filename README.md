# 🌦 Weather Forecast with Robotic Voice Speaker

This Python project fetches real-time weather data and reads it aloud using a robotic voice. It uses **WeatherAPI** to retrieve weather details and **pyttsx3** for text-to-speech functionality.

## 🚀 Features
- 🌍 Get real-time weather updates for any city
- 🔊 Robotic voice assistant (using `pyttsx3`)
- 📌 Fetches details like temperature, humidity, region, and time
- 🛠 Error handling for incorrect city names or network issues

## 🛠 Technologies Used
- Python
- `requests` (for fetching weather data)
- `json` (for parsing API response)
- `pyttsx3` (text-to-speech conversion)

## 📥 Installation
### 1️⃣ Clone the repository
```sh
git clone https://github.com/imshaa/WeatherForecast.git
cd weather-forecast-voice
```

### 2️⃣ Install required dependencies
```sh
pip install requests pyttsx3
```

## 🎤 How It Works
1. The program **asks the user for a city name**
2. It fetches **real-time weather data** from WeatherAPI
3. The **robotic voice speaker (pyttsx3)** reads out the weather details

## 📜 Usage
```sh
python weather_forecast.py
```
Then enter a city name when prompted. The program will fetch the weather and read it out loud.

## 🔊 About Robotic Voice Speaker
This project uses `pyttsx3`, a **text-to-speech** conversion library in Python that works offline. It supports multiple voice properties:
- **Rate** (speed of speech)
- **Volume**
- **Different voice types** (male/female)

By default, it reads weather details in a **robotic voice** to make the experience more interactive.

## 📌 Example Output
```sh
Enter the name of the city: London
🔊 "Here is the weather information for London. The temperature is 15 degrees Celsius. The humidity is 80%."
```

## 🛠 Future Improvements
- ✅ Add voice input support
- ✅ Improve speech clarity and intonation
- ✅ Display additional weather details like wind speed

## 🤝 Contributing
Feel free to fork this project and improve it! Pull requests are welcome. 😊

## 📄 License
This project is open-source and available under the **MIT License**.

---
🔗 **Follow for more cool projects!** 🚀


