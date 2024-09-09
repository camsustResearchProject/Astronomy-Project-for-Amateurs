import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set the font to Computer Modern using Matplotlib's built-in support
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'

# data

data = {
    '$D_S$' : [658.11, 12.82, 16.41, 69.06],
    '$D_C$' : [632.24, 12.80, 16.38, 68.75],
    '$D_A$' : [546.00, 12.76, 16.32, 67.63],
    '$D_L$' : [732.10, 12.84, 16.45, 69.90]
}

df = pd.DataFrame(data)
corr_matrix = df.corr()
print(corr_matrix)

# Plot the correlation matrix as a heatmap using Matplotlib
plt.figure(figsize=(8, 6))
plt.imshow(corr_matrix, cmap='Greens', interpolation='nearest', vmax=1, vmin=0.99899)

# Add colorbar
plt.colorbar()

# Add labels
plt.xticks(ticks=np.arange(len(corr_matrix.columns)), labels=corr_matrix.columns, fontsize=14)
plt.yticks(ticks=np.arange(len(corr_matrix.index)), labels=corr_matrix.index, fontsize=14)

# Add title
plt.title('Correlation Matrix Heatmap of Galaxies Distances')

# Annotate the heatmap with the correlation values
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.index)):
        plt.text(j, i, f'{corr_matrix.iloc[i, j]:.6f}', ha='center', va='center', color='#fff', fontsize=10)

# Show the plot
plt.show()