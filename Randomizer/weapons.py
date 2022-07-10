# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 18:07:13 2022

@author: dcmol
"""
import os
import re
import random
import json
  
def weaponcheck():
    ids=[]
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    list_dir.remove('weapons.py')
    for filename in list_dir:
        data={}
        with open(filename) as json_file:
            data=json.load(json_file)
            if "weapon" in data:
                ids.append(data["id"])
    return ids
def armorcheck():
    ids=[]
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    list_dir.remove('weapons.py')
    for filename in list_dir:
        data={}
        with open(filename) as json_file:
            data=json.load(json_file)
            if "armor" in data:
                ids.append(data["id"])
    return ids
print(weaponcheck())