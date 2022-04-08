#datetime module
from datetime import timedelta,date

td = timedelta(days =365)
d = date.today()
print(d + td)