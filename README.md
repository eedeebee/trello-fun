# trello-fun

Trello utilities built using the Trello REST API.  They read credentials from `keys.yml` of the form:

     Key: xxxxxxxxx
     Secret: yyyyyyyyyyyyy
     Token: xxxxxxxxxxxxxxxxxxxx

See Trello API authentication details.  The key and secret are used for read only activities.
The token needs to be a read/write capable token and is only needed and used by the am.py utility



## Assign Members 

    ./am.py -h --sourceBoardID [ID] --boardID [ID]

Copies all users and admins from source board to the specified board.

## Trello Search

Basic trello search tool.

    ./ts.py -h
