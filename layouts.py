import dash_core_components as dcc
import dash_html_components as html
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# the entry layout
layout_entry = html.Div(children=[
    html.H2('Welcome to A Bite of China!'),
    html.Div(className='row', children=[
        dcc.Link(html.Button('Explore Dishes'), href='/apps/dish')
    ], style={'padding': 10}),
    html.Div(className='row', children=[
        dcc.Link(html.Button('Recommend Restaurants'), href='/apps/rest')
    ], style={'padding': 10})
])

# the layout for dish recommender
layout_dish_recom = html.Div([
    html.H2('Welcome to A Bite of China!'),
    html.H3('Dish Explorer'),
    html.Div(className='row', children=[
        html.Div('Sort all Chinese dishes by '),
        html.Div(children=[
            dcc.Dropdown(id='dish_sort', options=[
                {'label': 'number of reviews', 'value': 'num_review'},
                {'label': 'number of restaurants', 'value': 'num_rest'},
                {'label': 'average rating', 'value': 'rating_avg_weighted'},
            ], clearable=False, value='num_review')
        ], style={'padding': 10, "width": "20%"})
    ], style={'display': 'flex', 'align-items': 'center'}),
    dcc.Graph(id='dish_plot'),
    html.Div(className='row', children=[
        dcc.Link(html.Button('Go Back'), href='/')
    ], style={'padding': 10})
])

# the layout for restaurant recommender
layout_rest_recom = html.Div([
    html.H2('Welcome to A Bite of China!'),
    html.H3('Restaurant Recommender'),
    # html.Div(className='row', children=[
    #     html.Div('Sort all Chinese dishes by '),
    #     html.Div(children=[
    #         dcc.Dropdown(id='dish_sort', options=[
    #             {'label': 'number of reviews', 'value': 'num_review'},
    #             {'label': 'number of restaurants', 'value': 'num_rest'},
    #             {'label': 'average rating', 'value': 'rating_avg_weighted'},
    #         ], clearable=False, value='num_review')
    #     ], style={'padding': 10, "width": "20%"})
    # ], style={'display': 'flex', 'align-items': 'center'}),
    # dcc.Graph(id='dish_plot'),
    html.Div(className='row', children=[
        dcc.Link(html.Button('Go Back'), href='/')
    ], style={'padding': 10})
])
