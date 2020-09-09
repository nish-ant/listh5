# listh5

```
listh5 /path/to/file.h5
```

Python script to list hdf5 file keys

Also supports mat files (-v7+)

### Installation (Optional)
1. Clone the repository in a local directory.
2. Open `listh5` with a text editor and change the path to the script.
3. Place `listh5` in a desired directory (e.g. `$HOME/.local/bin/`). Check if the directory is included in `$PATH`: `echo $PATH`
4. Make the script executable: `chmod +x listh5`

listh5 requires [HDF5 for Python](https://www.h5py.org/).

### Instructions
These instructions apply when the python script is executed after following the above installation steps.

To run without the shell script, replace `listh5` with `python listh5.py` in the commands (e.g. `python listh5.py -h`).

```
Help: listh5 -h
Usage: listh5 [filepath] -h -n -d=[key] -s=[key] -sa -v 
         -h,--help          Display help
	 -n,--nolist		Disable output of list of keys
	 -d=?,--display=?	Value of passed 'key'
	 -s=?,--shape=?		Shape of passed 'key'
	 --sa,--shapeall	Shape of all keys
	 -v,--verbosity		Enable verbose display
```
