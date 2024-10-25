import pandas as pd
import matplotlib.pyplot as plt

# Data (based on the values from your image)
data = {
    'X': [1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2],
    'Y': [0.55, 0.88, 0.94, 1.1, 1.14, 1.14, 0.75, 0.54, 0.55, 0.54, 0.4]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot the graph
plt.figure(figsize=(8, 4))
plt.plot(df['X'], df['Y'], marker='o', linestyle='-', color='b')

# Customize the plot
plt.title('Visualization of the Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

# Show the plot
plt.show()
