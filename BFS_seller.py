# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:11:58 2020

@author: hhyyz
"""


def person_is_seller(name):
    return name[-1]=='y'

def mysearch(name):
    search_queue=deque()
    searched=[] #搜索过的
    obj=[]
    search_queue+=graph[name] #search_queue是数组
    while search_queue:
        person=search_queue.popleft()
        nodes=graph[person]               
                
        if person not in searched:
            if person_is_seller(person):
                print(person+" is a mango seller")
                obj.append(person)
                searched.append(person)###########?书上没有这句
            
            else:
                search_queue+=graph[person]
                searched.append(person)
                
        for i in nodes:
            if i not in searched:
                if i not in parent:######重要！因为这是广度优先，最先更新parent的会比后来更新的路径更短
                    parent[i]=person

               
    print(searched)
    return parent,obj

from collections import deque
graph={}

graph["hyz"]=["alice","bob","claire"]
graph["alice"]=["lala"]
graph["lala"]=["peggy"]
graph["bob"]=["anuj","peggy"]
graph["claire"]=["jonny","thom"]
graph["anuj"]=[]
graph["peggy"]=[]
graph["thom"]=["jonny"]
graph["jonny"]=[]
parent={}
parent["alice"]="hyz"
parent["bob"]="hyz"
parent["claire"]="hyz"
parent["hyz"]=None
myparent,myobj=mysearch("hyz") 

for i in myobj:
    while i is not None:
        if i!="hyz":
            print(i+'-',end='')  # D -> B -> A
            i = myparent[i]  
        else:
            print(i)
            i = myparent[i]  ##这句不能少
                
    