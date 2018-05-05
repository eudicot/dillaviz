import numpy as np
import pandas as pd
import holoviews as hv
import networkx as nx
import json
hv.extension('bokeh')
from bokeh.io import save, output_file, show


#Open Json Files With JDilla connections
with open('rels.json') as fp:
    songs = json.load(fp)


#Create Edge List
edgeList = []
for edge in songs:
    connect = ()
    for k, v in edge.items():
        connect = connect + (v,)
    edgeList.append(connect)


#Create empty graph
dillaGraph = nx.Graph()

numNodes = 0

#Add edges to graph
for entry in edgeList:
    i = 0 
    j = 1
    dillaGraph.add_edge(entry[i],entry[j])
    numNodes += 1


#For Display Purposes
padding = dict(x=(-1.2, 1.2), y=(-1.2, 1.2))




#Create hoverable Graph

print(numNodes)
node_labels = ['Test']*(numNodes+1)
node_info = hv.Dataset(node_labels, vdims='Label')

dillaGraph = hv.Graph.from_networkx(dillaGraph, nx.layout.spring_layout).redim.range(**padding)
dillaGraph = hv.Graph((dillaGraph, kdims = ['test']), label = 'JDilla Sampled Song Network Graph').redim.range(**padding)






#For exportation Purposes
renderer = hv.renderer('bokeh')
dillaGraph = renderer.get_plot(dillaGraph).state
show(dillaGraph)
