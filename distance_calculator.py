# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 12:30:32 2017

@author: iibanez
Distance Between Two Cities - Calculates the distance between two cities and 
allows the user to specify a unit of distance. This program may require 
finding coordinates for the cities like latitude and longitude.
"""

#from pygeocoder  import Geocoder
import geocoder
import numpy as np

def getdistance(locA,locB):
    '''
    Function input:
        locA,locB: latitude and longitude coordinates in degrees, of two places
    the function uses  Haversine formula to calculate the distance between
    two places.
    '''
    r = 6371.0
    radlocA = [0,0]
    radlocB = [0,0]
    radlocA[0] = np.deg2rad(locA[0])
    radlocA[1] = np.deg2rad(locA[1])
    radlocB[0] = np.deg2rad(locB[0])
    radlocB[0] = np.deg2rad(locB[0])
    varlat = radlocA[0] - radlocB[0]
    varlong = radlocA[1] - radlocB[1]
    a = (np.sin(varlat/2))**2 + np.cos(radlocA[0])*np.cos(radlocB[0])* \
    (np.sin(varlong/2))**2
    c = 2* np.arctan2(np.sqrt(a),np.sqrt(1-a))
    d = r * c
    return d


def getlatlong(place):
    ''' using Google maps API, it calculates latitude and longitude accpeting
    an script as input
    '''
    g = geocoder.google(place)
    return g.latlng


def convert_km_to_miles(km):
    '''function that simply convert distance from Km to Miles
    '''
    miles_per_km = 0.621371192
    return km * miles_per_km


def distance_calculator():
    '''
    main script that ask the user the metric units, and two strings defining
    places (understandable by google maps), and returns the distance
    between them
    '''
    # first, the metric units have to be defined
    while True:
        units = str(raw_input('Please, Enter the metric units, Km or Miles\n'))
        if units in ['Km','km','KM','k','K']:
            units = 'Km' 
            break
        elif units in ['Miles','miles','m','M' ]:
            units = 'Miles'
            break
        else:
            print ' Please, Introduce Km or Miles as the units'
    # Then, the two places have to be defined. those need to be recognized
    # By google maps
    while True:
        placeA = str(raw_input ('\n Please, introduce the first place to calculate distance\n'))
        placeB = str(raw_input ('\n Please, introduce the second place to calculate distance\n'))
        locA = getlatlong(placeA)
        locB = getlatlong(placeB)
        if locA == []:
            if locB != []:
                print ' Sorry, Google maps does not recognize the  first location'
        elif locB == []:
            if locA != []:
                print ' Sorry, Google maps does not recognize the second location'
        if locA == []:
            if locB == []:
                print ' Sorry, Google maps does not recognize none of the locations'
        if locA != []:
            if locB !=[]:
                break
    #finally, the distance between the two places is calculated
    d= getdistance(locA,locB)
    if units == 'Km':
        print 'the distance between {} and {} is {} Km'.format(placeA,placeB,d)
    elif units == 'Miles':
         d = convert_km_to_miles(d)
         print 'the distance between {} and {} is {} Miles'.format(placeA,placeB,d)
         
        
        
distance_calculator()
            
        
    
 