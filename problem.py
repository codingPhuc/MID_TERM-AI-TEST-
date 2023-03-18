import sys
import time
import os
class SingleFoodSearchProblem:
    def __init__(self, maze_file):
        self.maze = self.read_maze(maze_file)
        self.start_state = self.get_start_state()
        self.goal_state = self.get_goal_state()
        
    def read_maze(self, maze_file):# reading the maze file 
        with open(maze_file, 'r') as f:
            maze = [line.strip() for line in f]
        return maze
    
    def get_start_state(self):# the beginning state that pacman start at 
        for i in range(len(self.maze)):
            if 'P' in self.maze[i]:
                return (i, self.maze[i].index('P'))
        return None
    
    def get_goal_state(self): # the goal that pack man is trying to get 
        for i in range(len(self.maze)):
            if '.' in self.maze[i]:
                return (i, self.maze[i].index('.'))
        return None
    
    def get_successors(self, state):# the way that pack_man move form a given postion
        successors = []
        x, y = state
        if x > 0 and self.maze[x-1][y] != '%':
            successors.append(((x-1, y), 1))
        if x < len(self.maze) - 1 and self.maze[x+1][y] != '%':
            successors.append(((x+1, y), 1))
        if y > 0 and self.maze[x][y-1] != '%':
            successors.append(((x, y-1), 1))
        if y < len(self.maze[0]) - 1 and self.maze[x][y+1] != '%':
            successors.append(((x, y+1), 1))   
        return successors
    
    def is_goal_state(self, state):# check if it is the goal state 
        return state == self.goal_state
    
    def get_path_cost(self, cost_so_far, current_state, action, next_state):
        return cost_so_far + 1
    
    def print_maze(self):
        for line in self.maze:
            print(line)
    def Tranlate_action(self, state, action):
        i, j = state
        if action == 'N':
            return (i-1, j)
        elif action == 'S':
            return (i+1, j)
        elif action == 'W':
            return (i, j-1)
        elif action == 'E':
            return (i, j+1)
        elif action == 'Stop':
            return 
        else:
            raise ValueError(f'Unknown action {action}')

    def animate(self, direction):
        current_state = self.start_state
        
        actions = []
        now = self.get_start_state() 
        for i in direction : 
            next = self.Tranlate_action(now,i)
            actions.append(next)
            now= next 
        while actions:
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(len(self.maze)):
                line = ''
                for j in range(len(self.maze[i])):
                    if (i, j) == current_state:
                        line += 'P'
                    elif (i, j) == self.goal_state:
                        line += '.'
                    else:
                        line += self.maze[i][j]
                print(line)
            print('Press Enter to continue...')
            input()
            next_state = actions.pop(0)
            current_state = next_state
    # def animate(self, actions):
    #     current_state = self.start_state
    #     while actions:
    #         os.system('cls' if os.name == 'nt' else 'clear')
    #         for i in range(len(self.maze)):
    #             line = ''
    #             for j in range(len(self.maze[i])):
    #                 if (i, j) == current_state:
    #                     line += 'P'
    #                 elif (i, j) == self.goal_state:
    #                     line += '.'
    #                 else:
    #                     line += self.maze[i][j]
    #             print(line)
    #         print('Press Enter to continue...')
    #         input()
    #         next_state = actions.pop(0)
    #         current_state = next_state
    
