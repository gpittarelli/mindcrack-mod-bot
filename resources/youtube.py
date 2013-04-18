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
import getpass

logging.basicConfig(format='%(levelname)s:%(message)s',level = logging.INFO)

username = raw_input("username")
password = getpass.getpass("password")

#Setting up PRAW
logging.info ("Setting up PRAW...")
r = praw.Reddit(user_agent='YouReddit:D /u/martincharles07/')
logging.info ("Signing in...")
logging.debug ("Signing in with: " + username + "and password:" + password)
r.login(username, password)
logging.info ("Sign in Sucessful!")


def YoutoRedditBot(channel,subreddit,flair):

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

    #Erase File
    f.close()
    os.remove(channel + '.dat')

    logging.info("Checking for duplication")
    logging.debug (url)


    #Checking double posting
    tnt = (r.search(title, subreddit=subreddit, sort=None, limit=0))
    o = open ('Submissions.dat', 'w+')
    for submission in tnt:
        o.write (str(submission) + os.linesep)
    o.close()

    # Search file for matches and tries to post
    if search('Submissions.dat', title) == False:
            logging.debug ('Submitting...')
            os.remove('Submissions.dat')
            try:
                flairyfairy = r.submit(subreddit,title,url = url)
            except praw.errors.AlreadySubmitted:
                logging.warning ("Failed to submit (error 1)")
                return False
            else:
                logging.info("Submitted successfully")
                logging.info("Trying to flair")
                try:
                    r.get_subreddit(subreddit).set_flair(flairyfairy,flair)
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


YoutoRedditBot("adlingtont","MindcrackModBot","Adlington")
YoutoRedditBot("ArkasMc","MindcrackModBot","Arkas")
YoutoRedditBot("AvidyaZen","MindcrackModBot","Avidya")
YoutoRedditBot("w92baj","MindcrackModBot","Baj")
YoutoRedditBot("bdoubleo100","MindcrackModBot","BdoubleO")
YoutoRedditBot("BlameTheController","MindcrackModBot","BlameTheController")
YoutoRedditBot("ethoslab","MindcrackModBot","Etho")
YoutoRedditBot("generikb","MindcrackModBot","Generikb")
YoutoRedditBot("guudeboulderfist","MindcrackModBot","Guude")
YoutoRedditBot("jsano19","MindcrackModBot","Jsano")
YoutoRedditBot("supermcgamer","MindcrackModBot","MCGamer")
YoutoRedditBot("MillBeeful","MindcrackModBot","Millbee")
YoutoRedditBot("mhykol","MindcrackModBot","Mhykol")
YoutoRedditBot("nebris88","MindcrackModBot","Nebris")
YoutoRedditBot("pakratt13","MindcrackModBot","Pakratt")
YoutoRedditBot("paulsoaresjr","MindcrackModBot","PaulSoaresJr")
YoutoRedditBot("pauseunpause","MindcrackModBot","Pause")
YoutoRedditBot("Pyropuncher","MindcrackModBot","Pyrao")
YoutoRedditBot("ShreeyamNET","MindcrackModBot","Shreeyam")
#YoutoRedditBot("xisumavoid","hermitcraft")
#YoutoRedditBot("sethbling","minecraft")
#YoutoRedditBot("Keralis","hermitcraft")
#YoutoRedditBot("SlamacowCreations","minecraft")
#YoutoRedditBot("digbuildlive","minecraft")
#YoutoRedditBot("elementanimation","minecraft")
#YoutoRedditBot("animationcraftpg5","minecraft")

import time
logging.info ("All done")
time.sleep(5)
