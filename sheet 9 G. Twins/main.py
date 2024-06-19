def min_number_of_coins(n, coins:list):
    coins.sort(reverse=True)
    
    total_sum = sum(coins)
    
    selected_sum = 0
    num_selected_coins = 0
    
    for coin in coins:
        selected_sum += coin
        num_selected_coins += 1
        if selected_sum > total_sum / 2:
            break
    
    return num_selected_coins

n = int(input())
coins = list(map(int, input().split()))

print(min_number_of_coins(n, coins))
