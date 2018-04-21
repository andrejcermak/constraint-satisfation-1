'''
MIT constraint satisfaction problem

'''
class Node:
    def __init__(self, domain, constraints, name):
        self.constraints = constraints
        self.domain = domain
        self.assigned_value = None
        self.name = name
        self.free = []
        for i in range(len(domain)):
            self.free.append(True)

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
        self.nodes = {}
        print graph_dict
        for key in graph_dict:
            self.nodes[key]=(Node(self.domain, graph_dict[key], key))

    def dfs(self):
        self.nodes['T'].domain = [1]
        self.nodes['T'].assigned_value = 1
        order1 = ["T","N","B","C", "P","S","L"]
        order = ["T","L","B","C", "S","P","N"]
        it = 0
        x = 0
        while it<len(order):

            node = self.nodes[order[it]]
            # backtracking
            if node.assigned_value is not None and not it == 0:
                start = node.assigned_value
                node.assigned_value = None

                # find next possible value
                for i in range(start, len(node.free)):
                    if node.free[i]:
                        node.assigned_value = i + 1
                        break
                print "backtracking end ", node.name, node.assigned_value

            else:
                # cross out all non-possible values for current node
                for const in node.constraints:
                    if self.nodes[const].assigned_value is not None:
                        node.free[self.nodes[const].assigned_value-1] = False

                # find lowest possible value
                for i in range(len(node.free)):
                    if node.free[i]:
                        node.assigned_value = i+1
                        break
                print node.name, node.assigned_value

            # no possible value, backtrack
            if node.assigned_value is None:
                for i in range(len(node.free)):
                    node.free[i] = True
                it -= 1

            else:
                it += 1

g = {"N": ["T","P","L","C","B"],
     "B": ["N","C"],
     "C": ["B", "N", "P", "L"],
     "P": ["S", "C","N","L"],
     "S": ["P"],
     "L": ["C","P","N","T"],
     "T": ["N","L"]
     }
g1 = {"N": ["T","P","L","C","B","S"],
     "B": ["N","C"],
     "C": ["B", "N", "P", "L","T","S"],
     "P": ["S", "C","N","L","T"],
     "S": ["P","N","C"],
     "L": ["C","P","N","T"],
     "T": ["N","L","C","P"]
     }
domain = [1,2,3,4]
graph = Graph(domain, g1)
graph.dfs()
for name,node in graph.nodes.iteritems():
    print name,node.assigned_value,node.domain, node.constraints,  node.free
