import dash_core_components as dcc
import dash_html_components as html
import logging
import pickle

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


with open('./data/dropdown_options', 'rb') as f:
    dish_options = pickle.load(f)


# the entry layout
layout_entry = html.Div(children=[
    html.H2('Welcome to A Bite of China!', style={'margin-left': 10}),
    dcc.Markdown('''No idea which dish to try? Not a problem. Click on the **EXPLORE DISHES** button!''',
                 style={'margin-left': 10}),
    dcc.Markdown('''Already have a dish in mind? Click on the **EXPLORE RESTAURANTS** button!''',
                 style={'margin-left': 10}),
    html.Div(className='row', children=[
        dcc.Link(html.Button('Explore Dishes'), href='/apps/dish')
    ], style={'padding': 10}),
    html.Div(className='row', children=[
        dcc.Link(html.Button('Explore Restaurants'), href='/apps/rest')
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
    dcc.Markdown('''
        Feel free to zoom in and out in the figure below! 
        Click on each bar and explore restaurants serving the dish of interest!
    '''),
    dcc.Graph(id='dish_plot', style={'display': 'none'}),
    html.Div(className='row', children=[
        dcc.Link(html.Button('Go Back to Homepage'), href='/')
    ], style={'padding': 10})
])

# the layout for restaurant recommender
layout_rest_recom = html.Div([
    html.H2('Welcome to A Bite of China!'),
    html.H3('Restaurant Explorer'),
    dcc.Markdown('''
        Each restaurant is represented as a data point in 2D plot, with dimensions as the number of reviews and
         average rating. Color is based on the number of stars for a restaurant.
    '''),
    dcc.Markdown(id='gmap_md', children='Click on the restaurant of interest to activate its Google Map link here!'),
    dcc.Markdown('''
        Change mind? No problem! Try a different dish from the dropdown menu below!
    '''),
    dcc.Dropdown(id='dish_selector', options=dish_options, clearable=False,
                 placeholder="Select a dish to see recommendations"),
    dcc.Graph('rest_plot', style={'display': 'none'}),
    html.Div(className='row', children=[
        dcc.Link(html.Button('Go Back to Dish Explorer'), href='/apps/dish')
    ], style={'padding': 10})
])
