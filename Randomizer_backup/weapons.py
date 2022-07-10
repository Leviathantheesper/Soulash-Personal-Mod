# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 18:07:13 2022

@author: dcmol
"""
#"ammo","backpack","belt","boots","head_armor","head_cloth","left_hand","legs_armor","legs_cloth","right_hand","torso_cloth","torso_armor"
import os
import re
import random
import json
def weaponcheck():
    ids=[]
    list_dir=os.listdir()
    list_dir.remove('weapons.py')
    for filename in list_dir:
        data={}
        with open(filename) as json_file:
            data=json.load(json_file)
            if "weapon" in data and not "health" in data and "item" in data and not "corpse" in data and "durability" in data:
                ids.append(data["id"])
    ids.sort()
    return ids
def armorcheck():
    ids=[]
    list_dir=os.listdir()
    list_dir.remove('weapons.py')
    for filename in list_dir:
        data={}
        with open(filename) as json_file:
            data=json.load(json_file)
            if "armor" in data and not "health" in data and "item" in data and not "corpse" in data and "durability" in data and not "weapon" in data:
                ids.append(data["id"])
    ids.sort()
    return ids
def equipcheck():
    equipment={}
    ammo=[194,234,857]
    equipment["ammo"]=ammo
    equipment["weapons"]=weaponcheck()
    equipment["armor"]=armorcheck()
    return equipment
def equiplist():
    with open("ids.json") as json_file:
        data=json.load(json_file)
        ids=equipcheck()
        weapons={}
        armor={}
        ammo={}
        for i in ids["weapons"]:
            weapons[i]=data[str(i)]
        for i in ids["armor"]:
            armor[i]=data[str(i)]
        for i in ids["ammo"]:
            ammo[i]=data[str(i)]
        equip={}
        print("Weapons ",len(weapons))
        print("armor ",len(armor))
        print("ammo ",len(ammo))
        equip["weapons"]=weapons
        equip["armor"]=armor
        equip["ammo"]=ammo
    with open("equipment.json",'w') as json_fill:
         json.dump(equip, json_fill,indent=4)
    return equip
equiplist()
     