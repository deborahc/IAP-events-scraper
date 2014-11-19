from lxml import html
from lxml.html import parse
import time
import requests

path = 'http://student.mit.edu/iap/nc'
end_path = '.html'
total_events = 0
event_names = []
event_number = 1
for i in range(1,49):
    time.sleep(1)
    url = path + str(i) + end_path
    doc = parse(url).getroot()
    activities = doc.cssselect('div.activity')
    for activity in activities:
        event_name = activity.find('h3').text_content()
        if event_name not in event_names:
            event_names.append(event_name)
            total_events += 1
            print "At " + url + ": " + str(event_number) + " : " + event_name
            event_number +=1 
print "total events: " + str(total_events)
