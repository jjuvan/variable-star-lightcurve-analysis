#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:47:05 2026

@author: jacobjuvan
"""

import numpy as np
import argparse
import os
import pandas as pd

def convert_asassn(file):
    object_file = os.path.basename(file)
    object_name = os.path.splitext(object_file)[0]
    new_file = object_name + '.dat'
    
    extension = os.path.splitext(file)[1].lower()

    if extension == ".xlsx":
        df = pd.read_excel(file)
        data = df[["hjd", "mag", "mag err"]].copy()
    elif extension == ".csv":
        df = pd.read_csv(file)
        data = df[["hjd", "mag", "mag_err"]].copy()
    else:
        raise ValueError(f"Unsupported file format: {extension}")
    
    data = data.dropna()
    
    np.savetxt(
        new_file,
        data.to_numpy(),
        fmt="%.8f"
    )
        
parser = argparse.ArgumentParser()
parser.add_argument("indata", nargs="+", help = "Object's ASAS data file")
args = parser.parse_args()
indata = args.indata

for file in indata:
    convert_asassn(file)