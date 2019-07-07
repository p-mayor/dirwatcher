#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Watches the given directory for changes
"""
__author__ = "p-mayor"

import os
import argparse
import time
import signal
import logging


watched_files = {}
exit_flag = False


def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT. Other signals can be mapped here
    as well (SIGHUP?)
    Basically it just sets a global flag, and main() will exit it's loop if
    the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    # log the associated signal name (the python3 way)
    logger.warning('Received ' + signal.Signals(sig_num).name)

    global exit_flag
    exit_flag = True


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Watch input directory for file changes')
    parser.add_argument("-d", "--dir", default=".",
                        help="directory to be watched, defaults to '.'")
    parser.add_argument("-i", "--int", default=1,
                        help="polling interval, defaults to 1 second")
    parser.add_argument("-e", "--ext", default='.txt',
                        help="extension to be watched, defaults to .txt")
    parser.add_argument("text", help="text to be found")
    return parser


def scan_file(file, start_line_num, search_text):
    '''read file and look for search text'''
    line_number = 0
    with open(file) as f:
        for line_number, line in enumerate(f):
            if line_number >= start_line_num:
                if search_text in line:
                    watched_files[str(file.split('/')[1])] = line_number+1
                    print(f"found '{search_text}' on line {line_number+1}")
    return line_number+1


def read_dir(directory, extension):
    '''read files in directory ending in extension and update watched_files'''
    file_list = os.listdir("./"+directory)

    for f in file_list:
        if f.endswith(extension) and f not in watched_files:
            watched_files[f] = 0
    for f in watched_files:
        if f not in file_list:
            del watched_files[f]
    print(watched_files)


def main():
    args = create_parser().parse_args()
    print(args)

    # hint code:
    # Hook these two signals from the OS ..
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if OS sends either of these to my
    # process.

    start_time = time.time()
    print('\n\nStarted watching on:'+time.asctime(time.localtime(time.time())))
    while not exit_flag:
        try:
            read_dir(args.dir, args.ext)
            for f in watched_files:
                scan_file(args.dir+"/"+f, watched_files[f], args.text)
        except Exception as e:
            print(e)
            # This is an UNHANDLED exception
            # Log an ERROR level message here
        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        time.sleep(int(args.int))

    # final exit point happens here
    # Log a message that we are shutting down
    print('\n\nStopped watching on:'+time.asctime(time.localtime(time.time())))
    # Include the overall uptime since program start.
    end_time = time.time()
    print('Overall uptime: '+str(int(end_time-start_time))+' seconds')


if __name__ == '__main__':
    main()
