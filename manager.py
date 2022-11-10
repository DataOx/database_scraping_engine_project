from dao_module.dao import Dao
from config import URL
from google_api_module.module_google_api import GoogleAPI
from logging_module.logger import Logger
from parser_module.parser import Parser
from scraper_module.scraper import Scraper


class Manager:

    def __init__(self):
        self.scraper = Scraper(URL)
        self.parser = Parser()
        self.storage = Dao()
        self.spreadsheet = GoogleAPI()
        self.logger = Logger(self.__class__.__name__)

    def launch(self):
        self._save_to_db()
        self._send_to_sheet()

    def _save_to_db(self):
        data_list = self._scraper_selection()
        self.storage.save_all(data_list)
        self.logger.info(f"received records from the site: {len(data_list)} (last two days)")

    def _send_to_sheet(self):
        for_google_sheet = self.storage.get_non_saved_data()
        self.spreadsheet.append_data(for_google_sheet)
        self.logger.info(f"added to spreadsheet successfully new records: {len(for_google_sheet)}")
        self.storage.update_all(for_google_sheet)

    def _scraper_selection(self):
        if self.storage.table_is_empty():
            data_list = self.parser.get_cleaned_data(self.scraper.all_data)
        else:
            data_list = self.parser.get_cleaned_data(self.scraper.current_data)
        return data_list


if __name__ == '__main__':
    a = Manager()
    a.launch()
