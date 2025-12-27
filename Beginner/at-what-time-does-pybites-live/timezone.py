from datetime import datetime
from zoneinfo import ZoneInfo

AUSTRALIA = ZoneInfo('Australia/Sydney')
SPAIN = ZoneInfo('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt: datetime):
    """
    Receives a naive UTC datetime object and returns a two element
    tuple of Australian and Spanish (timezone aware) datetimes
    """