items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(budget):
    ratio_list = [(name, data["calories"] / data["cost"], data["cost"], data["calories"]) 
                  for name, data in items.items()]
    
    ratio_list.sort(key=lambda x: x[1], reverse=True)
    
    selected = []
    total_cost = 0
    total_calories = 0

    for name, ratio, cost, calories in ratio_list:
        if total_cost + cost <= budget:
            selected.append(name)
            total_cost += cost
            total_calories += calories

    return selected, total_cost, total_calories


def dynamic_programming(budget):
    item_list = list(items.items())
    n = len(item_list)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    keep = [[False] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, data = item_list[i - 1]
        cost = data["cost"]
        calories = data["calories"]

        for j in range(budget + 1):
            dp[i][j] = dp[i - 1][j]

            if cost <= j:
                if dp[i - 1][j - cost] + calories > dp[i][j]:
                    dp[i][j] = dp[i - 1][j - cost] + calories
                    keep[i][j] = True

    selected = []
    w = budget
    for i in range(n, 0, -1):
        if keep[i][w]:
            selected.append(item_list[i - 1][0])
            w -= item_list[i - 1][1]["cost"]

    total_calories = dp[n][budget]
    total_cost = budget - w

    return selected, total_cost, total_calories


if __name__ == "__main__":
    budget = 120

    greedy_items, greedy_cost, greedy_calories = greedy_algorithm(budget)
    print(f"Жадібний алгоритм (бюджет {budget}):")
    print(f"  Вибрано: {', '.join(greedy_items)}")
    print(f"  Вартість: {greedy_cost}, Калорійність: {greedy_calories}\n")

    dp_items, dp_cost, dp_calories = dynamic_programming(budget)
    print(f"Динамічне програмування (бюджет {budget}):")
    print(f"  Вибрано: {', '.join(dp_items)}")
    print(f"  Вартість: {dp_cost}, Калорійність: {dp_calories}")
