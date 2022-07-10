# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 18:07:13 2022

@author: dcmol
"""
import os
import re
import random
import json
  
    
def weapon_randomize():
    """
    Randomizes entity (weapons) damage.
    Returns
    -------
    None.

    """
    weapon_words=["attack_speed","damage","dmg_type","hands","hit_bonus",
                  "parry_bonus","range","type"]
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    list_dir.remove('weapons.py')
    counter=1
    for filename in list_dir:
        data={}
        with open(filename) as json_file:
            data=json.load(json_file)
            if "weapon" in data:
                spdmult=0.8*random.random()+0.6
                new_value=round(spdmult*data["weapon"]["attack_speed"],1)
                print(data["weapon"])
                data["weapon"]["attack_speed"]=new_value
                data["weapon"]["hands"]=random.randint(1,2)
                rngmult=random.randint(1,2)
                data["weapon"]["range"]=max(1,rngmult*data["weapon"]["range"])
                print(data["weapon"])
                
        print(data)
weapon_randomize()