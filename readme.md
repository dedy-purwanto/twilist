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

    
    twilist.py send 3 

You will also be able to delete specific draft:    

    twilist.py del 3

You can also replace specific tweet draft:
    
    twilist.py rep 3 "New tweet" 

By default, all draft will be saved inside the same folder from which 
you run the twilist.py, but you can specify another source instead, 
using:

    twilist.py --file /path/to/twilist.txt


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

For example, I use twilist to store my tweet drafts, sync it using
Ubuntu One to get the same list at my home and my office, and run it
every 30 minutes, so in my bashrc I put these aliases

    alias twilist = '/usr/bin/twilist.py --file "$HOME/Ubuntu One/twilist.txt"'
    alias ta = 'twilist add'
    alias tl = 'twilist list'

I also soft-linked twilist.py to /usr/bin/. And to run it for every
30 minutes, in my crontab:

    30 * * * * /usr/bin/twilist.py --file "/home/kecebongsoft/Ubuntu One/twilist.txt" send
