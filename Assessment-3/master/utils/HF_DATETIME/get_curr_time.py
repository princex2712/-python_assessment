from datetime import datetime
from django.conf import settings
import pytz

def get_current_time():
    """
    Retrieves the current time in the specified time zone.

    This function fetches the current Coordinated Universal Time (UTC) and converts
    it to the time zone specified in the Django settings.

    Returns:
    - A datetime object representing the current time in the specified time zone.

    Dependencies:
    - datetime module from Python's standard library.
    - pytz module for handling time zones.
    - settings module from Django to access Django settings.

    Example:
    >>> current_time = get_current_time()
    >>> print(current_time)
    2024-02-06 15:30:00+05:30
    """
    utc_now = datetime.utcnow()
    curr_time = pytz.timezone(settings.TIME_ZONE)
    return utc_now.astimezone(curr_time)

