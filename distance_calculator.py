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

            
class Distanciator(object):
    '''
    main class that ask the user the metric units, and two strings defining
    places (understandable by google maps), and returns the distance
    between them
    '''
    def __init__(self):
        self.units = ''
        self.placeA = ''
        self.placeB = ''
        self.d = 0
        self.g = None
        self.locA = []
        self.locB = []
    
    def calculate(self):
        # first, the metric units have to be defined
        while True:
            self.units = str(raw_input('Please, Enter the metric units, Km or Miles\n'))
            if self.units in ['Km','km','KM','k','K']:
                self.units = 'Km' 
                break
            elif self.units in ['Miles','miles','m','M' ]:
                self.units = 'Miles'
                break
            else:
                print ' Please, Introduce Km or Miles as the units'
        # Then, the two places have to be defined. those need to be recognized
        # By google maps
        while True:
            self.placeA = str(raw_input ('\n Please, introduce the first place to calculate distance\n'))
            self.placeB = str(raw_input ('\n Please, introduce the second place to calculate distance\n'))
            self.locA = self.getlatlong(self.placeA)
            self.locB = self.getlatlong(self.placeB)
            if self.locA == []:
                if self.locB != []:
                    print ' Sorry, Google maps does not recognize the  first location'
            elif self.locB == []:
                if self.locA != []:
                    print ' Sorry, Google maps does not recognize the second location'
            if self.locA == []:
                if self.locB == []:
                    print ' Sorry, Google maps does not recognize none of the locations'
            if self.locA != []:
                if self.locB !=[]:
                    break
        #finally, the distance between the two places is calculated
        self.d= self.getdistance()
        if self.units == 'Km':
            print 'the distance between {} and {} is {} Km'.format(self.placeA,self.placeB,self.d)
        elif self.units == 'Miles':
             self.convert_km_to_miles()
             print 'the distance between {} and {} is {} Miles'.format(self.placeA,self.placeB,self.d)
   
    def convert_km_to_miles(self):
        '''function that simply convert distance from Km to Miles
        '''
        miles_per_km = 0.621371192
        self.d = self.d * miles_per_km
            
            
    def getlatlong(self, place):
        ''' using Google maps API, it calculates latitude and longitude accepting
        an script as input
        '''
        self.g = geocoder.google(place)
        return self.g.latlng
    
    
    def getdistance(self):
        '''
        Method input:
        locA,locB: latitude and longitude coordinates in degrees, of two places
        the function uses  Haversine formula to calculate the distance between
        two places.
        '''
        r = 6371.0
        radlocA = [0,0]
        radlocB = [0,0]
        radlocA[0] = np.deg2rad(self.locA[0])
        radlocA[1] = np.deg2rad(self.locA[1])
        radlocB[0] = np.deg2rad(self.locB[0])
        radlocB[0] = np.deg2rad(self.locB[0])
        varlat = radlocA[0] - radlocB[0]
        varlong = radlocA[1] - radlocB[1]
        a = (np.sin(varlat/2))**2 + np.cos(radlocA[0])*np.cos(radlocB[0])* \
        (np.sin(varlong/2))**2
        c = 2* np.arctan2(np.sqrt(a),np.sqrt(1-a))
        self.d = r * c
        return self.d
    
iker = Distanciator()
iker.calculate()
iker.d
    
 