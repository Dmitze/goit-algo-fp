import random
import matplotlib.pyplot as plt


def monte_carlo_dice_simulation(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sums_count[total] += 1
    
    probabilities = {s: count / num_rolls for s, count in sums_count.items()}
    
    return sums_count, probabilities


def analytical_probabilities():
    outcomes = {
        2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6,
        8: 5, 9: 4, 10: 3, 11: 2, 12: 1
    }
    
    total_outcomes = 36
    probabilities = {s: count / total_outcomes for s, count in outcomes.items()}
    
    return probabilities


def compare_results(monte_carlo_probs, analytical_probs):
    print("Порівняння результатів:\n")
    print(f"{'Сума':<6} {'Монте-Карло':<15} {'Аналітика':<15} {'Різниця':<10}")
    print("-" * 50)
    
    for s in range(2, 13):
        mc = monte_carlo_probs[s]
        ana = analytical_probs[s]
        diff = abs(mc - ana)
        print(f"{s:<6} {mc:<15.4f} {ana:<15.4f} {diff:<10.4f}")


def plot_results(monte_carlo_probs, analytical_probs):
    sums = list(range(2, 13))
    mc_values = [monte_carlo_probs[s] for s in sums]
    ana_values = [analytical_probs[s] for s in sums]

    plt.figure(figsize=(10, 6))
    plt.bar([s - 0.2 for s in sums], mc_values, width=0.4, label='Монте-Карло', alpha=0.7)
    plt.bar([s + 0.2 for s in sums], ana_values, width=0.4, label='Аналітика', alpha=0.7)
    
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Порівняння ймовірностей: Монте-Карло vs Аналітика')
    plt.xticks(sums)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    num_rolls = 1000000
    
    print(f"Симуляція {num_rolls} кидків двох кубиків...\n")
    
    sums_count, monte_carlo_probs = monte_carlo_dice_simulation(num_rolls)
    analytical_probs = analytical_probabilities()
    
    compare_results(monte_carlo_probs, analytical_probs)
    
    print("\n\nВисновки:")
    print("Результати Монте-Карло близькі до аналітичних розрахунків.")
    print("Чим більша кількість симуляцій, тим точніше результати.")
    
    plot_results(monte_carlo_probs, analytical_probs)
