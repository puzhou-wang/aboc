import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import logging

from app import app
from layouts import layout_entry, layout_dish_recom, layout_rest_recom
import callbacks

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.layout = dcc.Loading(children=[
    html.Div([
        dcc.Location(id='url', refresh=True),
        html.Div(id='page-content')
    ])], fullscreen=True, type='graph')


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        logger.info('app opened at entry page!')
        return layout_entry
    elif pathname == '/apps/dish':
        logger.info('dish explorer visited!')
        return layout_dish_recom
    elif pathname.startswith('/apps/rest'):
        dish_selected = pathname[10:]
        if not dish_selected:  # user goes into restaurant recommender from entry page
            logger.info('restaurant recommender visited from entry page!')
            return layout_rest_recom
        else:  # user goes into restaurant recommender by selecting a dish in dish explorer
            logger.info(f'restaurant recommender visited with selected dish: {dish_selected[1:]}')
            return layout_rest_recom
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=False, port=8080)
