import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import ListedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable
import pandas as pd
import scipy.stats as stats


def heatmap(
    data,
    ax=None,
    axes_labels=None,
    heatmap_kwargs=None,
    annot_kwargs=None,
    color_ax_kwargs=None,
    ax_lw=0.01,
):
    heatmap_kwgs = dict(
        square=True,
        xticklabels=False,
        yticklabels=False,
        cbar=False,
        cmap="RdGy",
        center=0,
        # linewidths=0.01,
    )
    if heatmap_kwargs is not None:
        heatmap_kwgs.update(heatmap_kwargs)

    if ax is None:
        fig, ax = plt.subplots(figsize=(5, 5))
    sns.heatmap(data, ax=ax, **heatmap_kwgs)

    n = data.shape[0]
    if ax_lw is None or ax_lw == 0:
        pass
    else:
        for i in range(n):
            ax.axhline(i, c="w", lw=ax_lw)
            ax.axvline(i, c="w", lw=ax_lw)

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


def stripplot(plot_df, ax=None, col_names=None, row_names=None):
    if ax is None:
        fig, ax = plt.subplots(
            nrows=3,
            ncols=3,
            figsize=(7, 5),
            dpi=300,
            sharex="col",
            # constrained_layout=True,
        )
    sns.despine(bottom=True, left=True)

    if col_names is None:
        COL_NAMES = ["Exact", "Global Scale", "Vertex Scale"]
    else:
        COL_NAMES = col_names
    if row_names is None:
        ROW_NAMES = ["All Subjects", "Females", "Males"]
    else:
        ROW_NAMES = row_names

    for rdx, gender in enumerate(["all", "female", "male"]):
        for cdx, scale in enumerate(["exact", "glob", "vertex"]):
            tmp_df = plot_df[(plot_df.scale == scale) & (plot_df.gender == gender)]

            sns.stripplot(
                x="distance",
                y="scale",
                hue="relationship",
                data=tmp_df,
                dodge=True,
                alpha=0.25,
                zorder=1,
                ax=ax[rdx, cdx],
                jitter=0.25,
            )

            sns.pointplot(
                x="distance",
                y="scale",
                hue="relationship",
                data=tmp_df,
                dodge=0.8 - 0.8 / 4,
                join=False,
                palette=["w"],
                markers="d",
                scale=1.1,
                estimator=np.median,
                errorbar=None,
                ax=ax[rdx, cdx],
            )
            sns.pointplot(
                x="distance",
                y="scale",
                hue="relationship",
                data=tmp_df,
                dodge=0.8 - 0.8 / 4,
                join=False,
                palette="dark",
                markers="d",
                scale=1,
                estimator=np.median,
                errorbar=None,
                ax=ax[rdx, cdx],
            )

            handles, labels = ax[rdx, cdx].get_legend_handles_labels()
            ax[rdx, cdx].get_legend().remove()

            ax[rdx, cdx].set_xticks([])
            ax[rdx, cdx].set_yticks([])
            ax[rdx, cdx].set_xlabel("")
            ax[rdx, cdx].set_ylabel("")

            if rdx == 0:
                ax[rdx, cdx].set_title(
                    COL_NAMES[cdx], fontdict=dict(fontsize=10), loc="left"
                )

            if cdx == 0:
                ax[rdx, cdx].set_ylabel(
                    ROW_NAMES[rdx],
                    fontdict=dict(fontsize=8),
                )

            # if rdx == 2:
            #     if cdx == 1:
            #         ax[rdx, cdx].set_xlabel("Distance", fontdict=dict(fontsize=8),)

    # fig.legend(
    #     handles[:4],
    #     ["Monozygotic", "Dizygotic", "Sibling", "Unrelated"],
    #     loc=8,
    #     title="Relationships",
    #     ncol=4,
    #     handletextpad=0,
    #     columnspacing=1,
    #     frameon=True,
    # )

    if ax is None:
        return fig, handles, labels
    else:
        return handles, labels


def stripplot_cov(plot_df, ax=None, col_names=None, row_names=None):
    if ax is None:
        fig, ax = plt.subplots(
            nrows=3,
            ncols=1,
            figsize=(2.0, 5),
            dpi=300,
            sharex="col",
            # constrained_layout=True,
        )
    sns.despine(bottom=True, left=True)

    if col_names is None:
        COL_NAMES = ["Exact", "Global Scale", "Vertex Scale"]
    else:
        COL_NAMES = col_names
    if row_names is None:
        ROW_NAMES = ["All Subjects", "Females", "Males"]
    else:
        ROW_NAMES = row_names

    for rdx, gender in enumerate(["all", "female", "male"]):
        for cdx, scale in enumerate(["exact"]):
            tmp_df = plot_df[(plot_df.scale == scale) & (plot_df.gender == gender)]

            sns.stripplot(
                x="distance",
                y="scale",
                hue="relationship",
                data=tmp_df,
                dodge=True,
                alpha=0.25,
                zorder=1,
                ax=ax[rdx],
                jitter=0.25,
            )

            sns.pointplot(
                x="distance",
                y="scale",
                hue="relationship",
                data=tmp_df,
                dodge=0.8 - 0.8 / 4,
                join=False,
                palette=["w"],
                markers="d",
                scale=1.1,
                estimator=np.median,
                errorbar=None,
                ax=ax[rdx],
            )
            sns.pointplot(
                x="distance",
                y="scale",
                hue="relationship",
                data=tmp_df,
                dodge=0.8 - 0.8 / 4,
                join=False,
                palette="dark",
                markers="d",
                scale=1,
                estimator=np.median,
                errorbar=None,
                ax=ax[rdx],
            )

            handles, labels = ax[cdx].get_legend_handles_labels()
            ax[rdx].get_legend().remove()

            ax[rdx].set_xticks([])
            ax[rdx].set_yticks([])
            ax[rdx].set_xlabel("")
            ax[rdx].set_ylabel("")

            # if cdx == 0:
            #     ax[rdx].set_ylabel(ROW_NAMES[rdx], fontdict=dict(fontsize=8))

    ax[0].set_title("iv) Neuroanatomy", fontdict=dict(fontsize=10), loc="left")
    # ax[-1].set_xlabel("Distance")

    if ax is None:
        return fig
