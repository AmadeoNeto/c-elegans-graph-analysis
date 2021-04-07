'''Module responsible for reading the database'''
import os
from graph import Digraph

def get_file_path(dir_path:str):
    return "".join(list(os.getcwd())) + dir_path

def get_dataset():
    datapath = get_file_path("\\celegansneural\\celegansneural.gml")
    dataset = open(datapath)
    return dataset

def insert_vertex(graph,dataset):
    dataset.readline() # ignore "["
    dataset.readline() # ignore "id" (its already computed)
    label_line = dataset.readline() # gets the label line
    dataset.readline() # ignore "]"

    label = int(label_line[11:-2]) # extract the label from the line
    graph.new_vertex(label) # insert a vertex with the label in the graph

def insert_edge(graph, dataset):
    dataset.readline() # ignore "["
    src_line = dataset.readline()
    target_line = dataset.readline()
    weight_line = dataset.readline()
    dataset.readline() # ignore "]"

    src = int(src_line[10:-1])
    target = int(target_line[10:-1])
    weight = int(weight_line[9:-1])
    graph.edge_between(src, target, weight)

def create_graph():
    graph = Digraph()
    dataset = get_dataset()
    for line in dataset:
        if line == "  node\n":
            insert_vertex(graph,dataset)
        if line == "  edge\n":
            insert_edge(graph,dataset)


    dataset.close()
    return graph

def test():
    g = create_graph()
    print(g)

if __name__ == "__main__":
    test()
