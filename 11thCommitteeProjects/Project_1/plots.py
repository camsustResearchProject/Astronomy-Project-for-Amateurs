import matplotlib.pyplot as plt
import numpy as np

# Set the font to Computer Modern using Matplotlib's built-in support
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'

# Data
distances = {
    '3C 273': [658.11, 632.24, 546.00, 732.10],
    'NGC 4051': [12.82, 12.80, 12.76, 12.84],
    'NGC 3982': [16.41, 16.38, 16.32, 16.45],
    'NGC 7469': [69.06, 68.75, 67.63, 69.90]
}

actual = {
    '3C 273': 705.23,
    'NGC 4051': 13.64,
    'NGC 3982': 18.91,
    'NGC 7469': 66.47
}

# Plotting
plt.figure(figsize=(10, 6))

for i, (label, distance) in enumerate(distances.items()):
    plt.subplot(2, 2, i + 1)
    bars = plt.bar(np.arange(len(distance)) * 0.6, distance, width=0.4, color=['#004035', '#018c65', '#025a40', '#008c3e'])
    plt.ylabel(r'Distance (Mpc)')
    plt.title(label)
    plt.xticks(np.arange(len(distance)) * 0.6, [r'$D_{S}$', r'$D_{C}$', r'$D_{A}$', r'$D_{L}$'])  # Add x-axis labels
    
    # Add labels on the bins and rotate them 90 degrees
    for j, bar in enumerate(bars):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f'{distance[j]:.2f}', ha='center', va='center', fontsize=10, color='white', rotation=90)
    
    # Add horizontal line at the actual value
    plt.axhline(y=actual[label], color='black', linestyle='--', linewidth=1)
    
    # Remove top and right spines
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()