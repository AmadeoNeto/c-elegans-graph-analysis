from data_analysis import create_graph

def print_header():
    print("Analysis of Neural network of the nematode C. Elegans vertices distance")
    print("Disponibilized by Mark Newman at: " +
        "http://www-personal.umich.edu/~mejn/netdata/celegansneural.zip\n")

    print("This algorithm will calculate the distance between 2 vertices in " +
     "a directed graph that represents the neural network of C. Elegans.")
    print("Each vertex represents a point in the neural network " +
     "and is numbered in the range 1-302.")
    print("Note: there are 2 differents representation for each vertex, " +
     "by label(original) and by index(renumbered). This algorithm receives "+
     "the vertex in the original enumeration.\n")

def main():
    print_header()
    graph = create_graph()
    print("Start Vertex: ", end="")
    v1 = int(input())
    print("Target Vertex: ", end="")
    v2 = int(input())
    print()
    graph.dijkstra(v1,v2)

if __name__ == "__main__":
    main()
