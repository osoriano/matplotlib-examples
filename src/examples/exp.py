from matplotlib.figure import Figure
import numpy as np


def get_fig():
    """
    Sample exp plot
    """
    fig = Figure()
    ax = fig.subplots()
    x = np.linspace(0, 4, 100)
    y = np.exp(x)

    ax.plot(x, y, label=r'$e^x$')
    ax.set_title('Exp plot')
    ax.legend(loc='upper left')
    return fig
