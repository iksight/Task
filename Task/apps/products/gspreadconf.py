import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']


credentials = ServiceAccountCredentials.from_json_keyfile_name('Task/apps/products/credentials.json', scope)
gs = gspread.authorize(credentials)
