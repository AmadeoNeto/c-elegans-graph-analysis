from data_analysis import create_graph
import time, random, sys

def time_analysis():
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

def generate_test_cases():
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
    out = ""
    for i in range(297):
        for j in range(297):
            out += f"{i} {j}\n"

    print(out)

if __name__ == "__main__":
    # generate_test_cases()
    time_analysis()
    #generate_all_cases()
