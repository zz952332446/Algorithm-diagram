# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 16:17:33 2020

@author: hhyyz
"""
####graph
graph={}
graph["start"]={}
graph["start"]["a"]=6
graph["start"]["b"]=2
graph["a"]={}
graph["a"]["fin"]=1
graph["b"]={}
graph["b"]["a"]=3
graph["b"]["fin"]=5
graph["fin"]={}
#print(graph)  #{'start': {'a': 6, 'b': 2}, 'a': {'fin': 1}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}
#print(graph["start"].keys()) #dict_keys(['a', 'b'])获取邻居
#print(graph["start"]["a"])  #6 权值

####costs
infinity=float("inf")
costs={}
costs["a"]=6
costs["b"]=2
costs["fin"]=infinity


####parents
parents={}
parents["a"]="start"
parents["b"]="start"
parents["fin"]=None

processed=[]#记录处理过的结点

def find_lowest_cost_node(costs):
    lowest_cost=float("inf")
    lowest_cost_node=None
    for i in costs:
        cost=costs[i]
        if cost<lowest_cost and i not in processed:##!后一个条件！
            lowest_cost=costs[i]
            lowest_cost_node=i
    return lowest_cost_node




node=find_lowest_cost_node(costs)   #未处理的结点中找到开销最小的
while node is not None:
    neighbor=graph[node]
    cost=costs[node]
    for n in neighbor.keys():        #遍历开销最小结点的所有结点
        new_cost=cost+neighbor[n]    #!neighbor[n]!
        if costs[n]>new_cost:
            costs[n]=new_cost
            parents[n]=node
            
    processed.append(node)          #!这句的缩进
    node=find_lowest_cost_node(costs)  ##!costs!

print(parents)
print(costs)

###反向打印
print("fin"+'-',end='')
i=parents["fin"]
print(i+'-',end='')
while parents[i] != "start":
    i=parents[i]
    print(i+'-',end='')
print("start")


###正向打印
t=list(parents.keys()) [list (parents.values()).index ('start')]
print("start"+'-',end='')
print(t+'-',end='')
while t!="fin":
    t=list(parents.keys()) [list (parents.values()).index (t)]
    print(t+'-',end='')

