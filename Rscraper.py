#!/user/bin/env python3

import re
import praw
import scraperConfig as cfg


reddit = praw.Reddit(client_id=cfg.client_id,
                    client_secret=cfg.client_secret,
                    user_agent="comment scraper:69:1.0 (by /u/Node_Node_Node)")

"""
for id in cfg.uniq_ids:
    submission = reddit.submission(id=id)

    submission.comments.replace_more(limit=0)

    with open("text.txt", "w", encoding="utf-8") as f:
        for comment in submission.comments.list():
            f.write(comment.body)


submission = reddit.submission(id=cfg.target)

submission.comments.replace_more(limit=None, threshold=5)

with open("target.txt", "w", encoding="utf-8") as f:
    for comment in submission.comments.list():
        f.write(comment.body)

"""

for comment in reddit.subreddit('politics').stream.comments():
    print(comment.body)
