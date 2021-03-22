from matplotlib.figure import Figure
import numpy as np


def get_fig():
    """
    A graph of two lines
    """
    fig = Figure()
    ax = fig.subplots()
    x = np.arange(100)
    y1 = 2 * x + 1
    y2 = x + 20

    ax.plot(x, y1, label='2x + 1')
    ax.plot(x, y2, label='x + 20')
    ax.set_title('Linear plot')
    ax.legend(loc='upper left')
    return fig
