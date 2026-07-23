import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualizations(results_file, output_dir):
    df = pd.read_csv(results_file)
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Success Rate by Attack Type
    plt.figure(figsize=(10, 6))
    # Filter for standard attacks
    std_attacks = df[df['Attack'].isin(['Dictionary', 'Brute Force'])]
    success_counts = std_attacks.groupby(['Attack', 'Success']).size().unstack(fill_value=0)
    success_counts.plot(kind='bar', stacked=True, color=['#ff9999','#66b3ff'])
    plt.title('Success vs Failure by Attack Type')
    plt.ylabel('Number of Accounts')
    plt.xticks(rotation=0)
    plt.savefig(os.path.join(output_dir, 'success_rate.png'))
    plt.close()
    
    # 2. Attempts by Difficulty (for Dictionary Attack)
    plt.figure(figsize=(10, 6))
    dict_df = df[df['Attack'] == 'Dictionary']
    sns.boxplot(x='Difficulty', y='Attempts', data=dict_df)
    plt.title('Attempts required by Password Difficulty (Dictionary Attack)')
    plt.savefig(os.path.join(output_dir, 'attempts_by_difficulty.png'))
    plt.close()
    
    # 3. Runtime comparison
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Attack', y='Time', data=std_attacks)
    plt.title('Average Execution Time per Attack')
    plt.ylabel('Time (seconds)')
    plt.savefig(os.path.join(output_dir, 'runtime_comparison.png'))
    plt.close()

    print(f"[+] Visualizations saved to {output_dir}")

if __name__ == "__main__":
    create_visualizations("../data/results.csv", "../graphs")
