#!/usr/bin/env python

"""reddman -- the Reddit<->Mailman bridge

Usage:
  reddman.py message (--file=<path> | -)
  reddman.py replies
  reddman.py -h | --help | --version

Options:
  message         read a message (from file or STDIN) and post it to reddit
  replies         scan for replies in reddit and post them to mailman
  -f --file=PATH  path to file to read as a message
  -h --help       show this help message and exit
  --version       show the version

"""

VERSION = '0.0.1'

from docopt import docopt
import praw

def replies():
  reddit = praw.Reddit(
    'reddman',
    user_agent = f'linux:reddman:v{VERSION} (by /u/igor_47')

  for submission in reddit.subreddit('moomers').hot(limit=10):
      print(submission.title)

def main(arguments):
  if arguments['message']:
    pass
  elif arguments['replies']:
    return replies()
  else:
    print("Invalid command; see --help for usage")

if __name__ == '__main__':
    arguments = docopt(__doc__, version=f'reddman.py version {VERSION}')
    main(arguments)
