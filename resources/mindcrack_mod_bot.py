#!/usr/bin/env python
'''
Created on Mar 7, 2013

@author: Martin-PC8

This is a program that searches for videos from youtube channels and posts
them to reddit.

Error 1: Could not submit because the post was already submitted.
'''
import praw
import logging
import getpass
import re
import time

# Import local project files into the global namespace:
from mindcrackers import *
from youtube import *
from twitch import *

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

username = raw_input("username")
password = getpass.getpass("password")
subreddit_name = raw_input("subreddit")

# Setting up PRAW
logging.info("Setting up PRAW...")
r = praw.Reddit(user_agent='YouReddit:D /u/martincharles07/')
logging.info("Signing in...")
logging.debug("Signing in with: " + username + "and password:" + password)
r.login(username, password)
logging.info("Sign in Sucessful!")

subreddit = r.get_subreddit(subreddit_name)

streamers = []

for (name, youtube, twitch) in mindcrackers:
    logging.info("Updating: %s (Youtube: %s, Twitch: %s)"
                 % (name, youtube, twitch))

    if youtube:
        YoutoRedditBot(r, youtube, subreddit_name, name)
    else:
        logging.info("Skipping YouTube channel")

        if twitch:
            if twitch_is_streaming(twitch):
                streamers.append((name, "//twitch.tv/%s" % (twitch)))
                logging.info("%s is streaming!" % (name))
            else:
                logging.info("Skipping Twitch stream")

# Get sidebar
settings = subreddit.get_settings()
sidebar = settings['description']

# Markers used are [](#BOT_STREAMS) and [](/BOT_STREAMS)
opening_marker = "[](#BOT_STREAMS)"

# Remove text between markers
sidebar = re.sub(r'(\[\]\(#BOT_STREAMS\)).*(\[\]\(/BOT_STREAMS\))',
                 '\\1\\2',
                 sidebar)

if streamers:
    links = map(lambda (name, url): "[%s](%s)" % (name, url), streamers)

    streamers_msg = " | **Now Streaming:** " + (", ".join(links))

    try:
        marker_pos = sidebar.index(opening_marker) + len(opening_marker)
    sidebar = sidebar[:marker_pos] + streamers_msg + sidebar[marker_pos:]
except ValueError:
    # Substring not found
    logging.warning("No streams marker found.")

'''
 Apply sidebar changes
 Note that this causes the following to be logged in console:
   :0: UserWarning: Extra settings fields: [u'submit_text_label',
   u'submit_link_label', u'exclude_banned_modqueue']
This seems to be completely benign, perhaps praw is not completely up to date
subreddit.update_settings(description=sidebar)
'''

logging.info("All done")
time.sleep(5)
