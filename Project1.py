#Range use: Range 1
import random
import time
import matplotlib.pyplot as plt

def Unique_element(A):
    n = len(A)
    comparisons = 0
    for i in range (0, n -1):
        for j in range (i + 1 ,n ):
            comparisons +=1
            if A[i] == A[j]:
                return comparisons
    return  comparisons
        
def average_comparisons_for_m(m):
    sizes = [int(factor * m) for factor in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3]]
    average_comparisons = {}

    for size in sizes:
        total_comparisons = 0
        
        for _ in range(100):  # Run 100 times
            random.seed(time.time())  # Seed based on current system time
            array = [random.randint(1, m) for _ in range(size)]
            total_comparisons += Unique_element(array)

        average_comparisons[size] = total_comparisons / 100

    return average_comparisons

def plot_graph(m_values, average_results_dict):
    for m in m_values:
        sizes = [int(factor * m) for factor in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3]]
        worst_case = [(n*(n-1))//2 for n in sizes]
        average_case = [average_results_dict[m][size] for size in sizes]
        
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, worst_case, label="Worst Case", marker='o')
        plt.plot(sizes, average_case, label="Average Case", marker='x')
        plt.title(f"Comparisons for m = {m}")
        plt.xlabel("Array Size (n)")
        plt.ylabel("Number of Comparisons")
        plt.legend()
        plt.grid(True)
        plt.show()

m_values = [200, 2000, 400, 4000, 600, 6000, 800, 8000]
average_results_dict = {}

for m in m_values:
    average_results_dict[m] = average_comparisons_for_m(m)

plot_graph(m_values, average_results_dict)