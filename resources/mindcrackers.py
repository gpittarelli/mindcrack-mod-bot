f#!/usr/bin/env python
'''
Defines a list of the members of the mindcrack community.

Each Mindcracker is represented as a tuple of:

(name, youtube channel name, twitch user name)

Note that the name (first field) is also used as the user's flair
class in the subreddit.

If the youtube/twitch name is missing, then that site will not be
queried and updated for that user. (If some mindcrackers don't want
videos auto posted). For future reference, these lines are marked with
comments including the missing field.

'''

mindcrackers = [
    ("Adlington", "adlingtont", ""), # No twitch
    ("Anderzel", "", "anderzel"), # YT: imanderzel
    ("Arkas", "ArkasMc", "mc_arkas"),
    ("Avidya", "AvidyaZen", "AvidyaZEN"),
    ("Baj", "w92baj", "w92baj"),
    ("BdoubleO", "bdoubleo100", "bdoubleo"),
    ("BlameTheController", "BlameTheController", "blamethecontroller"),
    ("Docm", "", "docm77live"), # YT: docm77
    ("Etho", "ethoslab", "ethotv"),
    ("Generikb", "generikb", "generikb"),
    ("Guude", "guudeboulderfist", "guude"),
    ("Jsano", "jsano19", ""), # Has a justin.tv (jsano19), not twitch...
    ("Kurt", "", "kurtjmac"), # YT: kurtjmac
    ("MCGamer", "supermcgamer", "SuperMCGamer"),
    ("Millbee", "MillBeeful", "millbee"),
    ("Mhykol", "mhykol", "mhykol"),
    ("Nebris", "nebris88", "nebris"),
    ("Pakratt", "pakratt13", ""), # No twitch
    ("PaulSoaresJr", "paulsoaresjr", ""), # No twitch
    ("Pause", "pauseunpause", "pauseunpause"),
    ("Pyrao", "Pyropuncher", "pyropuncher"),
    ("Shreeyam", "ShreeyamNET", "shreeyamnet"),
    ("TheJims", "", "thejimslp"), # YT: thejims
    ("VintageBeef", "", "vintagebeef"), # YT: vintagebeef
    ("Zisteau", "", "zisteau1"), # YT: zisteau
]


#YoutoRedditBot("xisumavoid","hermitcraft")
#YoutoRedditBot("sethbling","minecraft")
#YoutoRedditBot("Keralis","hermitcraft")
#YoutoRedditBot("SlamacowCreations","minecraft")
#YoutoRedditBot("digbuildlive","minecraft")
#YoutoRedditBot("elementanimation","minecraft")
#YoutoRedditBot("animationcraftpg5","minecraft")
