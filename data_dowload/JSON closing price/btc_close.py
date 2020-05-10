
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
try:
    # Python 2.x
    from urllib2 import urlopen
except ImportError:
    # Python 3.x
    from urllib.request import urlopen
import json
import requests
import pygal
import math
from itertools import groupby

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)
file_requests = req.json()

filename = 'btc_close_2017_request.json'
with open(filename) as f:
    btc_data = json.load(f)
dates, months,weeks,weekdays,closes =[],[],[],[],[]
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))
    dates.append(date)
    months.append(month)
    weeks.append(week)
    weekdays.append(weekday)
    closes.append(close)
    print("{} is month {} week {}, {}, the close price is {} RMB".format(
        date, month, week, weekday, close))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = 'Close (¥)'
line_chart.x_labels = dates
N = 20  #every 20 days
line_chart.x_labels_major = dates[::N]
line_chart.add('Close', closes)
line_chart.render_to_file('Close Chart（¥）.svg')

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = 'Close Log(¥)'
line_chart.x_labels = dates
N = 20  #every 20 days
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(value) for value in closes]
line_chart.add('Close_Log', close_log)
line_chart.render_to_file('Close Log Chart（¥）.svg')


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):  # 2
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = [str(x) for x in x_unique]
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month],closes[:idx_month],'Monthly Close Average（¥)','Month Average')
line_chart_month

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(
    weeks[1:idx_week], closes[1:idx_week], 'Weekly Close Average（¥)', 'Week Average')
line_chart_week


idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday',
      'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(
    weekdays_int, closes[1:idx_week], 'Weekdays Close Average', 'Weekdays Average')
line_chart_weekday.x_labels = wd
line_chart_weekday.render_to_file('Weekdays Average.svg')
line_chart_weekday


with open('Close Value Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write(
        '<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
            'Close Chart（¥）.svg', 'Close Log Chart（¥）.svg', 'Monthly Close Average（¥)',
            'Weekly Close Average（¥)', 'Weekdays Average.svg'
    ]:
        html_file.write(
            '    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))  # 1
    html_file.write('</body></html>')
