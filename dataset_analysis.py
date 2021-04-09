from graph_builder import create_graph, get_dataset
import time, random, sys

def time_analysis():
    ''' Receives test cases from the console and make analysis
    of it execution time
    '''
    graph = create_graph()
    times = []
    out = ""
    counter = 1

    for line in sys.stdin:
        line = line[:-1].split()

        if len(line) == 0:
            continue

        src = int(line[0])
        target = int(line[1])

        start_time = time.time()

        try:
            graph.dijkstra(src, target)
        except KeyError:
            out += f"Execution {counter+1} ({src} -> {target}): key not found\n"
            continue

        execution_time = time.time() - start_time
        times.append(execution_time)
        out += f"Execution {counter} ({src} -> {target}): {execution_time*1000}ms\n"
        counter += 1

    print("- Time Analysis -")
    print(f"Total time: {sum(times)}s")
    print(f"Lowest time: {min(times)*1000}ms")
    print(f"Biggest Time: {max(times)*1000}ms")
    media = sum(times)/len(times) * 1000
    print(f"Media: {media}ms\n")

    print("Cases tested:")
    print(out)

def generate_label_test_cases():
    '''Generate random pairs of numbers to be used in dijkstra by label'''
    out = ""
    for i in range(1,303):
        picked = []
        for _ in range(150):
            target = random.randint(0,302)
            while target in picked:
                target = random.randint(0,302)
            picked.append(target)
            out += f"{i} {target}\n"

    print(out)

def generate_all_cases():
    '''Generate all possible test cases by index for dijkstra'''
    out = ""
    for i in range(297):
        for j in range(297):
            out += f"{i} {j}\n"

    print(out)

def farthest_path():
    '''Receives test cases from console and print the path with the
     biggest distance and, below, the distance of each path'''
    graph = create_graph()
    distances = []
    out = ""

    for line in sys.stdin:
        line = line[:-1].split()

        if len(line) == 0:
            continue

        src = int(line[0])
        target = int(line[1])

        dij = graph.dijkstra(src, target)
        if dij is not None:
            dis = dij[1]
            distances.append(dis)
            out += f"Distance {src}->{target}: {dis}\n"

    print(f"The longest path has length: {max(distances)}\n")
    print(out)

def graph_elements_count():
    '''Print the number of nodes and edges aswell as the number of distint weights of edges on the graph'''
    nodes = 0    # Number of nodes in the graph
    edges = 0    # Number of edges in the graph
    values = []  # List with all weight values in the graph

    dataset = get_dataset()

    # Start the count, it can be optimized but there is no need
    for line in dataset:
        line = line[:-1]
        if line == "  node":
            nodes += 1
        elif line == "  edge":
            edges += 1
        elif "value" in line:
            weight = line.split()[1]
            if weight not in values:
                values.append(weight)

    dataset.close()

    # Print the results
    print("Nodes:", nodes)
    print("Edges:", edges)
    print("Unique Weights:", len(values))

if __name__ == "__main__":
    # generate_test_cases()
    #time_analysis()
    #generate_all_cases()
    #graph_elements_count()
    farthest_path()
