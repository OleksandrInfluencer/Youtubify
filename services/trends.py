import logging
import asyncio
from pytrends.request import TrendReq

async def get_trend_for_query(query):
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = [query]
    try:
        logging.info("Building payload for query: %s", query)
        await asyncio.to_thread(pytrends.build_payload, kw_list, timeframe='now 7-d')
        logging.info("Payload built successfully")

        interest_over_time_df = await asyncio.to_thread(pytrends.interest_over_time)
        logging.info("Data retrieved successfully")

        if interest_over_time_df.empty:
            logging.warning("No data for query '%s' over the last week", query)
            return f"No data for query '{query}' over the last week."

        total_interest = interest_over_time_df[query].sum()
        return total_interest
    except Exception as e:
        logging.error("Error fetching trend data: %s", e, exc_info=True)
        return f"Error fetching trend data for query '{query}'."

