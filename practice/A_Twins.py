n = int(input())

coins = list(map(int, input().split()))

coins.sort(reverse = True)

total_sum = sum(coins)

my_sum = 0

coin_count = 0

for coin in coins:
    my_sum += coin
    coin_count += 1

    twin_sum = total_sum - my_sum
    if my_sum > twin_sum:
        print(coin_count)
        break