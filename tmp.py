def min_coin_count(value, coin_list):
    count = 0
    for c in range(len(coin_list)):
        coin = max(coin_list)
        if(value//coin > 0):
            count += value//coin
            value = value%coin
            coin_list.remove(coin)
        else:
            coin_list.remove(coin)
    return count
