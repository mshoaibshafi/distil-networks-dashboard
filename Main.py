
import os,sys
from pprint import pprint
from extractDomains import extractDomains
from createDashboard import createDashboard
from convertCSV2HTML import convertCSV2HTML

# set the account ID as an envrionment variable
# $ export Account_ID=844001-xx-yy-zz
accountId = os.environ.get('Account_ID')

# Extract all domain names and their domain_IDs from Distil Account
extractDomains(accountId)

# Create CSV File for the Dashboard
createDashboard(accountId)

# Convert CSV file to HTML
convertCSV2HTML()