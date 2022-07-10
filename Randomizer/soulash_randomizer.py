# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 15:15:16 2022

@author: dcmol
"""
import os
import re
import random
import json
def damage_randomize():
    """
    Randomizes entity (weapons) damage.
    Returns
    -------
    None.

    """
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    list_dir.remove('equipment.json')
    list_dir.remove('weapons.py')
    list_dir.remove('armor_classes.json')
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        jsons=''
        rewrite=True
        with open(filename,'r+') as file:
            jsons=file.read()
            var=10*random.random()
            stat_name="dmg_max"
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+"
            reg=re.search(pattern, jsons)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                new_line=re.sub("[0-9]+",str(stat_number),line)
                jsons=jsons.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            var=var*random.random()
            stat_name="dmg_min"
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+"
            reg=re.search(pattern, jsons)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                new_line=re.sub("[0-9]+",str(stat_number),line)
                jsons=jsons.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(jsons)
                file.close()
def exp_randomize():
    """
    Randomizes entity exp.
    Returns
    -------
    None.

    """
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    list_dir.remove('equipment.json')
    list_dir.remove('weapons.py')
    list_dir.remove('armor_classes.json')
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        jsons=''
        rewrite=True
        with open(filename,'r+') as file:
            jsons=file.read()
            var=0.5+4.5*random.random()
            stat_name="exp"
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+"
            reg=re.search(pattern, jsons)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                new_line=re.sub("[0-9]+",str(stat_number),line)
                jsons=jsons.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(jsons)
                file.close()
def health_randomize():
    """
    Randomizes entity exp.
    Returns
    -------
    None.

    """
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    list_dir.remove('equipment.json')
    list_dir.remove('weapons.py')
    list_dir.remove('armor_classes.json')
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        jsons=''
        rewrite=True
        with open(filename,'r+') as file:
            jsons=file.read()
            var=0.5+7.5*random.random()
            stat_name="health"
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+"
            reg=re.search(pattern, jsons)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                new_line=re.sub("[0-9]+",str(stat_number),line)
                jsons=jsons.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(jsons)
                file.close()
def dur_randomize():
    """
    Randomizes entity durability.
    Returns
    -------
    None.

    """
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    list_dir.remove('equipment.json')
    list_dir.remove('weapons.py')
    list_dir.remove('armor_classes.json')
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        jsons=''
        rewrite=True
        with open(filename,'r+') as file:
            jsons=file.read()
            var=0.5+4.5*random.random()
            stat_name="durability"
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+"
            reg=re.search(pattern, jsons)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                new_line=re.sub("[0-9]+",str(stat_number),line)
                jsons=jsons.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(jsons)
                file.close()
def nutr_randomize():
    """
    Randomizes entity nutrition.
    Returns
    -------
    None.

    """
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    list_dir.remove('equipment.json')
    list_dir.remove('weapons.py')
    list_dir.remove('armor_classes.json')
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        jsons=''
        rewrite=True
        with open(filename,'r+') as file:
            jsons=file.read()
            var=0.5+1.5*random.random()
            stat_name="nutrition"
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+"
            reg=re.search(pattern, jsons)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                new_line=re.sub("[0-9]+",str(stat_number),line)
                jsons=jsons.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(jsons)
                file.close()
def liquidsources_randomize():
    """
    Randomizes entity liquid source limit.
    Returns
    -------
    None.

    """
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    list_dir.remove('equipment.json')
    list_dir.remove('weapons.py')
    list_dir.remove('armor_classes.json')
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        jsons=''
        rewrite=True
        with open(filename,'r+') as file:
            jsons=file.read()
            var=0.5+1.5*random.random()
            stat_name="liquid_source"
            da_stat="\""+stat_name+"\""
            sub_stat_name="limit"
            da_sub_stat="\""+sub_stat_name+"\""
            pattern=da_stat+r":\s[{]\n(.*\n)*\t*"+da_sub_stat+": [0-9]+"
            reg=re.search(pattern, jsons)
            try:
                lines=reg.group(0)
                splines=lines.splitlines()
                line=splines[len(splines)-1]
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                line=re.sub("[0-9]+",str(stat_number),line)
                splines[len(splines)-1]=line
                new_lines="\n".join(splines)
                jsons=jsons.replace(lines,new_lines)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(jsons)
                file.close()
def weight_randomize():
    """
    Randomizes entity weight.
    Returns
    -------
    None.

    """
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    list_dir.remove('equipment.json')
    list_dir.remove('weapons.py')
    list_dir.remove('armor_classes.json')
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        jsons=''
        rewrite=True
        with open(filename,'r+') as file:
            jsons=file.read()
            var=0.1+1.9*random.random()
            stat_name="weight"
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+[.][0-9]+"
            reg=re.search(pattern, jsons)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+[.][0-9]*", line).group(0)
                stat_number=round(var*float(statstring),1)
                new_line=re.sub("[0-9]+[.][0-9]*",str(stat_number),line)
                jsons=jsons.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(jsons)
                file.close()
def weapon_randomize():
    """
    Randomizes weapons stats.
    Returns
    -------
    None.

    """
    #weapon_words=["attack_speed","damage","dmg_type","hands","hit_bonus",
    #              "parry_bonus","range","type"]
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    list_dir.remove('equipment.json')
    list_dir.remove('weapons.py')
    list_dir.remove('armor_classes.json')
    for filename in list_dir:
        data={}
        with open(filename) as json_file:
            data=json.load(json_file)
            if "weapon" in data:
                spdmult=0.8*random.random()+0.6
                new_value=round(spdmult*data["weapon"]["attack_speed"],1)
                data["weapon"]["attack_speed"]=new_value
                data["weapon"]["hands"]=random.randint(1,2)
                rngmult=random.randint(1,2)
                data["weapon"]["range"]=max(1,rngmult*data["weapon"]["range"])
        with open(filename,'w') as json_file:
            json.dump(data, json_file,indent=4)
def resis_randomize():
    """
    Randomizes resistances.
    Returns
    -------
    None.

    """
    res=["acid","death","electricity","fire","frost",
         "holy","parry","physical","poison"]
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    list_dir.remove('equipment.json')
    list_dir.remove('weapons.py')
    list_dir.remove('armor_classes.json')
    for filename in list_dir:
        data={}
        with open(filename) as json_file:
            data=json.load(json_file)
            if "armor" in data:
                for types in res:
                    resmult=2*random.random()
                    resadd=random.randint(-2,2)
                    old_value=data["armor"][types]
                    new_value=max(int(resmult*old_value+resadd),0)
                    data["armor"][types]=new_value
        with open(filename,'w') as json_file:
            json.dump(data, json_file,indent=4)
def equip_randomize():
    """
    Randomizes entity equipment.
    Returns
    -------
    None.

    """
    equip_words=["right_hand","ammo","amulet","backpack","belt","boots",
                  "cape","gloves","head_armor","head_cloth","left_hand",
                  "legs_armor","legs_cloth","ring1","ring2","torso_armor",
                  "torso_cloth"]
    list_dir=os.listdir()
    list_dir.remove('soulash_randomizer.py')
    list_dir.remove('ids.json')
    list_dir.remove('equipment.py')
    list_dir.remove('equipment.json')
    list_dir.remove('weapons.py')
    list_dir.remove('armor_classes.json')
    with open("armor_classes.json") as armor_json:
        armors_by_class=json.load(armor_json)
        armor_json.close()
    with open("equipment.json") as equipment_json:
        equipment=json.load(equipment_json)
        equipment_json.close()
    hands={}
    for filename in list_dir:
        data={}
        with open(filename) as json_file:
            data=json.load(json_file)
            if "weapon" in data:
                hands[data["id"]]=data["weapon"]["hands"]
    for filename in list_dir:
        data={}
        with open(filename) as json_file:
            data=json.load(json_file)
            if "equipment" in data:
                data["equipment"]["ammo"]={}
                for limb in equip_words:
                    if limb != "backpack":
                        data["equipment"][limb]=[{}]
                for limb in equip_words:
                    if limb=="right_hand":
                        data["equipment"][limb][0]["chance"]=1.0
                        iden=random.choice(list(equipment["weapons"]))
                        data["equipment"][limb][0]["id"]=int(iden)
                        data["equipment"][limb][0]["name"]=equipment["weapons"][iden]
                        data["equipment"][limb][0]["stack"]=1
                        if re.search("crossbow",equipment["weapons"][iden],re.IGNORECASE):
                            data["equipment"]["ammo"][0]["chance"]=1.0
                            data["equipment"]["ammo"][0]["id"]=234
                            data["equipment"]["ammo"][0]["name"]="Bolt"
                            data["equipment"]["ammo"][0]["stack"]=random.randint(3,40)
                        elif re.search("bow",equipment["weapons"][iden],re.IGNORECASE):
                            data["equipment"]["ammo"][0]["chance"]=1.0
                            arrow_choice=random.choice(["194","857"])
                            data["equipment"]["ammo"][0]["id"]=int(arrow_choice)
                            data["equipment"]["ammo"][0]["name"]=equipment["ammo"][arrow_choice]
                            data["equipment"]["ammo"][0]["stack"]=random.randint(3,40)
                        else:
                            data["equipment"]["ammo"][0]["chance"]=0.1
                            arrow_choice=random.choice(["194","857","234"])
                            data["equipment"]["ammo"][0]["id"]=int(arrow_choice)
                            data["equipment"]["ammo"][0]["name"]=equipment["ammo"][arrow_choice]
                            data["equipment"]["ammo"][0]["stack"]=random.randint(1,3)
                    elif limb == "left_hand":
                        if hands[data["equipment"]["right_hand"][0]["id"]]==1:
                            data["equipment"][limb][0]["chance"]=0.1+0.8*random.random()
                            shields=[arm for arm in armors_by_class
                                     if armors_by_class[arm]=="left_hand"]
                            iden=random.choice(list(equipment["weapons"])+shields
                                               +shields+shields+shields)
                            data["equipment"][limb][0]["id"]=int(iden)
                            if iden in shields:
                                otherlimb="armor"
                            else:
                                otherlimb="weapons"
                            data["equipment"][limb][0]["name"]=equipment[otherlimb][iden]
                            data["equipment"][limb][0]["stack"]=1
                        else:
                            data["equipment"].pop(limb)
                    elif limb not in ("ammo","backpack"):
                        limbfix=re.sub("[0-9]","",limb)
                        limbers=[arm for arm in armors_by_class if armors_by_class[arm]==limbfix]
                        data["equipment"][limb][0]["chance"]=0.1+0.8*random.random()
                        iden=random.choice(limbers)
                        data["equipment"][limb][0]["id"]=int(iden)
                        data["equipment"][limb][0]["name"]=equipment["armor"][iden]
                        data["equipment"][limb][0]["stack"]=1
            json_file.close()
        with open(filename,'w') as json_file:
            json.dump(data, json_file,indent=4)
damage_randomize()
exp_randomize()
health_randomize()
dur_randomize()
nutr_randomize()
liquidsources_randomize()
weight_randomize()
weapon_randomize()
resis_randomize()
equip_randomize()
        #with open(filename,'w') as json_file:
        #    json.dump(data, json_file,indent=4)
    