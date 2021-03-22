from flask import Flask

import examples.empty as empty
import examples.exp as exp
import examples.grid.grid as grid
import examples.line as line
import examples.scatter as scatter
import util

app = Flask(__name__)


@app.route('/')
def home_route():
    return app.send_static_file('index.html')


@app.route('/empty')
@util.fig_to_img
def empty_route():
    return empty.get_fig()


@app.route('/line')
@util.fig_to_img
def line_route():
    return line.get_fig()


@app.route('/exp')
@util.fig_to_img
def exp_route():
    return exp.get_fig()


@app.route('/scatter')
@util.fig_to_img
def scatter_route():
    return scatter.get_fig()


@app.route('/grid')
@util.fig_to_img
def grid_route():
    return grid.get_fig()
