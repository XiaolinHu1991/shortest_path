import numpy as np
import copy

class Dijkstra(object):
    def __init__(self, locations):
        self.locations = locations
        self.Q = {}
    
    
    def _initialize(self, ):
        for node in self.locations.all_nodes:
            node.previous = None
            
            if node.is_start:
                node.distance_to_start = 0
            else:
                node.distance_to_start = np.inf
            
            self.Q[node.name] = node.distance_to_start
    
        
    def _calculate_shortest_path(self, ):        
        while self.Q != {}:
            for name in self.Q:
                node = self.locations.find_node_by_name(name)
                self.Q[name] = node.distance_to_start
            
            u_name = min(self.Q, key=self.Q.get)
            u = self.locations.find_node_by_name(u_name)
            
            del self.Q[u_name]
            
            for neighbor_name in u.neighbors:
                neighbor = self.locations.find_node_by_name(neighbor_name)
                alternative_length = u.distance_to_start + u.neighbors[neighbor_name]
                
                if alternative_length < neighbor.distance_to_start:
                    neighbor.distance_to_start = alternative_length
                    neighbor.previous = u_name
                
    def find_shortest_path(self, ):
        """
        Returns
        -------
        path : list
            List of nodes from start to end
        distance : float
            Minimum distance along shortest path
        """
        
        self._initialize()
        self._calculate_shortest_path()
        
        path = []
        node = self.locations.find_end()
        
        distance = node.distance_to_start
        
        while not node.is_start:
            path.append(node.name)
            node = self.locations.find_node_by_name(node.previous)
        
        path.append(node.name)
        
        path.reverse()
        
        return path, distance
            
                
                
                
                
                
                
                