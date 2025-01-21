import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

def simulate_plays(k, p, simulations=10000):
    """Simulate the number of plays needed to win k tubs of ice cream."""
    results = []
    for _ in range(simulations):
        successes = 0
        plays = 0
        while successes < k:
            plays += 1
            if np.random.rand() < p:
                successes += 1
        results.append(plays)
    return results

def theoretical_stats(k, p):
    """Calculate theoretical expected value and variance."""
    expected_value = k / p
    variance = k * (1 - p) / (p ** 2)
    return expected_value, variance

if __name__ == "__main__":
    # Parameters
    k = 5  # Number of tubs to win
    p = 0.3  # Probability of winning in a single play
    simulations = 10000

    # Simulations and theoretical results
    simulated_plays = simulate_plays(k, p, simulations)
    expected_value, variance = theoretical_stats(k, p)

    # Print results
    print(f"Theoretical Expected Value: {expected_value:.2f}")
    print(f"Theoretical Variance: {variance:.2f}")
    print(f"Simulated Mean: {np.mean(simulated_plays):.2f}")
    print(f"Simulated Variance: {np.var(simulated_plays):.2f}")

    # Visualization
    plt.hist(simulated_plays, bins=30, density=True, alpha=0.7, label="Simulated")
    x = np.arange(k, max(simulated_plays) + 1)
    plt.plot(x, nbinom.pmf(x - k, k, p), 'r-', label="Theoretical")
    plt.title("Number of Plays Distribution")
    plt.xlabel("Number of Plays")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.show()
