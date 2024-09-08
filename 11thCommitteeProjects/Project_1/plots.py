import matplotlib.pyplot as plt
import numpy as np

# Set the font to Computer Modern using Matplotlib's built-in support
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'

# Data
distances = {
    '3C 273': [658.11, 632.24],
    'NGC 1068': [10.26, 10.25],
    'NGC 3982': [16.41, 16.38],
    'NGC 7469': [69.06, 68.75]
}

actual = {
    '3C 273': 705.23,
    'NGC 1068': 13.48,
    'NGC 3982': 18.91,
    'NGC 7469': 66.47
}

# Plotting
plt.figure(figsize=(5, 5))

for i, (label, distance) in enumerate(distances.items()):
    plt.subplot(2, 2, i + 1)
    bars = plt.bar([0, 0.45], distance, width=0.4, color=['#8cc5e3', '#1a80bb'])
    plt.ylabel(r'Distance (Mpc)')
    plt.title(label)
    plt.xticks([])  # Remove x-axis labels
    
    # Add labels on the bins and rotate them 90 degrees
    plt.text(0, distance[0] / 2, r'$D_{s}$', ha='center', va='center', fontsize=14, color='white', rotation=90)
    plt.text(0.45, distance[1] / 2, r'$D_{c}$', ha='center', va='center', fontsize=14, color='white', rotation=90)
    
    # Add horizontal line at the actual value
    plt.axhline(y=actual[label], color='black', linestyle='--', linewidth=1)
    
    # Remove top and right spines
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
