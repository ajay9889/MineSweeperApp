from queue import PriorityQueue
import random


def generate_empty_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def is_valid_position(grid, row, col, target_value):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return False
    return grid[row][col] == target_value


def place_mine(grid, row, col):
    grid[row][col] = "X"
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r, c = row + dr, col + dc
            if is_valid_position(grid, r, c, 0):
                grid[r][c] += 1


def generate_minesweeper_grid(rows, cols, mines):
    if mines >= rows * cols:
        raise ValueError("Too many mines for the grid size.")

    grid = generate_empty_grid(rows, cols)
    available_positions = [(r, c) for r in range(rows) for c in range(cols)]

    for _ in range(mines):
        random.shuffle(available_positions)
        row, col = available_positions.pop()
        place_mine(grid, row, col)

    return grid


def print_minesweeper_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))


# rows = 10
# cols = 10
# mines = 5

# minesweeper_grid = generate_minesweeper_grid(rows, cols, mines)
# print_minesweeper_grid(minesweeper_grid)
# def maximumPrioritySum(priority, x, y):
#     n = len(priority)
#     dp = [0] * (y + 1)
#     for i in range(n):
#         for j in range(y, x - 1, -1):
#             dp[j] = max(dp[j], dp[j - x] + priority[i] if j >= x else 0)

#     return dp[y]


def maximumPrioritySumee(priority, x, y):
    last_time_performed = {}
    max_priority_sum = 0
    total_time = 0

    for task in priority:
        current_time = last_time_performed.get(task, -1)
        time_since_last_task = total_time - current_time
        print(current_time, time_since_last_task, task, max_priority_sum)
        if time_since_last_task >= x:
            total_time += 1
            max_priority_sum += task
            last_time_performed[task] = total_time
        else:
            remaining_time = x - time_since_last_task
            print(remaining_time, x, total_time)
            if remaining_time <= y - total_time:
                total_time += remaining_time
                max_priority_sum += task
                maximumPrioritySum(priority, current_time, remaining_time)
            else:
                break

    return max_priority_sum


def maximumPrioritySum(priority, x, y):
    task_last_performed = {}
    max_priority_sum = 0
    current_time = 0
    while current_time < y:
        for task in priority:
            if task in task_last_performed:
                time_since_last_task = current_time - task_last_performed[task]
                if time_since_last_task < x:
                    current_time = task_last_performed[task] + x
            if current_time < y or current_time == x:
                max_priority_sum += task
                task_last_performed[task] = current_time
                current_time += 1
    return max_priority_sum


# priority = [3, 1, 2]
# x = 5
# y = 7
# result = maximumPrioritySum(priority, x, y)
# print(result)




def getMinCost(cost, compatible1, compatible2, min_compatible):
    n = len(cost)
    gpu_info = [(cost[i], compatible1[i], compatible2[i]) for i in range(n)]
    gpu_info.sort()  # Sort GPUs by cost in ascending order
    
    cluster1_count = 0
    cluster2_count = 0
    min_cost = float('inf')
    
    for i in range(n):
        c1, c2 = gpu_info[i][1], gpu_info[i][2]
        if c1 == 1:
            cluster1_count += 1
        if c2 == 1:
            cluster2_count += 1
        
        if cluster1_count >= min_compatible and cluster2_count >= min_compatible:
            min_cost = min(min_cost, sum(cost[:i+1]))  # Calculate the cost so far
    
    if cluster1_count < min_compatible or cluster2_count < min_compatible:
        return -1  # It's not possible to satisfy the requirements
    
    return min_cost

# Example usage:
cost = [2, 4, 6, 5]
compatible1 = [1, 1, 1, 0]
compatible2 = [0, 0, 1, 1]
min_compatible = 2
result = getMinCost(cost, compatible1, compatible2, min_compatible)
print(result)  # Output: 13
