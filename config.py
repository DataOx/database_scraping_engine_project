import os

import pytz

from dotenv import load_dotenv

load_dotenv()

URL = "https://www.oxford-royale.com/wp-admin/admin-ajax.php?enrol_total={}&action=get_enrolmeter_entries"

HEADERS = {
    'authority': 'www.oxford-royale.com',
    'accept': '*/*',
    'content-type': 'application/x-www-form-urlencoded',
    'referer': 'https://www.oxford-royale.com/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

SPREADSHEET_ID = '1JLKGDotCfnqol-ujKvM4XLZ6l8zOtSIdilOveDCCIwg'
NAME_LIST = "MAIN_LIST"

CURRENT_TIME_ZONE = pytz.timezone("Europe/Kyiv")

POSTGRES_CONNECTION_STR = 'postgresql://{}:{}@{}:{}/{}'.format(
    os.environ.get('POSTGRES_USER'), os.environ.get('POSTGRES_PASSWORD'), os.environ.get('POSTGRES_HOST'),
    os.environ.get('POSTGRES_PORT'), os.environ.get('POSTGRES_DB'))
