'''Module with the Digraph class'''
from heap import Min_Heap
import math

class Digraph:
    '''Stores a weighted directioned graph represented with a Adjacency List.
    Each list element is represented as a tuple (destiny, weight)'''
    def __init__(self, size = 0):
        self.__adj = []
        self.__labels = dict()
        self.__index = dict()

        for i in range(size):
            self.new_vertex(str(i))

    def new_vertex(self, label):
        index = self.size
        self.__adj.append([])

        self.__labels[index] = label
        self.__index[label] = index

    def edge_between(self,v1,v2,weight):
        '''Creates a weighted directioned edge between v1 and v2'''
        self.get_adjacents(v1).append((v2,weight))

    def get_adjacents(self, v):
        '''Return the vertices adjacents to v'''
        return self.__adj[v]

    def get_label(self,index):
        return self.__labels[index]

    def get_index_by_label(self, label):
        return self.__index[label]

    @property
    def size(self):
        '''The number of vertices in the graph'''
        return len(self.__adj)

    def dijkstra(self,start,target, by_label=False):
        antecessors = [-1 for i in range(self.size)]
        distances = [(math.inf,i) for i in range(self.size)]

        if by_label:
            index_start = self.get_index_by_label(start)
            index_target = self.get_index_by_label(target)
        else:
            index_start = start
            index_target = target

        distances[index_start] = (0,distances[index_start][1])

        open_heap = Min_Heap()
        open_heap.insert(distances[index_start])

        while open_heap.size != 0:
            dis_ver = open_heap.extract_min()
            v1 = dis_ver[1]
            adjacents = self.get_adjacents(v1)

            for i in range(len(adjacents)):
                edge = adjacents[i]
                edge_weight = edge[1]
                v2 = edge[0]
                alt = distances[v1][0] + edge_weight

                if distances[v2][0] > alt:
                    antecessors[v2] = v1

                    distances[v2] = (alt, v2)
                    open_heap.insert(distances[v2])

        if antecessors[index_target] == -1:
            # print(antecessors)
            return

        path = [target]
        aux = index_target

        while aux != index_start:
            if aux == -1:
                break
            aux = antecessors[aux]

            if by_label:
                path.append(self.get_label(aux))
            else:
                path.append(aux)

        path.reverse()
        distance = distances[index_target][0]

        return (path, distance)

    def __str__(self):
        out = ""
        for i in range(self.size):
            out += f"{i}|\"{self.get_label(i)}\": "
            out += str(self.get_adjacents(i))
            out += "\n"

        return out

if __name__ == "__main__":
    g = Digraph(7)
    # g.edge_between(4,2,1)
    # g.edge_between(5,1,3)
    # g.edge_between(2,1,20)
    # g.edge_between(0,6,9)
    # g.edge_between(4,5,30)
    # g.edge_between(4,0,1)
    # g.edge_between(6,1,1)
    # print(g)
    # g.dijkstra(4,1)
