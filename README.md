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


## Example usage

`python dirwatcher.py -d test -i 2 -e .txt hello`

- this starts watching the directory `./test` with a polling interval of 2 seconds, looking in only files with the extension '.txt' for the phrase 'hello'