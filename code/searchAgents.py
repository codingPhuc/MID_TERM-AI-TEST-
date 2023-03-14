from problem import SingleFoodSearchProblem 
from fringes import Queue 
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
class BFS(SearchStrategy):
    def search(self, g: SingleFoodSearchProblem, src: tuple , dst: tuple) -> tuple:
        expanded = [] # list of expanded vertices in the traversal order
        path = [] # path from src to dst
        if src == dst : 
            expanded = []
            path = [src]
            return expanded , path 
        q= Queue()
        q.enqueue(src)
        expanded =[]
        parents = dict()
        parents[src] = -1 
        
        while not q.is_empty() : 
            cur = q.dequeue()
            expanded.append(cur)
            print(cur)
            successors = g.get_successors(cur[0]) 
            for(v,d ,w) in  successors : 
                if (v,d) not in expanded and not q.contain((v,d)):
                    if v == dst[0] : 
                        parents[(v,d)] = cur 
                        path = self.get_path(src ,dst,parents)
                    parents[(v,d)] = cur 
                    q.enqueue((v,d))
        return expanded , path             


pac_man = SingleFoodSearchProblem("pacman_single01.txt")
bfs  = BFS()

print(bfs)
destination = (pac_man.get_goal_state(),"Stop")
start = ( pac_man.get_start_state(),"Stop")
expanded, path = bfs.search(pac_man, start, destination)
print(path)
