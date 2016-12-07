#!/usr/bin/python
from pylab import *
from matplotlib.finance import quotes_historical_yahoo
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import datetime
date1 = datetime.date( 2012, 1, 1 )
date2 = datetime.date( 2015, 3, 23 )

daysFmt = DateFormatter('%m-%d-%Y')

quotes = quotes_historical_yahoo('MSFT', date1, date2)
if len(quotes) == 0:
    raise SystemExit

dates = [q[0] for q in quotes]
opens = [q[1] for q in quotes]

fig = figure()
ax = fig.add_subplot(111)
ax.plot_date(dates, opens, '-')

# format the ticks
ax.xaxis.set_major_formatter(daysFmt)
ax.autoscale_view()

# format the coords message box
def price(x): return '$%1.2f'%x
ax.fmt_xdata = DateFormatter('%Y-%m-%d')
ax.fmt_ydata = price
ax.grid(True)

fig.autofmt_xdate()
show()