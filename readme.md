twilist is a tool to help me send my tweet draft by having a list of
tweet in a text file.

Adding a tweet to a list:
    
    twilist.py "Foo bar"
    
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
    

