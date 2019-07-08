#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Watches input file extension in input directory for changes and
scans for input text string, re-checking every polling interval.
"""
__author__ = "p-mayor w/ help from piero"

import os
import argparse
import time
import signal
import logging
import errno

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)
watched_files = {}
exit_flag = False


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


def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT. Other signals can be mapped here
    as well (SIGHUP?)
    Basically it just sets a global flag, and main() will exit it's loop if
    the signal is trapped.
    """
    # log the associated signal name (the python3 way)
    logger.warning('Received ' + signal.Signals(sig_num).name)

    if signal.Signals(sig_num).name == 'SIGINT':
        logger.info('Terminating dirwatcher -- keyboard interrupt signal')

    if signal.Signals(sig_num).name == 'SIGTERM':
        logger.info('Terminating dirwatcher -- OS interrupt signal')

    global exit_flag
    exit_flag = True


def scan_file(file, start_line_num, search_text):
    '''read file and look for search text'''
    line_number = 0
    with open(file) as f:
        for line_number, line in enumerate(f):
            # watched_files[str(file.split('/')[1])] = line_number+1
            if line_number >= start_line_num:
                if search_text in line:
                    logger.info(
                        f"{file}: found '{search_text}' on"
                        f" line {line_number+1}"
                    )
    return line_number+1


def read_dir(directory, extension, search_text):
    '''read files in directory ending in extension and update watched_files'''
    file_list = os.listdir(directory)

    for f in file_list:
        if f.endswith(extension) and f not in watched_files:
            watched_files[f] = 0
            logger.info(f"{f} added to watchlist.")

    for f in list(watched_files):
        if f not in file_list:
            logger.info(f"{f} removed from watchlist.")
            del watched_files[f]

    for f in watched_files:
        watched_files[f] = scan_file(
            os.path.join(directory, f),
            watched_files[f],
            search_text
        )


def main():
    '''parses command line and launches forever while loop'''
    args = create_parser().parse_args()

    # Hook these two signals from the OS ..
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if OS sends either of these to my
    # process.

    start_time = time.time()
    logger.info("\n"
                "----------------------------------------------------\n"
                f"Started {__file__}.\n"
                "----------------------------------------------------\n")
    logger.info(
        "Scanning {} for files ending in {} that"
        " contain {}".format(args.dir, args.ext, args.text)
    )
    while not exit_flag:
        try:
            read_dir(args.dir, args.ext, args.text)
        except OSError as e:
            if e.errno == errno.ENOENT:
                logger.error(f"{args.dir} directory not found")
                time.sleep(5)
            else:
                logger.error(e)
        except Exception as e:
            logger.error(f"UNHANDLED EXCEPTION:{e}")
        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        time.sleep(int(args.int))

    end_time = time.time()
    logger.info("\n"
                "----------------------------------------------------\n"
                "Stopped watching\n"
                'Uptime was '+str(int(end_time-start_time))+' seconds\n'
                "----------------------------------------------------\n"
                )
    logging.shutdown()


if __name__ == '__main__':
    main()
