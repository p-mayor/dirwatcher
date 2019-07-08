# Dirwatcher

A long running python 3 program that monitors certain file extensions in a directory for a certain text phrase.

## Arguments


```
positional arguments:
  text               text to be found

optional arguments:
  -h, --help         show this help message and exit
  -d DIR, --dir DIR  directory to be watched, defaults to '.'
  -i INT, --int INT  polling interval, defaults to 1 second
  -e EXT, --ext EXT  extension to be watched, defaults to .txt

```


## Example Usage

`python dirwatcher.py -d test -i 2 -e .txt hello`

- this starts watching the directory `./test` with a polling interval of 2 seconds, looking in only files with the extension '.txt' for the phrase 'hello'

## Example Output 

```
--------------------------------------------------------------------------------
Started watching on:  Sun Jul  7 20:28:43 2019
--------------------------------------------------------------------------------
Scanning /Users/peter/Documents/code/dirwatcher/test on Sun Jul  7 20:28:43 2019...
>>>> test1.txt found in directory. timestamp: Sun Jul  7 20:28:43 2019
>>>> test2.txt found in directory. timestamp: Sun Jul  7 20:28:43 2019
>>>> test3.txt found in directory. timestamp: Sun Jul  7 20:28:43 2019
Watched files:
{file name: last scanned line}
{'test1.txt': 0, 'test2.txt': 0, 'test3.txt': 0}
Scanning test1.txt...
Scanning test2.txt...
found 'hello' on line 1  timestamp: Sun Jul  7 20:28:43 2019
found 'hello' on line 6  timestamp: Sun Jul  7 20:28:43 2019
Scanning test3.txt...
found 'hello' on line 13  timestamp: Sun Jul  7 20:28:43 2019
--------------------------------------------------------------------------------
Scanning /Users/peter/Documents/code/dirwatcher/test on Sun Jul  7 20:28:45 2019...
Watched files:
{file name: last scanned line}
{'test1.txt': 0, 'test2.txt': 6, 'test3.txt': 19}
Scanning test1.txt...
Scanning test2.txt...
Scanning test3.txt...
--------------------------------------------------------------------------------
Scanning /Users/peter/Documents/code/dirwatcher/test on Sun Jul  7 20:28:47 2019...
Watched files:
{file name: last scanned line}
{'test1.txt': 0, 'test2.txt': 6, 'test3.txt': 19}
Scanning test1.txt...
Scanning test2.txt...
Scanning test3.txt...
^CWARNING:__main__:Received SIGINT timestamp: Sun Jul  7 20:28:47 2019
INFO:__main__:Terminating dirwatcher -- keyboard interrupt signal
--------------------------------------------------------------------------------
Stopped watching on: Sun Jul  7 20:28:49 2019
Uptime was 6 seconds
--------------------------------------------------------------------------------

```