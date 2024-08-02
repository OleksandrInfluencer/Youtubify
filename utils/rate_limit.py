import datetime

query_limits = {}
MAX_REQUESTS_PER_MINUTE = 5

def check_rate_limit(user_id):
    now = datetime.datetime.now()
    if user_id not in query_limits:
        query_limits[user_id] = []
    query_limits[user_id] = [timestamp for timestamp in query_limits[user_id] if
                             now - timestamp < datetime.timedelta(minutes=1)]
    if len(query_limits[user_id]) >= MAX_REQUESTS_PER_MINUTE:
        return False
    query_limits[user_id].append(now)
    return True
