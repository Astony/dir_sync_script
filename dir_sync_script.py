import argparse
from time import sleep

from loguru import logger

from sync_func import sync_func


def dir_sync_script(source_path: str, rep_path: str, timer: int) -> None:
    """
    Directories synchronization with timer of synchronize

    :param source_path: Path to the directory in which the synchronization will take place
    :type source_path: str
    :param rep_path: Path to the directory - source copy
    :type rep_path: str
    :param timer: Time interval between synchronization
    :type timer: int
    :return: None
    """
    while True:
        sync_func(source_path, rep_path)
        sleep(timer)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", type=str, help="path to source directory")
    parser.add_argument("replic_dir", type=str, help="path to the replic directory")
    parser.add_argument("timer", type=int, help="time interval between synchronization")
    parser.add_argument("log_path", type=str, help="path to log_file")
    args = parser.parse_args()

    logger.add(args.log_path, format="{time} {level} {message}")
    logger.info("Start synchronization")
    try:
        dir_sync_script(args.source_dir, args.replic_dir, args.timer)
    except KeyboardInterrupt:
        logger.info("Stop synchronization")
    except TypeError:
        logger.error("Directory/directories doesn't exists")
    except Exception as err:
        logger.error(f"Error\n{err}\nwas raised")
