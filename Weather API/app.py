from flask import Flask, 
     render_template, request
import requests
import json
import os

app = Flask(__name__)

picfolder = os.path.join('static','pics')
app.config['UPLOAD_FOLDER'] = picfolder

@app.route('/temperature', methods=['POST'])

def temperature():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], "weather1.jpg")
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=a802a031af600ff7a4811e9cd20fee1d')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    
    pressure = float(json_object['main']['pressure'])
    humidity = float(json_object['main']['humidity'])
    latitude = json_object['coord']['lat']
    longitude = json_object['coord']['lon']
    return render_template('temperature.html', image = pic1, latitude=latitude, longitude=longitude, temp=temp_f, pressure=pressure, humidity=humidity)
    
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
