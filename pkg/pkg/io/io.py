import os
from pathlib import Path
import pickle

import matplotlib.pyplot as plt
import numpy as np


def _handle_dirs(pathname, foldername, subfoldername):
    path = Path(pathname)
    if foldername is not None:
        path = path / foldername
        if not os.path.isdir(path):
            os.mkdir(path)
        if subfoldername is not None:
            path = path / subfoldername
            if not os.path.isdir(path):
                os.mkdir(path)
    return path


def savefig(
    name,
    format="png",
    dpi=300,
    foldername=None,
    subfoldername="figs",
    pathname="./twins/notebooks/outs",
    bbox_inches="tight",
    pad_inches=0.5,
    save_on=True,
    transparent=False,
    print_out=True,
    **kws,
):
    if save_on:
        path = _handle_dirs(pathname, foldername, subfoldername)
        savename = path / str(name + "." + format)
        plt.savefig(
            savename,
            format=format,
            facecolor="white",
            transparent=transparent,
            bbox_inches=bbox_inches,
            pad_inches=pad_inches,
            dpi=dpi,
            **kws,
        )
        if print_out:
            print(f"Saved figure to {savename}")


def saveobj(
    obj,
    name,
    foldername=None,
    subfoldername="objs",
    pathname="./twins/notebooks/outs",
    save_on=True,
):
    if save_on:
        path = _handle_dirs(pathname, foldername, subfoldername)
        savename = path / str(name + ".pickle")
        with open(savename, "wb") as f:
            pickle.dump(obj, f)
            print(f"Saved object to {savename}")


def savearr(
    arr,
    name,
    foldername=None,
    subfoldername="arrs",
    pathname="./twins/notebooks/outs",
    save_on=True,
    print_out=True,
):
    if save_on:
        path = _handle_dirs(pathname, foldername, subfoldername)
        savename = path / str(name + ".npy")
        np.save(savename, arr)

        if print_out:
            print(f"Saved array to {savename}")
