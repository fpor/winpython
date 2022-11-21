# -*- coding: utf-8 -*-
#
# Copyright © 2012 Pierre Raybaut
# Licensed under the terms of the MIT License
# (see winpython/__init__.py for details)

"""
WinPython utilities configuration

Created on Wed Aug 29 12:23:19 2012
"""

import sys
# import os.path as osp
from pathlib import Path

def get_module_path(modname):
    """Return module *modname* base path"""
    #return osp.abspath(
    #   osp.dirname(sys.modules[modname].__file__)
    #)    
    return str(Path(sys.modules[modname].__file__).parent.resolve())


def get_module_data_path(
    modname, relpath=None, attr_name='DATAPATH'
):
    """Return module *modname* data path
    Note: relpath is ignored if module has an attribute named *attr_name*

    Handles py2exe/cx_Freeze distributions"""
    datapath = getattr(sys.modules[modname], attr_name, '')
    if datapath:
        return datapath
    else:
        datapath = get_module_path(modname)
        # parentdir = osp.join(datapath, osp.pardir)
        parentdir = str(Path(datapath).parent)
        #if osp.isfile(parentdir):
        if Path(parentdir).is_file():
            # Parent directory is not a directory but the 'library.zip' file:
            # this is either a py2exe or a cx_Freeze distribution
            #datapath = osp.abspath(
                # osp.join(
                #     osp.join(parentdir, osp.pardir), modname
                # )
            #)    
            datapath = str((Path(parentdir).parent / modname).resolve())
        if relpath is not None:
            #datapath = osp.abspath(
                # osp.join(datapath, relpath)
            #)
            datapath = str((Path(datapath) / relpath).resolve())
        return datapath


DATA_PATH = get_module_data_path(
    'winpython', relpath='data'
)
IMAGE_PATH = get_module_data_path(
    'winpython', relpath='images'
)
