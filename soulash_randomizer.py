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
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        json=''
        rewrite=True
        with open(filename,'r+') as file:
            json=file.read()
            var=10*random.random()
            stat_name="dmg_max"
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+"
            reg=re.search(pattern, json)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                new_line=re.sub("[0-9]+",str(stat_number),line)
                json=json.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            var=var*random.random()
            stat_name="dmg_min"
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+"
            reg=re.search(pattern, json)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                new_line=re.sub("[0-9]+",str(stat_number),line)
                json=json.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(json)
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
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        json=''
        rewrite=True
        with open(filename,'r+') as file:
            json=file.read()
            var=0.5+4.5*random.random()
            stat_name="exp"
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+"
            reg=re.search(pattern, json)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                new_line=re.sub("[0-9]+",str(stat_number),line)
                json=json.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(json)
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
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        json=''
        rewrite=True
        with open(filename,'r+') as file:
            json=file.read()
            var=0.5+4.5*random.random()
            stat_name="durability"
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+"
            reg=re.search(pattern, json)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                new_line=re.sub("[0-9]+",str(stat_number),line)
                json=json.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(json)
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
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        json=''
        rewrite=True
        with open(filename,'r+') as file:
            json=file.read()
            var=0.5+1.5*random.random()
            stat_name="nutrition"
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+"
            reg=re.search(pattern, json)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                new_line=re.sub("[0-9]+",str(stat_number),line)
                json=json.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(json)
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
    print(list_dir)
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        json=''
        rewrite=True
        with open(filename,'r+') as file:
            json=file.read()
            var=0.5+1.5*random.random()
            stat_name="liquid_source"
            da_stat="\""+stat_name+"\""
            sub_stat_name="limit"
            da_sub_stat="\""+sub_stat_name+"\""
            pattern=da_stat+":\s[{]\n(.*\n)*\t*"+da_sub_stat+": [0-9]+"
            reg=re.search(pattern, json)
            try:
                lines=reg.group(0)
                splines=lines.splitlines()
                line=splines[len(splines)-1]
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                line=re.sub("[0-9]+",str(stat_number),line)
                splines[len(splines)-1]=line
                new_lines="\n".join(splines)
                print(json)
                json=json.replace(lines,new_lines)
                print(json)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(json)
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
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        json=''
        rewrite=True
        with open(filename,'r+') as file:
            json=file.read()
            var=0.1+1.9*random.random()
            stat_name="weight"
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+"
            reg=re.search(pattern, json)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                new_line=re.sub("[0-9]+",str(stat_number),line)
                json=json.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(json)
                file.close()