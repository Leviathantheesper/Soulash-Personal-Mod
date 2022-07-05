# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 17:44:45 2022

@author: dcmol
"""

import os
import re
#stats: "exp", "durability","nutrition"
def scalestat(stat_name,var):
    """
    Adds a multiplier to a given characteristic.
    Parameters
    ----------
    stat_name : string
        The name of the stat to be modified.
        Examples:
        "exp", "durability","nutrition","dmg_min","dmg_max"
    var : multiplier
        Number that will be multiplied to the stat.
    """
    list_dir=os.listdir()
    list_dir.remove('Modif.py')
    counter=1
    for filename in list_dir:
        print(str(counter)+' of '+str(len(list_dir)))
        counter+=1
        json=''
        rewrite=True
        with open(filename,'r+') as file:
            json=file.read()
            da_stat="\""+stat_name+"\""
            pattern=da_stat+": [0-9]+"
            reg=re.search(pattern, json)
            try:
                line=reg.group(0)
                statstring=re.search("[0-9]+", line).group(0)
                stat_number=int(var*int(statstring))
                new_line=da_stat+": "+str(stat_number)
                json=json.replace(line,new_line)
            except: # pylint: disable=bare-except
                print("Failed to mod ",stat_name," in ",filename)
                rewrite=False
            file.close()
        if rewrite:
            with open(filename,'w') as file:
                file.write(json)
                file.close()
def scaledamage(var):
    """
    Scales the damage of all weapons.
    Parameters
    ----------
    var : multiplier
        Number that will be multiplied to the damage.
    """
    scalestat("dmg_max",var)
    scalestat("dmg_min",var)
