from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_KEY = "871da2a6732da40a3868e0d7a5a0348f"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(WEATHER_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }
    else:
        return None

def get_forecast(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(FORECAST_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        forecast_list = data["list"][:5] 
        return [
            {"date": item["dt_txt"], "temp": item["main"]["temp"], "desc": item["weather"][0]["description"]}
            for item in forecast_list
        ]
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        weather = get_weather(city)
        if weather:
            return render_template("weather.html", weather=weather, city=city)
        else:
            return render_template("weather.html", error="City not found")

    return render_template("weather.html")

@app.route("/forecast", methods=["POST"])
def forecast():
    city = request.form["city"]
    forecast_data = get_forecast(city)
    
    if forecast_data:
        return render_template("forecast.html", forecast=forecast_data, city=city)
    else:
        return render_template("forecast.html", error="City not found")

from flask import Flask, render_template, request, redirect

@app.route("/info")
def info():
    return redirect("https://www.pmaccelerator.io/")


if __name__ == "__main__":
    app.run(debug=True)