# 📘 Assignment: Maze Pathfinding with BFS and DFS

## 🎯 Objective

Build a command-line maze solver in Python and compare Breadth-First Search (BFS) and Depth-First Search (DFS). You will practice graph modeling, algorithm design, and complexity-aware reasoning without external libraries.

## 📝 Tasks

### 🛠️ Parse and Model the Maze

#### Description
Represent a maze as a 2D grid and implement helper functions to find valid neighbor cells (up, down, left, right).

#### Requirements
The completed program should:

- Load a maze from a text file where `#` is a wall, `.` is free space, `S` is start, and `E` is end.
- Validate that the maze has exactly one `S` and one `E`.
- Implement `get_neighbors(row, col, maze)` returning only in-bounds, walkable cells.
- Keep the code organized using clear function names and type hints.


### 🛠️ Implement BFS and DFS Solvers

#### Description
Implement two pathfinding functions that attempt to find a path from `S` to `E`: one using BFS and one using DFS.

#### Requirements
The completed program should:

- Implement `solve_bfs(maze, start, end)` and `solve_dfs(maze, start, end)`.
- Return a list of coordinates representing a valid path, or an empty list when no path exists.
- Track and return how many nodes each algorithm explored.
- Print the maze with the path marked as `*` (without replacing `S` and `E`).


### 🛠️ Compare Algorithm Behavior

#### Description
Run both algorithms on the same maze and compare correctness and exploration behavior.

#### Requirements
The completed program should:

- Run BFS and DFS on `sample-maze.txt` and print both results.
- Show path length and explored-node count for each algorithm.
- Include a short code comment explaining why BFS guarantees the shortest path in unweighted grids.
- Add at least one additional maze test case and describe the observed difference between BFS and DFS.
