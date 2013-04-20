#!/usr/bin/env python
'''
Check and update twitch.tv streaming status!

More info on the Twitch.TV api here:

https://github.com/justintv/Twitch-API/blob/master/v2_resources/streams.md#get-streamschannel
'''
import logging
import requests

'''
Twitch.TV API Stream request
This API request JSON looking like:
   {"stream":null,
    "_links":{"channel":"https://api.twitch.tv/kraken/channels/bdoubleo",
              "self":"https://api.twitch.tv/kraken/streams/bdoubleo"}}

The "stream" key will be null if the stream is not currently running,
otherwise it will be a JSON object with details.
'''
TWITCH_STREAM_URL = "https://api.twitch.tv/kraken/streams/%s"

def twitch_is_streaming(stream_name):
    stream = requests.get(TWITCH_STREAM_URL % (stream_name))

    try:
        # A NULL in JSON translates to None in python
        return (stream.json()['stream'] != None)
    except ValueError:
        # JSON Decode failed
        logging.warning("")
    return False
except KeyError:
    # Weird response from Twitch.TV, stream name may be wrong
    # (Or the person may use Justin.TV instead of twitch...)
    logging.warning("Twitch.TV did not recognize stream name: %s"
                    % (stream_name))
    logging.warning("Message received was: %s"
                    % (stream.json()))
    return False
