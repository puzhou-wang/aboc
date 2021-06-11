import logging
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

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


def get_df_plot(dish_name):
    df_one_dish = df_rev[df_rev.review_text.str.contains(' '.join(dish_name.split('_')))]
    df_plot = df_one_dish.groupby(
        ['restaurant_id', 'name', 'stars', 'num_review_total', 'address']).mean().reset_index()
    list_dict = []
    for rest in df_plot.restaurant_id.unique():
        df_rest = df_one_dish[df_one_dish.restaurant_id == rest]
        avg_weighted = sum(df_rest['review_weight'] * df_rest['rating']) / sum(df_rest['review_weight'])
        num_review = df_rest.review_id.nunique()
        list_dict.append({'restaurant_id': rest, 'rating_avg_weighted': avg_weighted, 'num_dish_review': num_review})
    return df_plot.merge(pd.DataFrame(list_dict), on='restaurant_id')


def get_rest_plot(dish_name):
    df_plot = get_df_plot(dish_name)
    layout = dict(
        xaxis=dict(title='number of reviews regarding the dish'),
        yaxis=dict(title='weighted average rating')
    )
    data = go.Scatter(
        x=df_plot['num_dish_review'],
        y=df_plot['rating_avg_weighted'],
        text=df_plot['name'],
        mode='markers',
        marker=dict(
            size=10,
            color=df_plot['stars'],
            colorscale='Bluered',
            showscale=True
        ),
        hovertemplate=
        "restaurant name: %{text}<br>" +
        "restaurant stars: %{marker.color}<br>" +
        "number of reviews for dish: %{x}<br>" +
        "average rating for dish: %{y:.2f}<br>",
        name=""
    )
    fig_fr = go.Figure(data=data, layout=layout)
    return fig_fr
