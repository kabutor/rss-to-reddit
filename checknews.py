import json
import time
import praw
import feedparser
import html2text

import config
from datetime import datetime

# Create reddit client
reddit = praw.Reddit(
    client_id=config.reddit['client_id'],
    client_secret=config.reddit['client_secret'],
    user_agent=config.reddit['user_agent'],
    username=config.reddit['username'],
    password=config.reddit['password']
)
subreddit = reddit.subreddit(config.reddit['subreddit'])

reddit.validate_on_submit = True

# Get history
# History is just a basic dict saved to a json file.
# The key is the feed name and value is the unique title of the most recently posted entry
try:
    with open(config.historyfile) as data_file:
        history = json.load(data_file)
except IOError:
    history = {}

# Parse feeds
for name, url in config.feeds:
    # Check if we have history
    if name not in history:
        history[name] = ""

    # Check if we have a new entry to post
    try:
        feed = feedparser.parse(url)
        if feed['entries'][0]['title'] != history[name]:
            # Check its not just a blank because it's a first run
            entry = feed['entries'][0]
            _link = entry['link']
            _title = entry['title']
            history[name] = entry['title']
            
            submission = subreddit.submit(
                title = _title,
                selftext=None,
                url=_link ,
                send_replies=config.reddit['send_replies']
            )
            now = datetime.now()
            _localtime = now.strftime("%d/%m/%Y %H:%M:%S")
            f = open( config.logfile , "a")
            f.write( _localtime + ":" + submission.title + "\n")
            f.close()
            print ("Submitted: %s" % submission.title)
            time.sleep(10)
    except Exception as e:
            fp = open( config.logfile + "err" , "a")
            fp.write( _localtime + ":" + e + "\n")
            fp.close()
            print (e)

        

# Write the history file back to disk
with open(config.historyfile, "w") as data_file:
    data_file.write(json.dumps(history))
