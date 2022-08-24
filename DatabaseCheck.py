import mysql.connector
import os
from datetime import datetime

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

# Get Current Date
now = datetime.now()
startdttm = now.strftime("%Y-%m-%d") + ' 00:00:00'
# startdttm = '2021-03-15 00:00:00'

# Connect to Mysql Db
mydb = mysql.connector.connect(
  host="dbsrp3128",
  user="",
  password="",
  database="dtcr01"
)

mycursor = mydb.cursor()
select_stmt = "SELECT JobType, HierarchyNodeId, StartDttm, EndDttm, Success FROM btch_refreshlog WHERE startdttm >= %(startdttm)s"
mycursor.execute(select_stmt, {'startdttm': startdttm})

refreshLogResults = mycursor.fetchall()

for refreshLogResult in refreshLogResults:
  if (refreshLogResult[4] != 1):
      print(refreshLogResult)
      notify("Cache Job Failure", "Cache Job Failed")

mydb.close()
