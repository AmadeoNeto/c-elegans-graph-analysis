from data_analysis import create_graph

def print_header():
    print("Analysis of Neural network of the nematode C. Elegans vertices distance")
    print("Disponibilized by Mark Newman at: " +
        "http://www-personal.umich.edu/~mejn/netdata/celegansneural.zip\n")

    print("This algorithm will calculate the distance between 2 vertices in " +
     "a directed graph that represents the neural network of C. Elegans.")

    print("Note: there are 2 differents representation for each vertex, " +
     "by label(original) and by index(renumbered).\n")

def search_by_label():
    by_label = False

    print("Do you wanna execute this algorithm based on labels or indexes?")
    print("[1] By indexes (recommended)\n[2] By labels")
    option = input()
    if "1" in option:
        by_label = False
    elif "2" in option:
        by_label = True
    else:
        print("Invalid option")
        quit()

    return by_label

def print_path(graph, start, target, by_label):
    dijkstra = graph.dijkstra(start, target, by_label)

    if dijkstra is None:
        print(f"There is no path from {start} to {target}")
        return

    path = dijkstra[0]
    distance = dijkstra[1]

    out = ""
    out += f"Distance: {distance}\n"
    out += "Shortest path: "

    for i in range(len(path)-1):
        out += f"{path[i]}, "
    out += f"{path[-1]}\n"

    print(out)

def main():
    print_header()
    by_label = search_by_label()

    if by_label:
        print("Vertex are in ther interval 1-306 (some aren't in the database)")
    else:
        print("Vertex are in ther interval 0-296")

    graph = create_graph()
    print("Start Vertex: ", end="")
    src = int(input())
    print("Target Vertex: ", end="")
    target = int(input())
    print()

    try:
        print_path(graph, src, target, by_label)
    except KeyError:
        print("ERROR: One of the vertices is not availabe in the database!")

if __name__ == "__main__":
    main()
