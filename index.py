import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import logging

from app import app
from layouts import layout_entry, layout_dish_recom, layout_rest_recom
import callbacks

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        logger.info('app opened at entry page!')
        return layout_entry
    elif pathname == '/apps/app1':
        return layout_dish_recom
    elif pathname == '/apps/app2':
        return layout_rest_recom
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
