from collections import deque


WALL = "#"
FREE = "."
START = "S"
END = "E"
PATH = "*"


def load_maze(file_path: str) -> list[list[str]]:
    """Load a maze file into a 2D list of characters."""
    with open(file_path, "r", encoding="utf-8") as file:
        rows = [list(line.rstrip("\n")) for line in file if line.strip()]
    return rows


def find_start_end(maze: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return (start, end) coordinates. Raise ValueError if invalid."""
    starts: list[tuple[int, int]] = []
    ends: list[tuple[int, int]] = []

    for r, row in enumerate(maze):
        for c, value in enumerate(row):
            if value == START:
                starts.append((r, c))
            elif value == END:
                ends.append((r, c))

    if len(starts) != 1 or len(ends) != 1:
        raise ValueError("Maze must contain exactly one 'S' and one 'E'")

    return starts[0], ends[0]


def get_neighbors(row: int, col: int, maze: list[list[str]]) -> list[tuple[int, int]]:
    """Return valid neighbors (up, down, left, right)."""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors: list[tuple[int, int]] = []

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
            if maze[nr][nc] != WALL:
                neighbors.append((nr, nc))

    return neighbors


def reconstruct_path(
    parent: dict[tuple[int, int], tuple[int, int] | None],
    end: tuple[int, int],
) -> list[tuple[int, int]]:
    path: list[tuple[int, int]] = []
    current: tuple[int, int] | None = end

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


def solve_bfs(
    maze: list[list[str]],
    start: tuple[int, int],
    end: tuple[int, int],
) -> tuple[list[tuple[int, int]], int]:
    """Return (path, explored_count) using BFS."""
    queue = deque([start])
    parent: dict[tuple[int, int], tuple[int, int] | None] = {start: None}
    explored_count = 0

    while queue:
        current = queue.popleft()
        explored_count += 1

        if current == end:
            return reconstruct_path(parent, end), explored_count

        for neighbor in get_neighbors(current[0], current[1], maze):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    return [], explored_count


def solve_dfs(
    maze: list[list[str]],
    start: tuple[int, int],
    end: tuple[int, int],
) -> tuple[list[tuple[int, int]], int]:
    """Return (path, explored_count) using DFS."""
    stack = [start]
    parent: dict[tuple[int, int], tuple[int, int] | None] = {start: None}
    explored_count = 0

    while stack:
        current = stack.pop()
        explored_count += 1

        if current == end:
            return reconstruct_path(parent, end), explored_count

        for neighbor in get_neighbors(current[0], current[1], maze):
            if neighbor not in parent:
                parent[neighbor] = current
                stack.append(neighbor)

    return [], explored_count


def render_maze_with_path(
    maze: list[list[str]],
    path: list[tuple[int, int]],
) -> str:
    """Render a maze string with * marking the path (except S and E)."""
    rendered = [row[:] for row in maze]

    for r, c in path:
        if rendered[r][c] not in (START, END):
            rendered[r][c] = PATH

    return "\n".join("".join(row) for row in rendered)


def print_result(name: str, path: list[tuple[int, int]], explored_count: int) -> None:
    print(f"\n{name}:")
    if path:
        print(f"Path length: {len(path) - 1}")
        print(f"Explored nodes: {explored_count}")
    else:
        print("No path found")
        print(f"Explored nodes: {explored_count}")


def main() -> None:
    maze = load_maze("sample-maze.txt")
    start, end = find_start_end(maze)

    bfs_path, bfs_explored = solve_bfs(maze, start, end)
    dfs_path, dfs_explored = solve_dfs(maze, start, end)

    print_result("BFS", bfs_path, bfs_explored)
    print(render_maze_with_path(maze, bfs_path))

    print_result("DFS", dfs_path, dfs_explored)
    print(render_maze_with_path(maze, dfs_path))


if __name__ == "__main__":
    main()
