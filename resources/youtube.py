#!/usr/bin/env python
'''
Created on Mar 7, 2013

@author: Martin-PC8

This is a program that searches for videos from youtube channels and posts
them to reddit.

Error 1: Could not submit because the post was already submitted.
'''
import gdata.youtube.service
import praw
import os
import logging

def YoutoRedditBot(r, channel, subreddit_name, flair):
    def WriteEntryDetails(entry):
        f.write(entry.media.title.text + os.linesep)
        f.write(entry.published.text + os.linesep)
        f.write(entry.media.player.url + os.linesep)

    def GetAndWritetUserUploads(username):
        logging.info("Searching " + username)
        yt_service = gdata.youtube.service.YouTubeService()
        uri = 'http://gdata.youtube.com/feeds/api/users/%s/uploads' % username
        WriteVideoFeed(yt_service.GetYouTubeVideoFeed(uri))

    def WriteVideoFeed(feed):
        for entry in feed.entry:
            WriteEntryDetails(entry)

    def search (filetosearch, query):
        with open(filetosearch, 'r') as inF:
            for line in inF:
                if query in line:
                    return True
        return False


    f = open(channel + '.dat', 'w+')
    logging.debug("Searching " + channel + "...")
    GetAndWritetUserUploads(channel)
    f.close()
    f = open (channel + '.dat', 'r')

    title = f.readline()
    f.readline()
    url = f.readline()

    # Erase File
    f.close()
    os.remove(channel + '.dat')

    logging.info("Checking for duplication")
    logging.debug (url)


    # Checking double posting
    tnt = (r.search(title, subreddit=subreddit_name, sort=None, limit=0))
    o = open ('Submissions.dat', 'w+')
    for submission in tnt:
        o.write (str(submission) + os.linesep)
    o.close()

    # Search file for matches and tries to post
    if search('Submissions.dat', title) == False:
        logging.debug ('Submitting...')
        os.remove('Submissions.dat')
        try:
            flairyfairy = r.submit(subreddit_name,title,url = url)
        except praw.errors.AlreadySubmitted:
            logging.warning ("Failed to submit (error 1)")
            return False
        else:
            logging.info("Submitted successfully")
            logging.info("Trying to flair")
            try:
                r.get_subreddit(subreddit_name).set_flair(flairyfairy,flair)
            except praw.errors.ModeratorOrScopeRequired:
                logging.warning("Failed to flair!")
            else:
                logging.info("Flaired successfully")
            finally:
                return True
    else:
        os.remove('Submissions.dat')
        logging.warning ("Failed to submit (error 1)")
        return False
