from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="example app")
point = geolocator.geocode("332 Hill St San Francisco California 94114 USA").raw
print("lat:", point['lat'])
print("lon:", point['lon'])