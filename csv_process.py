import pandas
import os
from geopy.geocoders import Nominatim


def scv_validate(file):
    filename, ext = os.path.splitext(file)
    if ext == ".csv":
        df = pandas.read_csv(file)
        if 'Address' in df.columns:
            return True
        else:
            return False
    else:
        print("Invalid")
        return False


def process_csv(file):
    df = pandas.read_csv(file)
    df['lat'] = [get_lat(address) for address in df.Address]
    df['lon'] = [get_lon(address) for address in df.Address]
    return df


def get_lat(address):
    locator = Nominatim(user_agent="example app")
    point = locator.geocode(address).raw
    return point['lat']


def get_lon(address):
    locator = Nominatim(user_agent="example app")
    point = locator.geocode(address).raw
    return point['lon']
