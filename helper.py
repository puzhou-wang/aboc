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
    fig.update_layout(xaxis=dict(title='dish name', tickangle=270),
                      yaxis=dict(title=dict_ylabel[value]),
                      height=800)
    fig.layout.coloraxis.colorbar.title = 'avg. rating'
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
    fig = px.scatter(df_plot, y='rating_avg_weighted', x="num_dish_review", color="stars",
                     color_continuous_scale='Bluered', hover_name="name", custom_data=['longitude', 'latitude'])
    hovertemplate = "restaurant name: %{hovertext}<br>restaurant stars: %{marker.color}<br>" + \
                    "number of reviews for dish: %{x}<br>average rating for dish: %{y:.2f}<br>"
    fig.update_traces(hovertemplate=hovertemplate,
                      hoverlabel=dict(bgcolor='white'),
                      marker=dict(size=10))
    fig.update_layout(xaxis=dict(title='number of reviews mentioning '+' '.join(dish_name.split('_'))),
                      yaxis=dict(title='average rating'))
    return fig


def get_gmap_text(clickData):
    # pull restaurant name from click Data
    rest_name = clickData['points'][0]['hovertext']
    # pull restaurant longitude from click Data
    rest_long = clickData['points'][0]['customdata'][0]
    # pull restaurant latitude from click Data
    rest_lat = clickData['points'][0]['customdata'][1]
    # synthesize gmap link
    gmap_link = 'https://www.google.com/maps/search/'+'+'.join(rest_name.split())+f'/@{rest_lat},{rest_long},18z'
    return f'#### {rest_name} was selected! Find it on [Google Map]({gmap_link})!'
