from matplotlib.figure import Figure
import numpy as np


def get_fig():
    """
    Scatter plots for exponential distribution

    First plot uses numpy exponential distribution
    Second plot uses inverse transform sampling
    """
    width = 2 * 6.4
    height = 4.8
    fig = Figure(figsize=(width, height))
    ax1, ax2 = fig.subplots(1, 2)
    y = np.ones(100)

    x1 = np.random.exponential(size=100)
    ax1.scatter(x1, y, label=r'$e^x$')
    ax1.set_title('Scatter Plot')
    ax1.legend(loc='upper left')

    x2 = -np.log(np.random.random(100))
    ax2.scatter(x2, y, label=r'$-\log(u)$')
    ax2.set_title('Scatter Plot')
    ax2.legend(loc='upper left')
    return fig
