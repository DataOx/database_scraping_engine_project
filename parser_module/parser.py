import html
import re
from datetime import timedelta, datetime
from typing import List

from config import CURRENT_TIME_ZONE


class Parser:

    def __init__(self):
        self.current_time_zone = CURRENT_TIME_ZONE
        self.current_date = datetime.now(self.current_time_zone).date()

    def get_cleaned_data(self, data_from_scraper) -> List[dict]:
        cleaned_data = []
        for person in data_from_scraper:
            dictionary = {
                "name": html.unescape(person['name']),
                "gender": person['gender'],
                "country": person['country_name'],
                "date": self.date_correction(person['time_ago'])
            }
            cleaned_data.append(dictionary)
        return cleaned_data

    def date_correction(self, time_ago: str) -> datetime.date:
        date_: datetime.date = ''
        if re.search(r"minute|hour", time_ago):
            date_ = self.current_date - timedelta(days=1)
        elif re.search(r"yesterday", time_ago):
            date_ = self.current_date - timedelta(days=2)
        elif re.search(r"(\d+)\sdays\sago", time_ago):
            num_of_day = re.search(r"(\d+)\sdays\sago", time_ago).group(1)
            date_ = self.current_date - timedelta(days=int(num_of_day) + 1)
        return date_
