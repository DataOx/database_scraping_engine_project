import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from config import SPREADSHEET_ID, NAME_LIST


class GoogleCredentials:

    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    @property
    def sheet_service(self):
        creds = None
        if os.path.exists('google_api_module/token.json'):
            creds = Credentials.from_authorized_user_file('google_api_module/token.json', self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('google_api_module/credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
                self.create_token(creds)
        return build('sheets', 'v4', credentials=creds).spreadsheets()

    @staticmethod
    def create_token(creds):
        with open('google_api_module/token.json', 'w') as token:
            token.write(creds.to_json())


class GoogleAPI:

    def __init__(self):
        self.service = GoogleCredentials().sheet_service

    def create_(self):
        spreadsheet_ = self.service.create(body={
            'properties': {'title': 'TABLE_SUMMER'},
            'sheets': [{'properties': {'sheetType': 'GRID',
                                       'sheetId': 0,
                                       'title': 'MAIN_LIST',
                                       }}]
        }).execute()
        return spreadsheet_.get('spreadsheetId')

    def append_data(self, data: list):
        """writing data after non-empty fields"""
        self.service.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=f'{NAME_LIST}!A1',
            valueInputOption="USER_ENTERED",
            body={'values': data}
        ).execute()

#
# if __name__ == '__main__':
#     a = GoogleAPI()

