import argparse
import json
import os
import urllib2
import urllib
import sys

from subprocess import Popen, PIPE


def get_ext(path):
    name, ext = os.path.splitext(path)
    return ext

def save_in_clipboard(string):
    if sys.platform == 'darwin':
        cmd = 'pbcopy'

    p = Popen([cmd], stdin=PIPE)
    p.communicate(input=string)

def main():
    parser = argparse.ArgumentParser(description="Paste some stuff.")
    parser.add_argument('path',
                        nargs='?', default=None,
                        help="Path for file to paste.")
    parser.add_argument('--language', '-l',
                        dest='language', default=None,
                        help="Language for syntax highlighting")
    parser.add_argument('--private', '-p',
                        dest='private', default=False,
                        help="Whether to make the paste private")
    parser.add_argument('--no-clipboard', '-n', action='store_true',
                        dest='no_clipboard', default=False,
                        help="If you don't want the URL in the clipboard")

    args = parser.parse_args()
    data = {}
    data['private'] = args.private

    if args.path:
        with open(args.path, 'r') as f:
            data['contents'] = f.read()
        data['language'] = args.language if args.language else get_ext(args.path)
    else:
        data['contents'] = sys.stdin.read()
        data['language'] = args.language if args.language else 'Plain Text'

    req = urllib2.urlopen("https://www.refheap.com/api/paste",
                          data=urllib.urlencode(data))
    response = json.loads(req.read())
    url = response['url']

    if args.no_clipboard:
        print "Pasted at %s." % url
    else:
        save_in_clipboard(url)
        print "Saved %s in your clipboard." % url


if __name__ == '__main__':
    main()