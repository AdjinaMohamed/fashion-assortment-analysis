import matplotlib.pyplot as plt


def plot_top_white_space_gaps(white_space_gaps, brand_name, n=10, save_path=None):
    df = white_space_gaps.head(n).copy()
    df["category_price"] = df["category_main"] + " | " + df["price_band"]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(df["category_price"], df["sku_count"])
    ax.invert_yaxis()
    ax.set_title(f"Top {n} white-space segments for {brand_name}")
    ax.set_xlabel("Total SKUs in market")
    ax.set_ylabel("Category | Price band")
    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path, bbox_inches="tight", dpi=120)

    return ax
