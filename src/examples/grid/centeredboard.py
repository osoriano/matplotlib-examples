import numpy as np


class CenteredBoard:
    def __init__(self, n):
        """
        Create a board of size n x n centered at (0, 0).
        """
        self.n = n
        self.offset = n // 2
        self.grid = np.zeros((n, n), dtype=np.int32)

    def setval(self, i, j, v):
        i += self.offset
        j += self.offset
        self.grid[i][j] = v

    def getval(self, i, j):
        i += self.offset
        j += self.offset
        return self.grid[i][j]

    def inrange(self, i, j):
        i += self.offset
        j += self.offset
        return 0 <= i < self.n and 0 <= j < self.n
