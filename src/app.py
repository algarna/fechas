from datetime import *
from dateutil.relativedelta import *

#Print actual date
now = datetime.now()
print(now)

#Print the new date after adding months, weeks and hours
now = now + relativedelta(months=1, weeks=1, hours=5)
print(now)
