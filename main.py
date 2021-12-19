import praw

reddit = praw.Reddit(
    client_id="************",
    client_secret="**************",
    user_agent="<********>",
    username="*********",
    password="*************",
)

sub = reddit.subreddit("sub-name")


for submission in sub.new(limit=10):
    print("-----------")
    print(submission.title)
    title_lower = submission.title.lower()
    if "montevideo" in title_lower:
        for comment in submission.comments:
            
            if hasattr(comment, 'body'):
                comment_lower = comment.body.lower()
                count = 0
                if "muertevideo" in comment_lower:
                    count += 1
        if count == 0:
            submission.reply("muertevideo")
