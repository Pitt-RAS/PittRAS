# File-Size-Scanner

This script will recursively search all files and directories in a user-specified path and then flag each file that is over a certain size (provided in bytes by the user). 

## Python

Tested using python 3.9.4 on Windows 10. 

## Issues

Sometimes os.path.getsize() returns zero, when the file is definitely not zero. The program will print out any files that get marked as zero bytes so the user can manually check them. 

Additionally, be aware of the size that is returned for directories. See https://stackoverflow.com/questions/10404534/os-path-getsize-returns-incorrect-value. 

## Uses

Can be used for website development to ensure images and other media content aren't too large.