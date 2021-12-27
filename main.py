# First we import praw

import praw

# Here we introduce the bot's account's data 

reddit = praw.Reddit(
    client_id="************",
    client_secret="**************",
    user_agent="<********>",
    username="*********",
    password="*************",
)

# And this is the actual code

sub = reddit.subreddit("sub-name")

# Iterating trough the subreddit's post in a chronological order
for submission in sub.new(limit=10):
    
    # Checking if the post's title contains the word we are looking for
    title_lower = submission.title.lower()
    
    if "montevideo" in title_lower:
        
        # We should iterate again, but this time in the post's comments in order to check if the bot has already commented in this post since we don't like flood.
        for comment in submission.comments:
            if hasattr(comment, 'body'):
                comment_lower = comment.body.lower()
                count = 0
                if "muertevideo" in comment_lower:
                    count += 1
                    
        # If we don't find any "muertevideo" comment we reply the post with the mentioned word.
        if count == 0:
            submission.reply("muertevideo")
