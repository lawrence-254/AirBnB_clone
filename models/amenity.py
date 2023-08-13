#!/usr/bin/python3
'''importing parent class base model'''

from models.base_model import BaseModel


'''class amenity describing available amenities'''
class Amenity(BaseModel):
    '''public class attributes'''
    name = ""
