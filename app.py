from flask import Flask, render_template, request
import requests

app = Flask(__name__)

OPENWEATHERMAP_API_KEY = '603cda784189d192e3aa2cbcc0983aa5'

@app.route('/', methods=['GET', 'POST'])
def index():
	weather_data = None
	if request.method == 'POST':
		city = request.form.get('city')
		if city:
			url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric'
			response = requests.get(url)
			if response.status_code == 200:
				weather_data = response.json()

	return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
	app.run(debug=True)

