import heapq
import copy

def is_magic(square):
    s = 15
    # rows
    for row in square:
        if sum(row) != s:
            return False
    # columns
    for col in zip(*square):
        if sum(col) != s:
            return False
    # diagonals
    if sum(square[i][i] for i in range(3)) != s:
        return False
    if sum(square[i][2-i] for i in range(3)) != s:
        return False
    return True


def heuristic(square):
    s = 15
    h = 0

    # Only evaluate rows/cols with no zeros
    for row in square:
        if 0 not in row:
            h += abs(s - sum(row))

    for col in zip(*square):
        if 0 not in col:
            h += abs(s - sum(col))

    diag1 = [square[i][i] for i in range(3)]
    diag2 = [square[i][2-i] for i in range(3)]

    if 0 not in diag1:
        h += abs(s - sum(diag1))
    if 0 not in diag2:
        h += abs(s - sum(diag2))

    return h


def best_first_magic():
    initial = [[0]*3 for _ in range(3)]
    heap = []
    heapq.heappush(heap, (heuristic(initial), initial, set()))

    while heap:
        h, square, used = heapq.heappop(heap)

        # If fully filled and magic, return
        if len(used) == 9 and is_magic(square):
            return square

        # Find first empty cell
        for i in range(3):
            for j in range(3):
                if square[i][j] == 0:
                    for num in range(1, 10):
                        if num not in used:
                            new_square = copy.deepcopy(square)
                            new_square[i][j] = num
                            new_used = used | {num}
                            heapq.heappush(heap, (heuristic(new_square), new_square, new_used))
                    # Only fill one cell at a time
                    break
            else:
                continue
            break

    return None


result = best_first_magic()

if result:
    for row in result:
        print(row)
else:
    print("No solution found")
