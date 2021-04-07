'''Module responsible for reading the database'''
from graph import Digraph
import sys, os

def get_file_path(dir_path:str):
    return "".join(list(os.getcwd())) + dir_path

def get_dataset():
    datapath = get_file_path("\\celegansneural\\celegansneural.gml")
    dataset = open(datapath)
    return dataset

def graph_elements_count():
    '''Print the number of nodes and edges aswell as the number of distint weights of edges on the graph'''
    nodes = 0    # Number of nodes in the graph
    edges = 0    # Number of edges in the graph
    values = []  # List with all weight values in the graph

    # Start the count, can be optimized but there is no need
    for line in sys.stdin:
        line = line[:-1]
        if line == "  node":
            nodes += 1
        elif line == "  edge":
            edges += 1
        elif "value" in line:
            weight = line.split()[1]
            if weight not in values:
                values.append(weight)

    # Print the results
    print("Nodes:", nodes)
    print("Edges:", edges)
    print("Unique Weights:", len(values))

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
    # print(g.dijkstra(1,92,True))
    # print(g.dijkstra(0,7))

if __name__ == "__main__":
    test()
