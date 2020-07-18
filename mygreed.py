# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 08:42:25 2020

@author: hhyyz
"""

states_needed=set(["mt","wa","id","nv","ut","or","ca","az"])
stations={}
stations["kone"]=set(["id","nv","ut"])
stations["ktwo"]=set(["id","wa","mt"])
stations["kthree"]=set(["or","nv","ca"])
stations["kfour"]=set(["nv","ot"])
stations["kfive"]=set(["ca","az"])

final_stations=set()

while states_needed:
    best_station=None
    states_covered=set()
    for station,states_for_station in stations.items():  #dict_items([('kone', {'id', 'nv', 'ut'}), ('ktwo', {'wa', 'id', 'mt'}), ('kthree', {'or', 'ca', 'nv'}), ('kfour', {'ot', 'nv'}), ('kfive', {'ca', 'az'})])
        covered=states_needed & states_for_station
        if len(covered)>len(states_covered):
            best_station=station
            states_covered=covered
    final_stations.add(best_station)#先add在后
   #print(final_stations)
    states_needed-=states_covered
        
print(final_stations)
    