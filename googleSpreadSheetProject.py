import json
import sys
import time
import datetime
import grovepi
import math
import gspread
from oauth2client.service_account import ServiceAccountCredentials

sensor = 3
Google_JSON = 'ac04-589747e96b89.json' 
Google_Spreadsheet_Name = 'ac04-data'

#create a function that will connect to Google Spreadsheet
def open_google_spreadsheet(oauth_key_file, spreadsheet):
	try:
		scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
		credentials= ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
		gc = gspread.authorize(credentials)
		worksheet = gc.open(spreadsheet).sheet1
		return worksheet
	except Exception as ex:
		print('Problem logging in. Authorization failed.')
		sys.exit(1)

# function to read sensor data...
def read_sensor():
    [temp, hum] = grovepi.dht(sensor, 0)
    if ((math.isnan(temp) == False) and (math.isnan(hum) == False) and (hum >= 0)):
        time.sleep(1)
    return temp, hum

# clear the worksheet (initialize)
worksheet = None
count = 0
while True:
    # Login if necessary
    if worksheet is None:
        worksheet = open_google_spreadsheet(Google_JSON, Google_Spreadsheet_Name)

    # read sensor data...
    [temp, hum] = read_sensor()
    print('Temperature: {0:0.2f} C'.format(temp) + ' Humdity: {0:0.2f} %'.format(hum))

    # append the sensor data to the spreadsheet...
    try:
        worksheet.append_row((str(datetime.datetime.now()), temp, hum))
        count = count + 1
    except:
        print('Append error.')
        worksheet = None
        time.sleep(10)
        continue

    print('-> Record no. {0} '.format(count) + 'has been added to {0}'.format(Google_Spreadsheet_Name))
    time.sleep(10)







