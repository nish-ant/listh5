#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@program: listh5.py

@task: Function to list hdf5 file keys

"""

import h5py
import scipy.io as sio
import getopt
import sys
import os

def read_hdf5(path, saflag):
    keys = []
    with h5py.File(path, 'r') as hf:
        hf.visit(keys.append)
        for key in keys:
            kstr = hf[key].name
            is_grp = False
            try:
                is_dataset = isinstance(hf[kstr], h5py.Dataset)
            except:
                is_grp = True
                is_dataset = False
            if is_dataset:
                if kstr[0] != '_':
                    if not saflag:
                        print(kstr)
                    else:
                        dset = hf[kstr][()]
                        shp = dset.shape
                        sstr = shp if len(shp)>0 else "1 (scalar)"
                        print("{0} : {1}".format(kstr, sstr))
    return None

def read_mat(path, saflag):
    ismat = False
    try:
        dset = sio.loadmat(path)
        ismat = True
    except NotImplementedError:
        read_hdf5(path, saflag)
    except:
        ValueError('File not readable')
    #
    if ismat:
        for key in dset.keys():
            if key[0] != '_':
                if not saflag:
                    print(key)
                else:
                    print("{0} : {1}".format(key, dset[key].shape))                    
    return None
    
#-----------------------------------------------------------------------
# Additional functionality
fullCmdArgs = sys.argv
hflag = False
vflag = False
dflag = False
sflag = False
saflag = False
lflag = True
fpath = fullCmdArgs[1]      #; print(fpath)
argList = fullCmdArgs[2:]   #; print(argList)

# Help
hflag = False
if len(fullCmdArgs) > 1:
    if fullCmdArgs[1] in ("-h", "--help"):
        hflag = True  

# # TO TEST - Comment previous assignments
# fpath = "file:///home...h5" # 
# argList = [] # ['-n', '--sa'] # 

unixOptions = "hnd:s:v"
gnuOptions = ["help", "nolist", "display=", "shape=", "sa", "shapeall", "verbose"]

try:
    arguments, values = getopt.getopt(argList, unixOptions, gnuOptions)
except getopt.error as err:
    # Output error, and return with an error code
    print(str(err))
    sys.exit(1)
    
for currentArgument, currentValue in arguments:
    if currentArgument in ("-v", "--verbose"):
        vflag = True
    elif currentArgument in ("-n", "--nolist"):
        lflag = False
    elif currentArgument in ("-h", "--help"):
        hflag = True
    elif currentArgument in ("-d", "--display"):
        dflag = True
        fdat = currentValue[1:]
    elif currentArgument in ("-s", "--shape"):
        sflag = True
        fdat = currentValue[1:]
    elif currentArgument in ("--sa", "--shapeall"):
        saflag = True
        fdat = currentValue[1:]

if hflag:
    print("Lists hdf5 file keys.")
    print("Help: listh5 -h")
    print("Usage: listh5 [filename] -h -n -d=[datsetname] -s=[datsetname] -v ")
    print("\t -h,--help\t\tDisplay help")
    print("\t -n,--nolist\t\tDisable listing of datasets")
    print("\t -d=?,--display=?\tPrint contents of passed 'datasetname'")
    print("\t -s=?,--shape=?\t\tPrint shape of passed 'datasetname'")
    print("\t --sa,--shapeall\t\tPrint shape of all 'datasetname'")
    print("\t -v,--verbosity\t\tEnable verbose display")
    sys.exit()
    
if vflag: 
    print("Contents of "+fpath+" :")

# Basic listing 
if fpath.startswith('file://'):
    fpath = fpath[len('file://'):]
if not os.path.exists(fpath):
    sys.exit("Error: Unable to open file. No such file or directory.")
extn = os.path.splitext(fpath)[1]
#
# f = h5py.File(fpath, 'r')
# print("Keys: %s\n" % f.keys())
# a_group_key = list(f.keys())[0]
# dset = f['dsetname'][:]
# f.close()
#
if lflag: 
    if extn == '.h5':
        read_hdf5(fpath, saflag)
    elif extn == '.mat':
        read_mat(fpath, saflag)

if dflag or sflag:
    # fdat = input("Enter a name dataset: ")
    with h5py.File(fpath, 'r') as hf:
        datset = hf[fdat][()]#[:]
    if dflag:    
        if vflag == True: print("Contents of "+fdat+" :")
        print(datset)
    elif sflag:    
        if vflag == True: print("Shape of "+fdat+" :")
        print(datset.shape)
if saflag:
    if vflag == True: print("Shapes:")
    if extn == '.h5':
        read_hdf5(fpath, saflag)
    elif extn == '.mat':
        read_mat(fpath, saflag)
