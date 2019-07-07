# Dirwatcher

A simple python 3 script that watches certain files in a directory for a certain text phrase and returns the line number where the phrase was found.

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
Started watching on: Sun Jul  7 18:55:49 2019


>>>> test4.txt found in directory. timestamp: {'Sun Jul  7 18:55:49 2019'}


>>>> test1.txt found in directory. timestamp: {'Sun Jul  7 18:55:49 2019'}


>>>> test2.txt found in directory. timestamp: {'Sun Jul  7 18:55:49 2019'}


Scanning /Users/peter/Documents/code/dirwatcher/test on Sun Jul  7 18:55:49 2019...
Watched files:
{file name: last scanned line,...}
--------------------------------------------------
{'test4.txt': 0, 'test1.txt': 0, 'test2.txt': 0}
found 'hello' on line 1 in file test/test4.txt. timestamp: Sun Jul  7 18:55:49 2019
found 'hello' on line 5 in file test/test4.txt. timestamp: Sun Jul  7 18:55:49 2019


Scanning /Users/peter/Documents/code/dirwatcher/test on Sun Jul  7 18:55:51 2019...
Watched files:
{file name: last scanned line,...}
--------------------------------------------------
{'test4.txt': 5, 'test1.txt': 0, 'test2.txt': 4}
^CWARNING:__main__:Received SIGINT


Stopped watching on: Sun Jul  7 18:55:55 2019
Overall uptime: 6 seconds

```