import streamlit as st
from graph_builder import create_graph

def print_header():
    st.title("Analysis of Neural Network of the Nematode C. Elegans Vertices Distance")
    st.write("Dataset disponibilized by Mark Newman at:\n"+
        "http://www-personal.umich.edu/~mejn/netdata")

    st.write("This algorithm will calculate the distance between 2 vertices in " +
        "a directed graph that represents the neural network of C. Elegans.")
    st.write("**Note:** there are 2 differents representation for each vertex:" +
        " by label (original) and by index (re-enumerated). Due to " +
        "problems with the labeled enumeration caused by missing vertex associated "+ 
        "with some labels, it's recommended to use the search by index.")

    st.image("https://royalsocietypublishing.org/cms/asset/07403866-d542-4089-a14c-ca5d72f8a973/rstb20140212f01.jpg")


def search_by_label():
    st.header("Search")
    search_option = st.radio("Find path based on:", ("Indexes (recommended)","Labels"))

    if search_option == "Indexes (recommended)":
        st.write("Vertex are in the interval 0-296")
        by_label = False
    else:
        st.write("Vertex are in the interval 1-306 (some aren't in the database)")
        by_label = True

    return by_label

def print_path(graph, start, target, by_label):
    dijkstra = graph.dijkstra(start, target, by_label)

    if dijkstra is None:
        st.write(f"There is no path from {start} to {target}")
        return

    path = dijkstra[0]
    distance = dijkstra[1]
    st.write(f"Distance: {distance}")

    path_str = "Shortest path: "
    for i in range(len(path)-1):
        path_str += f"{path[i]}, "
    path_str += f"{path[-1]}\n"
    st.write(path_str)

def main():
    print_header()
    by_label = search_by_label()

    graph = create_graph()
    src = st.text_input("Start Vertex", help="The vertex where the search will start")
    target = st.text_input("Target Vertex", help="The vertex where the search will end")

    start_button = st.button("Find Path")
    if start_button:
        try:
            src = int(src)
            target = int(target)
            print_path(graph, src, target, by_label)
        except ValueError:
            st.error("Value invalid or empty!")
        except KeyError:
            st.error("One of the vertices is not availabe in the database!")

    st.write()
    st.header("References")
    st.write('''
  J. G. White, E. Southgate, J. N. Thompson, and S. Brenner, "The structure
  of the nervous system of the nematode C. Elegans", Phil. Trans. R. Soc.
  London 314, 1-340 (1986).

  D. J. Watts and S. H. Strogatz, "Collective dynamics of `small-world'
  networks", Nature 393, 440-442 (1998).
  ''')

if __name__ == "__main__":
    main()
