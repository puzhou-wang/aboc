import dash
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = 'A Bite of China'
server = app.server
