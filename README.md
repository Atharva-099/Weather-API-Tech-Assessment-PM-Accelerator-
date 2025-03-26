1. Clone the Repository
First, download the project files from GitHub by running:
git clone https://github.com/Atharva-099/Weather-API-Tech-Assessment-PM-Accelerator-.git
cd Weather-API-Tech-Assessment-PM-Accelerator-


2. Create a Virtual Environment (Optional but Recommended)
Setting up a virtual environment helps keep dependencies organized:
source venv/bin/activate

3. Install Dependencies
The app requires some Python libraries to function. Install them by running:
pip install -r requirements.txt


4. Run the Flask Application
Start the app by running:
python app.py
Once the server is running, open your browser and go to:
http://127.0.0.1:5000/


Features:

Enter a city name to get the current weather (temperature, humidity, wind speed, and description).

Option to view a 5-day weather forecast.

An info button redirects to PM Accelerator.

API Used:

OpenWeatherMap API for fetching weather data.
