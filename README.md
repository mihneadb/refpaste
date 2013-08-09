refpaste
=========

command line client for refheap.com

Paste of the usage help string:

    usage: refpaste [-h] [--language LANGUAGE] [--private PRIVATE]
                    [--no-clipboard] [--username USERNAME] [--token TOKEN]
                    [--anonymous]
                    [path]

    Paste to http://www.refheap.com.

    positional arguments:
      path                  Path for file to paste.

    optional arguments:
      -h, --help            show this help message and exit
      --language LANGUAGE, -l LANGUAGE
                            Language for syntax highlighting. You can omit this
                            and will try to infer from the file ext.
      --private PRIVATE, -p PRIVATE
                            Whether to make the paste private.
      --no-clipboard, -n    If you don't want the URL in the clipboard.
      --username USERNAME, -u USERNAME
                            Username to associate paste with. Needs token!
      --token TOKEN, -t TOKEN
                            Token to verify username.
      --anonymous, -a       Paste anonymously.

You can also set up a JSON file in `~/.refpasterc` with a pair of your username
and token data, i.e.:

    {"username": "YOUR USERNAME", "token": "YOUR TOKEN"}

