Mindcrack Mod Bot
=================

Github Project for the Mindcrack Mod Bot

The Goal of the MindcrackModBot project is twofold.

* First, to create an extensible, web configurable bot similar to AutoModerator, and document its functions extensively.
* The second is to implement that bot along the functions needed by the /r/mindcrack subreddit.

Functions (Web Interface)
======
Log in, multiple users, either on the same server as the bot, coded in php and utilizing a mySQL database to store conditions for the bot to fulfill on each run, including special timed runs and actions. Also able to change the bot's credentials and test that the bot can successfully login and run.

Functions (Bot)
======
Coded in python, the bot reads conditions from a database and fulfills them on the desired subreddit.
