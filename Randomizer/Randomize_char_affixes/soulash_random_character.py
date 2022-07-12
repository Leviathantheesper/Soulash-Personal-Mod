# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 01:22:57 2022

@author: dcmol
"""

import os
import re
import random
import json
def slodbkal(list_of_dicks,key,liss):
    for a in list_of_dicks:
        if key in a:
            b=random.choice(liss)
            liss.remove(b)
            a[key]=b
    return list_of_dicks
def affixes_randomize():
    """
    Randomizes entity (weapons) damage.
    Returns
    -------
    None.

    """
    data=""
    with open("affixes.json",'r+') as json_file:
        affixes_stats=["strength","intelligence","dexterity",
                         "willpower","endurance"]
        affixes_resistances=["acid","death","electricity","fire","frost",
             "holy","physical","poison"]
        affixes_damage=["acid","death","electricity","fire","frost",
             "holy","physical","poison"]
        affixes_other=["durability","weight","movement_speed","sight"]
        data=json.load(json_file)
        entries=list(data)
        chances=data["rarity_roll"]
        for i in chances:
            cheese=list(i)
            for j in cheese:
                base=round(0.045*random.random()+0.005,3)
                per_level=round(0.025*random.random()+0.005,3)
                i[j]['base']=base
                i[j]['per_level']=per_level
        prefixes=data["prefixes"]
        for i in prefixes:
            level=prefixes[i]
            for j in level:
                sas=affixes_stats.copy()
                for stat in sas:
                    if "statistics" in j:
                        if stat in j["statistics"]:
                            value=j["statistics"][stat]
                            j["statistics"].pop(stat,None)
                            newstat=random.choice(affixes_stats)
                            sas.remove(newstat)
                            if newstat not in j["statistics"]:
                                j["statistics"][newstat]=value
                            else:
                                j["statistics"][newstat]+=value
                            break
                for resis in affixes_resistances:
                    if "resistances" in j:
                        if resis in j["resistances"]:
                            value=j["resistances"][resis]
                            j["resistances"].pop(resis,None)
                            newstat=random.choice(affixes_resistances)
                            if newstat not in j["resistances"]:
                                j["resistances"][newstat]=value
                            else:
                                j["resistances"][newstat]+=value
                for element in affixes_damage:
                    if "damage" in j:
                        if element in j["damage"]:
                            value=j["damage"][element]
                            j["damage"].pop(element,None)
                            newstat=random.choice(affixes_damage)
                            if newstat not in j["damage"]:
                                j["damage"][newstat]=value
                            else:
                                j["damage"][newstat]=[j["damage"][newstat][0]+value[0],j["damage"][newstat][1]+value[1]]
                            var=0.5+random.random()
                            j["damage"][newstat]=[int(var*j["damage"][newstat][0]),int(var*j["damage"][newstat][1])]
                if "durability" in j:
                    j["durability"]=round(0.5+2.5*random.random(),1)
                if "weight" in j:
                    j["weight"]=round(0.5+0.4*random.random(),1)
                if "sight" in j:
                    j["sight"]=random.randint(1,3)
                if "movement_speed" in j:
                    j["movement_speed"]=-0.5*random.random()
        suffixes=data["suffixes"]
        for i in suffixes:
            level=suffixes[i]
            for j in level:
                sas=affixes_stats.copy()
                for stat in sas:
                    if "statistics" in j:
                        if stat in j["statistics"]:
                            value=j["statistics"][stat]
                            j["statistics"].pop(stat,None)
                            newstat=random.choice(affixes_stats)
                            sas.remove(newstat)
                            if newstat not in j["statistics"]:
                                j["statistics"][newstat]=value
                            else:
                                j["statistics"][newstat]+=value
                            break
                for resis in affixes_resistances:
                    if "resistances" in j:
                        if resis in j["resistances"]:
                            value=j["resistances"][resis]
                            j["resistances"].pop(resis,None)
                            newstat=random.choice(affixes_resistances)
                            if newstat not in j["resistances"]:
                                j["resistances"][newstat]=value
                            else:
                                j["resistances"][newstat]+=value
                for element in affixes_damage:
                    if "damage" in j:
                        if element in j["damage"]:
                            value=j["damage"][element]
                            j["damage"].pop(element,None)
                            newstat=random.choice(affixes_damage)
                            if newstat not in j["damage"]:
                                j["damage"][newstat]=value
                            else:
                                j["damage"][newstat]=[j["damage"][newstat][0]+value[0],j["damage"][newstat][1]+value[1]]
                            var=0.5+random.random()
                            j["damage"][newstat]=[int(var*j["damage"][newstat][0]),int(var*j["damage"][newstat][1])]
                if "durability" in j:
                    j["durability"]=round(0.5+2.5*random.random(),1)
                if "weight" in j:
                    j["weight"]=0.5+0.4*random.random()
                if "sight" in j:
                    j["sight"]=random.randint(1,3)
                if "movement_speed" in j:
                    j["movement_speed"]=-0.5*random.random()
        artifacts=data["artifacts"]
        abilities=[]
        for artifact in artifacts:
            if "ability" in artifact:
                abilities.append(artifact["ability"])
        artifacts=slodbkal(artifacts,"ability",abilities)
        for artifact in artifacts:
            sas=affixes_stats.copy()
            for stat in sas:
                if "statistics" in artifact:
                    if stat in artifact["statistics"]:
                        value=artifact["statistics"][stat]
                        artifact["statistics"].pop(stat,None)
                        newstat=random.choice(affixes_stats)
                        sas.remove(newstat)
                        if newstat not in artifact["statistics"]:
                            artifact["statistics"][newstat]=value
                        else:
                            artifact["statistics"][newstat]+=value
                        break
            for resis in affixes_resistances:
                if "resistances" in artifact:
                    if stat in artifact["resistances"]:
                        value=artifact["resistances"][stat]
                        artifact["resistances"].pop(stat,None)
                        newstat=random.choice(affixes_resistances)
                        if newstat not in artifact["resistances"]:
                            artifact["resistances"][newstat]=value
                        else:
                            artifact["resistances"][newstat]+=value
            for element in affixes_damage:
                if "damage" in artifact and artifact["name"]=="The Butcher":
                    if element in artifact["damage"]:
                        value=artifact["damage"][element]
                        artifact["damage"].pop(element,None)
                        newstat=random.choice(affixes_damage)
                        if newstat not in artifact["damage"]:
                            artifact["damage"][newstat]=value
                        else:
                            artifact["damage"][newstat]=[artifact["damage"][newstat][0]+value[0],artifact["damage"][newstat][1]+value[1]]
                        var=0.9+1.5*random.random()
                        artifact["damage"][newstat]=[int(var*artifact["damage"][newstat][0]),int(var*artifact["damage"][newstat][1])]
            if "durability" in artifact:
                artifact["durability"]=round(0.5+2.5*random.random(),1)
            if "weight" in artifact:
                artifact["weight"]=0.5+0.4*random.random()
            if "sight" in artifact:
                artifact["sight"]=random.randint(1,3)
            if "movement_speed" in artifact:
                artifact["movement_speed"]=-0.5*random.random()
        json_file.close()
        with open("affixes.json",'w') as json_file:
            json.dump(data, json_file,indent=4)

        
        
            
        
affixes_randomize()