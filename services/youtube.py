import logging
import asyncio
from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY
import datetime
import pytz

async def get_top_queries(period):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY, cache_discovery=False)
    now = datetime.datetime.now(pytz.UTC)

    if period == 'hour':
        time_delta = datetime.timedelta(hours=1)
    elif period == 'day':
        time_delta = datetime.timedelta(days=1)
    elif period == 'week':
        time_delta = datetime.timedelta(days=7)
    elif period == 'month':
        time_delta = datetime.timedelta(days=30)
    else:
        return ["Unknown period. Please use hour, day, week, or month."]

    published_after = (now - time_delta).isoformat()

    try:
        request = youtube.search().list(
            part="snippet",
            type="video",
            order="viewCount",
            videoDuration="short",
            publishedAfter=published_after,
            maxResults=10,
            relevanceLanguage="en",
            regionCode="US"
        )

        response = await asyncio.to_thread(request.execute)

        queries = []
        for item in response.get('items', []):
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']

            video_request = youtube.videos().list(
                part="statistics",
                id=video_id
            )
            video_response = await asyncio.to_thread(video_request.execute)
            view_count = video_response['items'][0]['statistics']['viewCount']

            queries.append((video_title, view_count, video_id))

        if not queries:
            return ["No results for this period."]

        return queries

    except Exception as e:
        logging.error("Error fetching data from YouTube: %s", e, exc_info=True)
        return ["Error fetching data from YouTube."]

def format_views(view_count, language_code):
    """Форматує кількість переглядів з одиницями виміру."""
    view_count = int(view_count)
    if view_count >= 1_000_000:
        if language_code == 'uk':
            return f"{view_count / 1_000_000:.1f} млн переглядів"
        else:
            return f"{view_count / 1_000_000:.1f}M views"
    elif view_count >= 1_000:
        if language_code == 'uk':
            return f"{view_count / 1_000:.1f} тис переглядів"
        else:
            return f"{view_count / 1_000:.1f}K views"
    else:
        if language_code == 'uk':
            return f"{view_count} переглядів"
        else:
            return f"{view_count} views"
