import heapq 
import random
import time

import tkinter as tk


class State:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.g_score = float('inf')
        self.f_score = float('inf')
        self.parent = None

    def __lt__(self, other):
        return self.f_score < other.f_score


class MazeSolver:
    def __init__(self, size, obstacle_percentage):
        self.size = size
        self.obstacle_percentage = obstacle_percentage
        self.grid = self.generate_grid()
        self.start_state = State(0, 0)
        self.goal_state = State(size - 1, size - 1)

    def generate_grid(self):
        grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        num_obstacles = int((self.obstacle_percentage / 100) * self.size ** 2)
        obstacles = random.sample(range(self.size ** 2), num_obstacles)
        
        # Set start state and goal state grids
        grid[0][0] = "start"  # Red
        grid[self.size - 1][self.size - 1] = "goal"  # Blue
        
        # Place obstacles randomly, avoiding start and goal state positions
        for obstacle in obstacles:
            row = obstacle // self.size
            col = obstacle % self.size
            if grid[row][col] == 0:
                grid[row][col] = "obstacle"
        
        return grid

    def get_successors(self, state):
        rows = len(self.grid)
        cols = len(self.grid[0])
        successors = []

        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1),   # Right
            (-1, -1), # Up-Left
            (-1, 1),  # Up-Right
            (1, -1),  # Down-Left
            (1, 1)    # Down-Right
        ]

        for direction in directions:
            new_row = state.row + direction[0]
            new_col = state.col + direction[1]

            if 0 <= new_row < rows and 0 <= new_col < cols and self.grid[new_row][new_col] != "obstacle":
                successor = State(new_row, new_col)
                successors.append(successor)

        return successors

    def heuristic(self, state):
        return max(abs(state.row - self.goal_state.row), abs(state.col - self.goal_state.col))

    def a_star(self):
        rows = len(self.grid)
        cols = len(self.grid[0])

        self.start_state.g_score = 0
        self.start_state.f_score = self.heuristic(self.start_state)

        open_set = [] # nodes to be explored 
        closed_set = set() 

        heapq.heappush(open_set, self.start_state)

        while open_set:
            current = heapq.heappop(open_set)

            if (current.row, current.col) == (self.goal_state.row, self.goal_state.col):
                path = []
                while current:
                    path.append((current.row, current.col))
                    current = current.parent
                path.reverse()
                return path

            closed_set.add(current)

            successors = self.get_successors(current)

            for successor in successors:
                if successor in closed_set:
                    continue

                tentative_g_score = current.g_score + 1

                if tentative_g_score < successor.g_score:
                    successor.g_score = tentative_g_score
                    successor.f_score = tentative_g_score + self.heuristic(successor)
                    successor.parent = current

                    if successor not in open_set:
                        heapq.heappush(open_set, successor)

        return None


class MazeVisualizer:
    def __init__(self, size):
        self.size = size
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=self.size*40, height=self.size*40)
        self.canvas.pack()

    def draw_maze(self, grid):
        for row in range(self.size):
            for col in range(self.size):
                x1 = col * 40
                y1 = row * 40
                x2 = x1 + 40
                y2 = y1 + 40

                if grid[row][col] == "obstacle":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                elif grid[row][col] == "start":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")  # Start state
                elif grid[row][col] == "goal":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")  # Goal state
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                    
    def draw_path(self, path):
        for step in path:
            row, col = step
            x1 = col * 40 + 10
            y1 = row * 40 + 10
            x2 = x1 + 20
            y2 = y1 + 20
            self.canvas.create_oval(x1, y1, x2, y2, fill="green")

    def run(self, maze_solver):
        self.draw_maze(maze_solver.grid)
        self.window.update()
        time.sleep(1)

        start_time = time.time()
        path = maze_solver.a_star()
        end_time = time.time()

        if path:
            self.draw_path(path)
            self.window.update()

        time_taken = (end_time - start_time) * 1000  # Convert to milliseconds
        cost = len(path) - 1 if path else float('inf')
        print("Time Taken:", time_taken, "milliseconds")
        print("Cost:", cost)

        self.window.mainloop()


def main():
    size = 10
    obstacle_percentage = int(input("Enter the obstacle percentage (10-90): "))

    if obstacle_percentage < 10 or obstacle_percentage > 90:
        print("Invalid obstacle percentage!")
        return

    maze_solver = MazeSolver(size, obstacle_percentage)
    maze_visualizer = MazeVisualizer(size)
    maze_visualizer.run(maze_solver)


if __name__ == "__main__":
    main()
