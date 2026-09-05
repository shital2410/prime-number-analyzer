# Prime Number Analyzer

This is a professional Python program designed to analyze prime numbers. It provides efficient logic to check whether a specific number is prime and generates a comprehensive list of all prime numbers within a specified range.

## 🚀 Features

- **Optimized Prime Checker:** Uses an efficient algorithm running up to $\sqrt{n}$ to minimize processing steps.
- **Range Generator:** Extracts and lists all prime numbers between a given starting and ending point.
- **Edge Case Management:** Successfully handles edge cases such as `0`, `1`, negative integers, and the number `2`.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries Used:** `math` (Built-in)

## 💻 How to Run the Project

### Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://python.org).

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```

2. **Navigate to the project folder:**
   ```bash
   cd Prime-Number-Analyzer
   ```

3. **Run the script:**
   ```bash
   python prime_analyzer.py
   ```

## 📈 Algorithm Details & Complexity

### 1. Is Prime Check (`is_prime`)
- **Logic:** Excludes numbers less than 2 and even numbers right away. Then, checks odd divisors only up to the square root of the number ($\sqrt{n}$).
- **Time Complexity:** $O(\sqrt{n})$ in the worst case.
- **Space Complexity:** $O(1)$ as it uses constant memory.

### 2. Range Generation (`generate_primes_in_range`)
- **Logic:** Iterates through the given range and calls the `is_prime` function for each element.
- **Time Complexity:** $O(R \cdot \sqrt{N})$, where $R$ is the range length and $N$ is the maximum number in that range.
-
