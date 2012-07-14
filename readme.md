twilist
=======================
twilist is a tool to help me send my tweet draft by having a list of
tweet in a text file.

Adding a tweet to a list:
    
    twilist.py add "Foo bar"
    
Sending a tweet in a list (first in first out):
    
    twilist.py send
    

Sending the first tweet item in the list:
    
    twilist.py send first
    

Sending the last tweet item in the list:
    
    twilist.py send last
    

Sending random tweet item in the list:
    
    twilist.py send rand
    

List of tweet:
    
    twilist.py list
    

This will return a list of tweet and it's index, and then you can look
at the index and send a specific item with this command:

    
    twilist.py send 3 (index value)
    

Requirements
------------------------
Twilist require you to have twidge in your system and already set up
with your account

All twilist data will be saved in "twilist" file inside the folder you
run the command from.

Why?
------------------------
I often have a lots to say in twitter, but sending all of them at
once might be annoying for others to see, so I want to keep them 
somewhere and send them at the time I want it (not scheduled), that way
I can store my thoughts right away and not losing it because writing it
later might spoil my mood.

So then twilist will coming handing, I set up aliases "twa" for 
"twilist.py add" and "twilist" for "twilist.py" in my bashrc, and
run the command in my Ubuntu One folder to make sure that the tweet
data are syncronized between my home computer and my office computer.

And  "twilist.py send" can also attached to cronjob if we want to 
schedule the tweet
