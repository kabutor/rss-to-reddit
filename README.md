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

## FAQ
# Q - ¿Can you choose picture from the RSS to be shown as thumbnail on the reddit post? #
A - I don't think it's possible, when you sumbit something to reddit (manually or via the API) you only have three options, text (no image), a picture(and then only the picture is shown) or a URL, that is what I use on the script.
When you submit a URL to reddit, that is parsed and some picture from there is used as a thumbnail on reddit, the poster has no control (AFAIK) , of the thumbnail that reddit select to be shown. 

# Q - ¿Can I see an example of the script in action? #
A - You can check https://www.reddit.com/r/planetaludico is a boardgame subreddit, the user https://www.reddit.com/user/PL_poster/ is the bot, everything posted by that bot is automatically generated from a list of blogs, podcast, and youtube channels using this script.
