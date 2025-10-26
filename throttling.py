import time
from fastapi import HTTPException, status
from collections import defaultdict

user_requests = defaultdict(list) 
# when accessing a key for first time, its value assigned is a list

AUTH_RATE_LIMIT = 5
AUTH_TIME_WINDOW_SECONDS=60

GLOBAL_RATE_LIMIT=3
GLOBAL_TIME_WINDOW_SECONDS=60


def apply_rate_limiter(user_id: str):
    current_time = time.time()

    # select rate limit based on user_id
    if user_id == 'generic_unauthenticated_user':
        rate_limit = GLOBAL_RATE_LIMIT
        time_window = GLOBAL_TIME_WINDOW_SECONDS
    else:
        rate_limit = AUTH_RATE_LIMIT
        time_window = AUTH_TIME_WINDOW_SECONDS

    # filter out requests older than the time window
    user_requests[user_id] = [
        t for t in user_requests[user_id] if t > current_time - time_window
    ]

    if len(user_requests[user_id]) >= rate_limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS, 
            detail='Too many requests, try again later.'
        )

    user_requests[user_id].append(current_time)
