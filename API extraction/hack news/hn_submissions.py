import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

submission_ids = r.json()
print(submission_ids)# contents in r are reading paper ids
submission_dicts = []
for submission_id in submission_ids[:30]:
    #get first 30 reading IDs
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    print(response_dict.keys())
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                              reverse=True)

    for submission_dict in submission_dicts:
        print("\nTitle:", submission_dict['title'])
        print("Discussion link:", submission_dict['link'])
        print("Comments:", submission_dict['comments'])


