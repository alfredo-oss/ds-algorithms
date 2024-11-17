"""
Design a directed Graph class that should support a structure like:
 [node] -> [node]
             /
           [node] - [node] 
So, the graph, needs to handle nodes. Which could be supported on a 
separate class/or it could be more easily represented as a key-value 
pair on a hashmap

* the graph should support the fact of adding an edge, where the edge
  has a "source" and a "destination".
    - "source" could be new or already existing value. same goes for
      destination. if it hasnt been created already.
* remove edge would look at a key and remove it alongside its neighbors. could be done with a .remove operation for a hashmap key
    - removing its a bit more complicated because it would be removing
      just an edge/link, not the entire node.
      -> lets double click on this:
         first we found the "src" element on the adjacency list: OK
         now, how do we remove the element that is the neighbor:
         we could instead of using an array using a deque:
         if we use a deque: (i dont know if you can index deques [lets assume yes])
            - we could iterate through the deque (because queues are iterable) find the element,
            - hold the left most element in a temp variable
            - swap it with the left most element:
            - popleft from the queue
            - append the left most element back on the queue, because the order of the neighbors doesnt
              really matter. 
            - EDGE CASE: 
                if the lenght of the queue is 1 and the element is present, then there is no need to perform the swap and you would just popleft from the queue.
                it would work because length is one and you end up popping    
* hasPath could be performed with bfs algorithm more efficiently.
"""
from collections import deque

class Graph:
    
    def __init__(self):
        self.adjlist = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjlist:
            self.adjlist[src] = deque()
        if dst not in self.adjlist:
            self.adjlist[dst] = deque()
        self.adjlist[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjlist and dst not in self.adjlist[src]:
            return False
        self.adjlist[src].remove(dst)    
        return True
                

    def hasPath(self, src: int, dst: int) -> bool:
            queue = deque()
            visit = set()
            queue.append(src)
            visit.add(src)
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    if curr == dst:
                        return True
                    for neighbor in self.adjlist[curr]:
                        if neighbor not in visit:
                            queue.append(neighbor)
                            visit.add(neighbor)
            return False
