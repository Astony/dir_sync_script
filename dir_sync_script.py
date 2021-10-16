import argparse
from time import sleep

from loguru import logger

from sync_func import sync_func


def dir_sync_script(source_path, rep_path, timer):
    while True:
        sync_func(source_path, rep_path)
        sleep(timer)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", type=str, help="path to source directory")
    parser.add_argument("replic_dir", type=str, help="path to the replic directory")
    parser.add_argument("timer", type=int, help="frequency of monitoring")
    parser.add_argument("log_path", type=str, help="path to log_file")
    args = parser.parse_args()

    logger.add(args.log_path, format="{time} {level} {message}")

    try:
        dir_sync_script(args.source_dir, args.replic_dir, args.timer)
    except KeyboardInterrupt:
        logger.info("Stop monitoring")
