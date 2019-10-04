from base_classes import Node, Map

locations = Map()
locations.add_node(Node("Frankfurt", 
                        {"Mannheim": 85, "Würzburg": 217, "Kassel": 173},
                        "start"))
locations.add_node(Node("Mannheim", {"Karlsruhe": 80}))
locations.add_node(Node("Würzburg", {"Erfurt": 186, "Nürnberg": 103}))
locations.add_node(Node("Kassel", {"München": 502}))
locations.add_node(Node("Karlsruhe", {"Augsburg": 250}))
locations.add_node(Node("Erfurt", {}))
locations.add_node(Node("Nürnberg", {"München": 167, "Stuttgart": 183}))
locations.add_node(Node("Augsburg", {"München": 84}))
locations.add_node(Node("Stuttgart", {}))
locations.add_node(Node("München", {}, "end"))

from dijkstra import Dijkstra
model = Dijkstra(locations)
path, distance = model.find_shortest_path()