def min_coin_count(value, coin_list):
    coin_list = sorted(coin_list)
    coin_list.reverse()
    count = 0
    for c in coin_list:
        if(value//c > 0):
            count += value//c
            value = value%c
    return count


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))