class Graph:
    def __init__(self):
        self.number_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        if node not in self.adjacent_list.keys():
            self.adjacent_list[node] = []
            self.number_nodes += 1
        return self

    def add_edge(self, node1, node2):
        if node1 not in self.adjacent_list.keys() or node2 not in self.adjacent_list.keys():
            return False
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)
        return True

    def show_connections(self):
        all_nodes = self.adjacent_list.keys()
        for node in all_nodes:
            node_conn = self.adjacent_list[node]
            connections = ""
            for vertex in node_conn:
                connections += vertex + " "
            print(node + " ---> " + connections)   
    
graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_edge('3','1')
graph.add_edge('3','4')
graph.add_edge('4','2')
graph.add_edge('4','5')
graph.add_edge('1','2')
graph.add_edge('1','0')
graph.add_edge('0','2')
graph.add_edge('6','5')
graph.show_connections()