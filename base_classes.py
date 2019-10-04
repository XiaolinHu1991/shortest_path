import numpy as np

class Map(object):
    def __init__(self, ):
        self.all_nodes = []
        self.sorted_nodes = []
    
    
    def add_node(self, node):
        self.all_nodes.append(node)
    
    
    def find_start(self, ):
        for node in self.all_nodes:
            if node.is_start:
                return node
    
    
    def find_end(self, ):
        for node in self.all_nodes:
            if node.is_end:
                return node
    
    def find_node_by_name(self, name):
        for node in self.all_nodes:
            if node.name == name:
                return node


class Node(object):
    def __init__(self, name="", neighbors={}, flag=""):
        """
        Parameters
        ----------
        name : string
            Name of the location
        neighbors : dictionary
            Keys: names; values: distance from current node to neighbor
        flag : string
            Possible values: ""; "start", "end
        """
        self.name = name
        self.neighbors = neighbors
        self._determine_flag(flag)
        self.previous = None
        
        
    def _determine_flag(self, flag):
        self.is_start = False
        self.is_end = False
        if flag == "start":
            self.is_start = True
            self.distance_to_start = 0
        else:
            self.distance_to_start = np.inf
            if flag == "end":
                self.is_end = True
        