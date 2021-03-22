import base64
import functools
import io


def fig_to_img(fig_func):
    @functools.wraps(fig_func)
    def wrapper():
        buf = io.BytesIO()
        fig = fig_func()
        fig.savefig(buf, format='png')
        data = base64.b64encode(buf.getbuffer()).decode('ascii')
        return f'''
        <div style="display: flex; justify-content: center">
            <img src="data:image/png;base64,{data}"/>
        </div>'''

    return wrapper
