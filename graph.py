'''Module with the Digraph class'''
from heap import Min_Heap
import math

class Digraph:
    '''Stores a weighted directioned graph represented with a Adjacency List.
    Each list element is represented as a tuple (destiny, weight)'''
    def __init__(self):
        self.__adj = []  # Adjacency list
        self.__labels = dict() # Dict: index -> label
        self.__index = dict() # Dict: label -> index

    def new_vertex(self, label):
        '''Create a new vertex with a given label'''
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
        '''Returns the label corresponding to the index'''
        return self.__labels[index]

    def get_index_by_label(self, label):
        '''Returns the index corresponding to the label'''
        return self.__index[label]

    @property
    def size(self):
        '''The number of vertices in the graph'''
        return len(self.__adj)

    def dijkstra(self,start,target, by_label=False):
        '''Returns a tuple (shortest_path, distance) where the shortest path is a list.

        Parameters
        ----------
        start : int
            The vertex where the path will start
        target : int
            The vertex where the path should end
        by_label : bool, optional
            The search should be by the label? (default is False)
        '''
        antecessors = [-1 for i in range(self.size)]
        distances = [(math.inf,i) for i in range(self.size)]

        if by_label:
            index_start = self.get_index_by_label(start)
            index_target = self.get_index_by_label(target)
        else:
            index_start = start
            index_target = target

        distances[index_start] = (0, distances[index_start][1])

        prior_queue = Min_Heap()
        prior_queue.insert(distances[index_start])

        while prior_queue.size != 0:
            popped = prior_queue.extract_min()
            v1 = popped[1]
            adjacents = self.get_adjacents(v1)

            for i in range(len(adjacents)):
                edge = adjacents[i]
                edge_weight = edge[1]
                v2 = edge[0]
                alt = distances[v1][0] + edge_weight

                if distances[v2][0] > alt:
                    antecessors[v2] = v1

                    distances[v2] = (alt, v2)
                    prior_queue.insert(distances[v2])

        if antecessors[index_target] == -1:
            # The target could not be reached
            return None

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
