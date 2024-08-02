from .start import register_start_handlers
from .queries import register_query_handlers
from .trends import register_trend_handlers

def register_handlers(dp):
    register_start_handlers(dp)
    register_query_handlers(dp)
    register_trend_handlers(dp)
