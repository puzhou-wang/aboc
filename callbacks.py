from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import logging

from app import app
import helper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# callback function to update dish_plot based on sort option selected by user
@app.callback(
    [Output('dish_plot', 'figure'),
     Output('dish_plot', 'style')],
    Input('dish_sort', 'value'))
def update_dish_plot(value):
    if value:
        return [helper.get_dish_plot(value), {}]
    else:
        raise PreventUpdate


# callback function to jump from dish explorer to corresponding restaurant recommender
@app.callback(
    Output('url', 'pathname'),
    Input('dish_plot', 'clickData'))
def dish_to_rest_recom(clickData):
    if clickData:
        url = clickData['points'][0]['hovertext']
        logger.info('jumping from dish explorer to restaurant recommender')
        return url
    else:
        raise PreventUpdate


# callback function to automatically select dish name in restaurant recommender
@app.callback(
    Output('dish_selector', 'value'),
    Input('url', 'pathname'))
def url_to_dish_selector(pathname):
    if pathname.startswith('/apps/rest'):
        dish_selected = pathname[10:]
        logger.info(f'update dish selector with value of {dish_selected[1:]}')
        return dish_selected[1:]
    else:
        raise PreventUpdate


# callback function to update restaurant_plot based on dish selector
@app.callback(
    [Output('rest_plot', 'figure'),
     Output('rest_plot', 'style')],
    Input('dish_selector', 'value'))
def url_to_dish_selector(dish_name):
    if dish_name:
        # dish_selected = pathname[10:]
        # logger.info(f'update dish selector with value of {dish_selected[1:]}')
        return [None, {}]
    else:
        raise PreventUpdate
