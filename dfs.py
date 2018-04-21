'''
MIT constraint satisfaction problem

'''
class Node:
    def __init__(self, name, domain, vertexes):
        self.vertexes = vertexes
        self.domain = domain
        self.name = name

class Graph(object):
    def __init__(self, domain, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        self.domain = domain
        self.nodes = []
        print graph_dict
        for key in graph_dict:
            self.nodes.append(Node(key, self.domain, graph_dict[key]))


g = {"N": ["T","P","L","C","B"],
     "B": ["N","C"],
     "C": ["B", "N", "P", "L"],
     "P": ["S", "C","N","L"],
     "S": ["P"],
     "L": ["C","P","N","T"],
     "T": ["N","L"]
     }
domain = [1,2,3,4]
graph = Graph(domain, g)

for x in graph.nodes:
    print x.name, x.domain, x.vertexes