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
Started watching on:  Sun Jul  7 19:56:06 2019
--------------------------------------------------------------------------------
>>>> test1.txt found in directory. timestamp: Sun Jul  7 19:56:06 2019
>>>> test2.txt found in directory. timestamp: Sun Jul  7 19:56:06 2019


Scanning /Users/peter/Documents/code/dirwatcher/test on Sun Jul  7 19:56:06 2019...
Watched files:
{file name: last scanned line,...}
--------------------------------------------------------------------------------
{'test1.txt': 0, 'test2.txt': 0}
Scanning test/test1.txt
found 'hello' on line 1  timestamp: Sun Jul  7 19:56:06 2019
found 'hello' on line 7  timestamp: Sun Jul  7 19:56:06 2019
found 'hello' on line 16  timestamp: Sun Jul  7 19:56:06 2019
Scanning test/test2.txt
found 'hello' on line 4  timestamp: Sun Jul  7 19:56:06 2019
found 'hello' on line 20  timestamp: Sun Jul  7 19:56:06 2019


Scanning /Users/peter/Documents/code/dirwatcher/test on Sun Jul  7 19:56:08 2019...
Watched files:
{file name: last scanned line,...}
--------------------------------------------------------------------------------
{'test1.txt': 16, 'test2.txt': 20}
Scanning test/test1.txt
Scanning test/test2.txt


Scanning /Users/peter/Documents/code/dirwatcher/test on Sun Jul  7 19:56:10 2019...
Watched files:
{file name: last scanned line,...}
--------------------------------------------------------------------------------
{'test1.txt': 16, 'test2.txt': 20}
Scanning test/test1.txt
Scanning test/test2.txt
^CWARNING:__main__:Received SIGINT timestamp: Sun Jul  7 19:56:12 2019
INFO:__main__:Terminating dirwatcher -- keyboard interrupt signal
--------------------------------------------------------------------------------
Stopped watching on: Sun Jul  7 19:56:12 2019
Uptime was 6 seconds
--------------------------------------------------------------------------------

```