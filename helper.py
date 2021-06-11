import logging
import pandas as pd
import plotly.express as px

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# read in data frames
df_dish = pd.read_csv('./data/dishes.csv')
df_rev = pd.read_csv('./data/reviews.csv')


def get_dish_plot(value):
    # dictionary to determine y axis label based on value
    dict_ylabel = {'num_review': 'number of reviews',
                   'num_rest': 'number of restaurants',
                   'rating_avg_weighted': 'average rating'}
    # dictionary to determine precision for y values in hover text based on value
    dict_yprecision = {'num_review': 0, 'num_rest': 0, 'rating_avg_weighted': 2}
    # sort df_dish based on value
    df_plot = df_dish.sort_values(value, ascending=False)
    fig = px.bar(df_plot, y=value, x="dish_name", color="rating_avg_weighted",
                 color_continuous_scale='Bluered', hover_name="link")
    # hover template
    htemplate = f'%{{x}}<br>{dict_ylabel[value]}: %{{y:.{dict_yprecision[value]}f}}'
    fig.update_traces(hovertemplate=htemplate, hoverlabel=dict(bgcolor='white'))
    fig.update_layout(xaxis=dict(title='dish name'),
                      yaxis=dict(title=dict_ylabel[value]),
                      height=800)
    return fig
