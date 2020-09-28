# RssToReddit

Get feed RSS post a link to a subreddit, just that.
This a modified version of https://github.com/skyride/reddit-rss-bot.git
Among the changes is that this is working on Python3, will create a logfile, 
and don't post the full text of the news, just the link.


## Installation
You want to try without messing with your system:
```
mkdir reddit
cd reddit
virtualenv .
source bin/activate
git clone https://github.com/kabutor/rss-to-reddit.git
cd rss-to-reddit
pip install -r requirements.txt
cp config.py.example config.py
```

Fill out config.py with your info, then stick checknews.py in your crontab.

## License

As the original code don't have any license stated I can't put this under any license, 
as is a derivate work from that code, that is a problem. I know.
