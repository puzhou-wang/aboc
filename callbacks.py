from dash.dependencies import Input, Output
import logging

from app import app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.callback(
    Output('app-1-display-value', 'children'),
    Input('app-1-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)


@app.callback(
    Output('app-2-display-value', 'children'),
    Input('app-2-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)
