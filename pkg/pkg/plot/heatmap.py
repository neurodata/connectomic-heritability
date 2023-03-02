import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import ListedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable


def heatmap(
    data,
    ax=None,
    axes_labels=None,
    heatmap_kwargs=None,
    annot_kwargs=None,
    color_ax_kwargs=None,
):
    heatmap_kwgs = dict(
        square=True,
        xticklabels=False,
        yticklabels=False,
        cbar=False,
        cmap="RdBu",
        center=0,
        # linewidths=0.01,
    )
    if heatmap_kwargs is not None:
        heatmap_kwgs.update(heatmap_kwargs)

    if ax is None:
        fig, ax = plt.subplots(figsize=(5, 5))
    sns.heatmap(data, ax=ax, **heatmap_kwgs)

    n = data.shape[0]
    for i in range(n):
        ax.axhline(i, c="w", lw=0.1)
        ax.axvline(i, c="w", lw=0.1)

    # plotting axes colors
    divider = make_axes_locatable(ax)

    def color_plotter(axes):
        "axes = top or left"

        classes = np.unique(axes_labels)
        n_classes = len(classes)

        # draw colors
        annot_kwgs = dict(fontsize=7, c="w", fontfamily="Dejavu Sans")
        if annot_kwargs is not None:
            annot_kwgs.update(annot_kwargs)

        color_ax_kwgs = dict(size="6%", pad="0.5%")
        if color_ax_kwargs is not None:
            color_ax_kwgs.update(color_ax_kwargs)

        if axes == "top":
            color_ax_kwgs.update(dict(position="top", sharex=ax))
            data = np.arange(0, n_classes).reshape(1, -1)
            annot = classes.reshape(1, -1)
        elif axes == "left":
            color_ax_kwgs.update(dict(position="left", sharey=ax))
            data = np.arange(0, n_classes).reshape(-1, 1)
            annot = classes.reshape(-1, 1)
            annot_kwgs.update(dict(rotation=90))

        # hexes = ["#df536b", "#60d050"]
        # rgbs = [mpl.colors.hex2color(i) for i in hexes]
        # cmap = ListedColormap(rgbs)
        cmap = ListedColormap(mpl.colormaps["tab10"](range(n_classes)))

        color_ax = divider.append_axes(**color_ax_kwgs)
        _remove_shared_ax(color_ax)

        sns.heatmap(
            data,
            annot=annot,
            annot_kws=annot_kwgs,
            fmt="",
            cmap=cmap,
            cbar=False,
            yticklabels=False,
            xticklabels=False,
            ax=color_ax,
            square=False,
            linewidths=0.05,
        )

    if axes_labels is not None:
        color_plotter("top")
        color_plotter("left")


def _remove_shared_ax(ax):
    """
    Remove ax from its sharex and sharey
    """
    # Remove ax from the Grouper object
    shax = ax.get_shared_x_axes()
    shay = ax.get_shared_y_axes()
    shax.remove(ax)
    shay.remove(ax)

    # Set a new ticker with the respective new locator and formatter
    for axis in [ax.xaxis, ax.yaxis]:
        ticker = mpl.axis.Ticker()
        axis.major = ticker
        axis.minor = ticker
        # No ticks and no labels
        loc = mpl.ticker.NullLocator()
        fmt = mpl.ticker.NullFormatter()
        axis.set_major_locator(loc)
        axis.set_major_formatter(fmt)
        axis.set_minor_locator(loc)
        axis.set_minor_formatter(fmt)
