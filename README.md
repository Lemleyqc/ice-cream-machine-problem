# Ben and Jerry's Ice Cream Machine Problem

This repository solves the statistical problem of determining the expected number of plays needed to obtain \( k \) tubs of ice cream from a machine, modeled using the **negative binomial distribution**.

## Problem Statement
You observe \( k \) people playing the ice cream machine at UTown. You count the total number of plays \( N \) required to win \( k \) tubs of ice cream. What is the expected distribution of \( N \), and how can we simulate it?

## Approach
This problem is modeled using the **negative binomial distribution**, which represents the number of trials \( N \) needed to achieve \( k \) successes in independent Bernoulli trials with success probability \( p \).

### Theoretical Results
- **Expected value** of \( N \): \( \mathbb{E}[N] = \frac{k}{p} \)
- **Variance** of \( N \): \( \text{Var}(N) = \frac{k(1-p)}{p^2} \)

## Repository Contents
1. **`solution.py`**: Python code to simulate the problem and validate theoretical results.
2. **`explanation.md`**: Detailed mathematical derivation and connection to the negative binomial distribution.

