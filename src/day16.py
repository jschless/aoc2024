import heapq
from collections import defaultdict

fname = "./examples/day16b.txt"
# fname = "./examples/day16.txt"
fname = "./inputs/day16.txt"
grid = {}
start = None
with open(fname) as f:
    for i, row in enumerate(f.read().strip().split("\n")):
        for j, char in enumerate(row):
            if char == "S":
                start = (i, j)
            grid[(i, j)] = char
            WD = j
            HT = i


clockwise = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
c_clockwise = {v: k for k, v in clockwise.items()}


def find_all_shortest_paths(grid, start, clockwise, c_clockwise):
    pq = []
    sp = (start, (0, 1))  # Start position and initial direction
    heapq.heappush(pq, (0, sp))  # Push start state into the priority queue

    cost_so_far = {sp: 0}  # Dictionary to store the minimum cost for each state
    parents = defaultdict(set)  # Map each state to its parent states
    visited = set()
    end_state = None  # To store the goal state when found

    # Dijkstra-like traversal
    while pq:
        cost, (cur_loc, cur_dir) = heapq.heappop(pq)
        if (cur_loc, cur_dir) in visited:
            continue
        visited.add((cur_loc, cur_dir))

        # Check if the forward location is the goal
        fwd_loc = (cur_loc[0] + cur_dir[0], cur_loc[1] + cur_dir[1])
        if grid.get(fwd_loc) == "E":  # Goal found
            end_state = (fwd_loc, cur_dir)
            cost_so_far[end_state] = cost + 1
            print("Part 1:", cost + 1)
            parents[end_state].add((cur_loc, cur_dir))
            break

        # Process forward movement
        if grid.get(fwd_loc) != "#":  # Valid forward move
            new_cost = cost + 1
            next_state = (fwd_loc, cur_dir)
            if next_state not in cost_so_far or new_cost <= cost_so_far[next_state]:
                if new_cost < cost_so_far.get(next_state, float("inf")):
                    cost_so_far[next_state] = new_cost
                    parents[next_state] = set()
                parents[next_state].add((cur_loc, cur_dir))
                heapq.heappush(pq, (new_cost, next_state))

        # Process turning clockwise
        temp = (cur_loc, clockwise[cur_dir])
        new_cost = cost + 1000
        if temp not in cost_so_far or new_cost <= cost_so_far[temp]:
            if new_cost < cost_so_far.get(temp, float("inf")):
                cost_so_far[temp] = new_cost
                parents[temp] = set()
            parents[temp].add((cur_loc, cur_dir))
            heapq.heappush(pq, (new_cost, temp))

        # Process turning counter-clockwise
        temp = (cur_loc, c_clockwise[cur_dir])
        new_cost = cost + 1000
        if temp not in cost_so_far or new_cost <= cost_so_far[temp]:
            if new_cost < cost_so_far.get(temp, float("inf")):
                cost_so_far[temp] = new_cost
                parents[temp] = set()
            parents[temp].add((cur_loc, cur_dir))
            heapq.heappush(pq, (new_cost, temp))

    # Backtrack to find all nodes in all shortest paths
    def backtrack(state, visited_nodes):
        if state in visited_nodes:
            return
        visited_nodes.add(state[0])  # Add only the grid location, not direction
        for parent in parents[state]:
            backtrack(parent, visited_nodes)

    if not end_state:
        return set()  # Return empty set if no path found

    result_nodes = set()
    backtrack(end_state, result_nodes)
    return result_nodes


result = find_all_shortest_paths(grid, start, clockwise, c_clockwise)
print("Part 2:", len(result))
