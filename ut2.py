import numpy as np
import matplotlib.pyplot as plt

def plot_radar_chart(scores):
    # Define categories as labels from 7.1 to 7.14
    categories = [f"7.{i+1}" for i in range(len(scores))]
    
    # Complete the circle by repeating the first value
    values = scores + scores[:1]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    # Create radar chart
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='teal', alpha=0.25)
    ax.plot(angles, values, color='teal', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    return fig
