from datetime import datetime
from pytz import timezone

date = datetime.now(timezone('Asia/Tokyo'))
print(date)
