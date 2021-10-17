# Introduction #

__dir_sync_script__ is a console utility that performs one-way synchronization of the contents of the two folders: source and replica.
_______________________________________________________________________________________________________________________________________________________________________
## Functionality ##


+ Creates/deletes a folder in the replica directory if this folder doesn't exist in the source directory.


+ Copies/deletes a folder in the replica directory if this folder doesn't exist in the source directory.


+ Keeps track of the content of the files.


+ Prints all changes to the console and saves them to the log file.



____________________________________________________________________________________________________________________________________
## Parameters ##

1) source_dir: str

     A path to source directory.


2)  replic_dir: str

    A path to replic directory.


3)  timer: int

    A time interval between synchronization in seconds.


4)   log_path: str

     A path to log file.

_______________________________________________________________________________________________
## Usage ##

To run this utility, enter in the console:

``python3 <path-to-script>/dir_sync_script.py <path-to-source-dir> <path-to-replica-dir> <time-of-synchronization (in seconds)> <path-to-log-file>``

To stop this utility, press the ``Ctrl+C`` key combination in the console:
