from django.http import HttpResponse
from django.shortcuts import render
import googlemaps
from Email.views import sendEmail

geocodeAPIKey="AIzaSyDfsbw3O9ZX3wJr7FSkLvcyD_Qg3C0G6M0"

def index(request):
    return HttpResponse("Index")

def coordinatesToLocation(request, latitude,longitude):
    """This function does nothing."""

    gmaps = googlemaps.Client(key=geocodeAPIKey)
    reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
    print reverse_geocode_result

    return ""


def locationToCoordinates(request, location):
    """This function does nothing."""

    print "I am here"
    gmaps = googlemaps.Client(key=geocodeAPIKey)

    # Geocoding and address
    geocode_result = gmaps.geocode(location)
    print geocode_result

    latitude=123
    longitude =123
    #return {'latitude':latitude, 'longitude':longitude}
    return request

def calculateDistanceByCoordinates(request,latitude_A, longitude_A, latitude_B,longitude_B,travel_mode):
    """This function does nothing."""
    #Travel Mode: driving, walking, bicycling, or transit.
    return "A"

def calculateDistanceByLocation(request,location_A, location_B,travel_mode):
    """This function does nothing."""
    #Travel Mode: driving, walking, bicycling, or transit.
    return "A"

def testMails(request):
    print "HERE"
    sendEmail("")
    return HttpResponse("done")

