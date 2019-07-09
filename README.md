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
2019-07-09 10:45:54.678 __main__     INFO     
----------------------------------------------------
Started dirwatcher.py.
----------------------------------------------------

2019-07-09 10:45:54.678 __main__     INFO     Scanning test for files ending in .txt that contain hello
2019-07-09 10:45:54.678 __main__     INFO     test3.txt added to watchlist.
2019-07-09 10:45:54.679 __main__     INFO     test/test3.txt: found 'hello' on line 13
^C2019-07-09 10:46:10.180 __main__     WARNING  Received SIGINT
2019-07-09 10:46:10.180 __main__     INFO     Terminating dirwatcher -- keyboard interrupt signal
2019-07-09 10:46:10.734 __main__     INFO     
----------------------------------------------------
Stopped watching
Uptime was 16 seconds
----------------------------------------------------
```