from flask import Flask, render_template, request, jsonify
import pygeoip
import sys
from flask import Flask
from flask_googlemaps import GoogleMaps
reload(sys)
sys.setdefaultencoding('utf8')
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

#connect db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://boby:josette@server/ipchecker'
db = SQLAlchemy(app)
SQLALCHEMY_ECHO = True
# Initialize the Flask application



# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyBx4w9J1n4D3BWBczKP4rA_w4MMn_B6XIk"

GoogleMaps(app)

# Default route, print user's IP
# geolocation

@app.route('/')

def index():
  ip = '132.89.198.23' #request.remote_addr
  rawdata = pygeoip.GeoIP('/opt/GeoIP/GeoLiteCity.dat')
  data = rawdata.record_by_name(ip)
  codecountry = data['country_code']
  country = data['country_name']
  #region = data['region_name']
  code = data['area_code']
  postal = data['postal_code']
  city = data['city']
  longi = data['longitude']
  lat = data['latitude']
  return render_template('index.html', user_ip=ip, country_code=codecountry, area_code=code, postal_code=postal, country_name=country, city=city, longitude=longi, latitude=lat)

def mapview():
    # creating a map in the view
    location = geolocator.geocode(request.remote_addr)
    mymap = Map(
        identifier="view-side",
        lat=location.latitude,
        lng=location.longitude,
        markers=[(lat, longi)]
    )
    return render_template('index.html', mymap=mymap)

@app.errorhandler(500)
def error_500(e):
    return render_template('index.html', country_name='Error finding GeoIP data for that address', country_code='Error finding GeoIP data for that address', area_code='Error finding GeoIP data for that address', postal_code='Error finding GeoIP data for that address', city='Error finding GeoIP data for that address', longitude='Error finding GeoIP data for that address', latitude='Error finding GeoIP data for that address')


if __name__ == '__main__':
  app.run(
        host="0.0.0.0",
        port=int("2000")
  )
