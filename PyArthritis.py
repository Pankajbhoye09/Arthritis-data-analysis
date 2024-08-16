import numpy as np
import matplotlib.pyplot as plt
import glob

def load_data(filename):
    """Load inflammation data from a CSV file."""
    return np.loadtxt(fname=filename, delimiter=',')

def plot_individual_patient_data(data):
    """Plot individual patient's inflammation data."""
    fig = plt.figure(figsize=(3.0, 10.0))
    ax = fig.add_subplot(111)
    ax.set_ylabel('Inflammation')
    ax.set_xlabel('Day')
    ax.plot(data)
    plt.show()

def plot_aggregate_statistics(data):
    """Plot aggregate statistics (average, max, min) across all patients."""
    fig, axes = plt.subplots(3, 1, figsize=(8.0, 10.0))
    for i, statistic in enumerate([np.mean(data, axis=0), np.amax(data, axis=0), np.amin(data, axis=0)]):
        ax = axes[i]
        ax.plot(statistic)
        ax.set_ylabel(['Average', 'Max', 'Min'][i])
    plt.tight_layout()
    plt.show()

def plot_difference_between_datasets(data1, data2):
    """Plot the difference in average inflammation between two datasets."""
    fig = plt.figure(figsize=(10.0, 3.0))
    ax = fig.add_subplot(111)
    ax.plot(np.mean(data1, axis=0) - np.mean(data2, axis=0))
    ax.set_ylabel('Average Difference')
    plt.tight_layout()
    plt.show()

def combine_and_plot_composite_data(filenames):
    """Combine data from multiple files and plot aggregate statistics."""
    composite_data = np.zeros((60, 40))
    for filename in filenames:
        composite_data += load_data(filename)
    composite_data /= len(filenames)

    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.0))
    for i, statistic in enumerate([np.mean(composite_data, axis=0), np.amax(composite_data, axis=0), np.amin(composite_data, axis=0)]):
        ax = axes[i]
        ax.plot(statistic)
        ax.set_ylabel(['Average', 'Max', 'Min'][i])
    plt.tight_layout()
    plt.show()

def sort_files(filenames):
    """Sort files into categories based on their names."""
    large_files = []
    small_files = []
    other_files = []
    for filename in filenames:
        if filename.startswith('inflammation'):
            large_files.append(filename)
        elif filename.startswith('small'):
            small_files.append(filename)
        else:
            other_files.append(filename)
    print("Large files:", large_files)
    print("Small files:", small_files)
    print("Other files:", other_files)

# Load and plot individual patient data
patient_data = load_data('inflammation-01.csv')
plot_individual_patient_data(patient_data)

# Plot aggregate statistics
plot_aggregate_statistics(patient_data)

# Compare data from two different datasets
data1 = load_data('inflammation-01.csv')
data2 = load_data('inflammation-02.csv')
plot_difference_between_datasets(data1, data2)

# Combine and plot composite data from multiple files
filenames = glob.glob('inflammation*.csv')
combine_and_plot_composite_data(filenames)

# Sort files into categories
sort_files(filenames)
