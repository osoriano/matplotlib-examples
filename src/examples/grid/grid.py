from collections import deque

from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
import numpy as np

from examples.grid.centeredboard import CenteredBoard


def get_fig():
    """
    Centered chess grid showing the minimum amount of steps
    a knight needs to arrive at each position
    """
    width = 3 * 6.4
    height = 3 * 4.8
    fig = Figure(figsize=(width, height))
    ax = fig.subplots()

    n = 25
    board = knight_explore(n)
    offset = board.offset
    grid = board.grid
    groups = get_knight_groups(board)

    # ax.matshow(grid)
    ax.matshow(groups)
    ax.set_xticks(range(board.n))
    ax.set_xticklabels(range(-offset, offset + 1))
    ax.set_yticks(range(board.n))
    ax.set_yticklabels(range(-offset, offset + 1))

    for i in range(n):
        for j in range(n):
            ax.text(i, j, grid[i, j], ha="center", va="center", color="w")

    # Draw step for octant
    linewidth = 2.5
    x = np.arange(offset + 2.5, n)
    y_step = np.arange(offset - 2.5, -1, -1)
    ax.step(x, y_step, color='black', linewidth=linewidth)

    # Draw step for knight move
    x_knight = np.arange(offset + 2.5, n, 2)
    y_knight = np.arange(offset - 2.5, 4, -1)
    ax.step(x_knight, y_knight, color='black', linewidth=linewidth)

    # Draw horizontal line
    y_line = np.full(offset - 1, offset + 0.5)
    ax.plot(x, y_line, color='black', linewidth=linewidth)

    # Draw retangle
    rect_size = 5
    rect_offset = offset - rect_size / 2
    rect = Rectangle(
        (rect_offset, rect_offset),
        rect_size,
        rect_size,
        linewidth=1,
        edgecolor='r',
        facecolor='none',
    )
    ax.add_patch(rect)

    ax.set_title('Knight positions from center')
    return fig


def get_knight_groups(board):
    groups = CenteredBoard(board.n)
    offset = groups.offset
    for y in range(offset + 1):
        for x in range(offset + 1):
            if x > 2 and x >= y:
                group = get_knight_group(x, y) + 1
                groups.setval(y, x, group)
                groups.setval(-y, -x, group)
                groups.setval(y, -x, group)
                groups.setval(-y, x, group)

                groups.setval(x, y, group)
                groups.setval(-x, -y, group)
                groups.setval(x, -y, group)
                groups.setval(-x, y, group)
    return groups.grid


def get_knight_group(x, y):
    """
    Get the group of the knight

    Reference:
    https://leetcode.com/problems/minimum-knight-moves/discuss/392053/Here-is-how-I-get-the-formula-(with-graphs)
    """
    if y < (x - 1) // 2 + 3:
        return (x - 3) // 2
    return (x + y - 8) // 3 + 1


def knight_explore(n):
    """
    Explore a board of size n centered at (0, 0).

    Board is explored according to path that a chess knight can take.
    Each entry in the board will contain the minimum amount of steps
    for the knight to arrive.
    """
    board = CenteredBoard(n)

    start_pos = (0, 0)
    start_v = 0
    q = deque([(start_pos, start_v)])
    seen = set()

    while q:
        pos, v = q.popleft()

        if pos in seen:
            continue

        i, j = pos
        if not board.inrange(i, j):
            continue

        seen.add(pos)

        board.setval(i, j, v)
        q.append(((i + 1, j + 2), v + 1))
        q.append(((i + 2, j + 1), v + 1))
        q.append(((i - 1, j - 2), v + 1))
        q.append(((i - 2, j - 1), v + 1))
        q.append(((i - 1, j + 2), v + 1))
        q.append(((i - 2, j + 1), v + 1))
        q.append(((i + 1, j - 2), v + 1))
        q.append(((i + 2, j - 1), v + 1))

    return board
