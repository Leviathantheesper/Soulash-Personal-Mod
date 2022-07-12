# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 17:47:59 2022

@author: dcmol
"""

import os
import re
import random
import json

def equipment_randomize():
    data={}
    with open("ids.json") as ids_json:
        data=json.load(ids_json)
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    with open("729_Gnome_villager.json") as gnome:
        data=json.load(gnome)
        print(data)
equipment_randomize()