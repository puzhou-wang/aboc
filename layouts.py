import dash_core_components as dcc
import dash_html_components as html
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# the entry layout
layout_entry = html.Div(children=[
    html.H2('Welcome to A Bite of China!'),
    html.Div(className='row', children=[
        dcc.Link(html.Button('Explore Dishes'), href='/apps/app1')
    ], style={'padding': 10}),
    html.Div(className='row', children=[
        dcc.Link(html.Button('Recommend Restaurants'), href='/apps/app2')
    ], style={'padding': 10})
])

# the layout for dish recommender
layout_dish_recom = html.Div([
    html.H3('App 1'),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-1-display-value'),
    dcc.Link('Go to App 2', href='/apps/app2')
])

# the layout for restaurant recommender
layout_rest_recom = html.Div([
    html.H3('App 2'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1', href='/apps/app1')
])
