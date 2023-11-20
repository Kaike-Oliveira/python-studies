# Calculate time

# Imports
from datetime import datetime
from dateutil.relativedelta import relativedelta

VALUE = 1000000
FORMAT = '%m/%d/%Y'
START_TIME = datetime.strptime('12/20/2023', FORMAT)
FINAL_TIME = START_TIME + relativedelta(years=5)
PERIOD = relativedelta(FINAL_TIME, START_TIME).years * 12

installments = 1
current_installments = START_TIME

while current_installments < FINAL_TIME:
    current_installments += relativedelta(months=1)
    print(f'{installments}X - {current_installments} - ${VALUE / PERIOD:,.2f}')
    installments += 1
