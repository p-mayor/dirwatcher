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
Started watching on: Sun Jul  7 16:57:48 2019


Scanning test...
{file name: last scanned line,...}
{'test1.txt': 0, 'test2.txt': 0, 'test3.txt': 0}
found 'hello' on line 1 in file test/test1.txt. timestamp: Sun Jul  7 16:57:48 2019
found 'hello' on line 7 in file test/test2.txt. timestamp: Sun Jul  7 16:57:48 2019
found 'hello' on line 17 in file test/test2.txt. timestamp: Sun Jul  7 16:57:48 2019

Scanning test...
{file name: last scanned line,...}
{'test1.txt': 1, 'test2.txt': 17, 'test3.txt': 0}
^CWARNING:__main__:Received SIGINT


Stopped watching on: Sun Jul  7 16:57:54 2019
Overall uptime: 6 seconds

```