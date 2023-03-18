from problem import SingleFoodSearchProblem 
from fringes import *
class SearchStrategy:
    def search(self, g: SingleFoodSearchProblem, src: tuple, dst: tuple) -> tuple:
        expanded = [] # list of expanded vertices in the traversal order
        path = [] # path from src to dst
        return expanded, path
    def get_path(self, src : tuple , dst: tuple , parents : dict)-> list : 
        path = []
        x = dst 
        while x != -1 : 
            path.append(x)
            x = parents[x]
        path.reverse()
        return path 
    def get_directions(self, locations):
        directions = []
        for i in range(1, len(locations)):
            curr = locations[i]
            prev = locations[i-1]
            if curr[0] > prev[0]:
                directions.append("S")
            elif curr[0] < prev[0]:
                directions.append("N")
            elif curr[1] > prev[1]:
                directions.append("E")
            elif curr[1] < prev[1]:
                directions.append("W")
        directions.append("Stop")
        return directions
class BFS(SearchStrategy):
    def search(self, g: SingleFoodSearchProblem, src: tuple , dst: tuple) -> tuple:
        expanded = [] # list of expanded vertices in the traversal order
        path = [] # path from src to dst
        if src == dst : 
            expanded = []
            path = [src]
            return self.get_directions(path)
        q= Queue()
        q.enqueue(src)
        expanded =[]
        parents = dict()
        parents[src] = -1 
        
        while not q.is_empty() : 
            cur = q.dequeue()
            expanded.append(cur)
            successors = g.get_successors(cur) 
            for(v,w) in  successors : 
                if v not in expanded and not q.contain(v):
                    if v == dst : 
                        parents[v] = cur 
                        path = self.get_path(src ,dst,parents)
                        direction =  self.get_directions(path)
                        return direction ,path
                    parents[v] = cur 
                    q.enqueue(v)                
class DFS(SearchStrategy):
    def search(self, g: SingleFoodSearchProblem, src: tuple , dst: tuple) -> tuple:
        expanded = [] # list of expanded vertices in the traversal order
        path = [] # path from src to dst
        if src == dst : 
            expanded = []
            path = [src]
            return self.get_directions(path)
        q= Stack()
        q.push(src)
        expanded =[]
        parents = dict()
        parents[src] = -1 
        
        while not q.is_empty() : 
            cur = q.pop()
            expanded.append(cur)
            successors = g.get_successors(cur) 
            for(v,w) in  successors : 
                if v not in expanded and not q.contain(v):
                    if v == dst : 
                        parents[v] = cur 
                        path = self.get_path(src ,dst,parents)
                        direction =  self.get_directions(path)
                        return direction ,path
                    parents[v] = cur 
                    q.push(v)           

pac_man = SingleFoodSearchProblem("pacman_single03.txt")

bfs = BFS()
dfs = DFS()
# ucs = UCS()


# for stg in [bfs, dfs]:
#   print(stg)
#   direction, path = stg.search(pac_man, pac_man.get_start_state(), pac_man.get_goal_state())
#   print(path)
#   print(direction)
direction, path = dfs.search(pac_man, pac_man.get_start_state(), pac_man.get_goal_state())
pac_man.animate(direction)