from matplotlib import pyplot as plt
import pandas as pd

def plot_alpha_coefficients(alpha_e, alpha_k):
    labels = ['αe', 'αk']
    values = [alpha_e, alpha_k]

    plt.bar(labels, values, color=['blue', 'orange'])
    plt.ylabel('Wartości współczynników')
    plt.title('Współczynniki αe i αk')
    plt.ylim(0, max(values) * 1.2)
    plt.grid(axis='y')
    plt.show()

def plot_reliability_indicators(indicators):
    df = pd.DataFrame(indicators)
    df.plot(kind='bar', figsize=(10, 6))
    plt.title('Wskaźniki niezawodności')
    plt.ylabel('Wartości')
    plt.xlabel('Wskaźniki')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def generate_results_table(data):
    df = pd.DataFrame(data)
    print(df.to_string(index=False))

def save_plot_to_file(filename):
    plt.savefig(filename)
    print(f'Wykres zapisany jako {filename}')