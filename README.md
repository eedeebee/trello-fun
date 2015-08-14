# trello-fun

Trello utilities built using the Trello REST API.  They read credentials from `keys.yml` of the form:

     Key: xxxxxxxxx
     Secret: yyyyyyyyyyyyy
     Token: xxxxxxxxxxxxxxxxxxxx

See Trello API authentication details, in particular, [getting a key and a token](https://trello.com/docs/gettingstarted/index.html#getting-an-application-key).

The key and secret are used for read only activities.
The token needs to be a read/write capable token.


## Add member to organization boards

Examples:

    ./add-member-to-org-boards.py --help
    ./add-member-to-org-boards.py --member kristinyamauchi --namePattern Engineering
    ./add-member-to-org-boards.py --member kristinyamauchi --namePattern "Team Tea"  --role admin

## Copy Board Members 

Examples:

    ./cp-members.py --help
    ./cp-members.py --sourceBoardID [ID] --boardID [ID]

Copies all users and admins from source board to the specified board.

## Trello Search

Basic trello search tool.

    ./ts.py -h
