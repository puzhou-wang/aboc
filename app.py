import dash
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = dash.Dash(__name__, suppress_callback_exceptions=True, title='A Bite of China', assets_folder='static',
                assets_url_path='static')
application = app.server
