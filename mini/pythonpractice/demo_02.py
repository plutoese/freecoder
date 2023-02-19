# 导入库
from itertools import combinations

# =================================
#           自定义组合函数
# =================================
def com(x, n=2):
    result = []
    if n < 2:
        return x
    else:
        for i in range(n-1, len(x)):
            record = ["*".join([item, x[i]]) for item in com(x[0:i], n-1)]
            result.extend(record)
        return result

# =================================
#             主程序
# =================================
input_NV = input("Please input N and V: ").split(",")
N, V = int(input_NV[0]), int(input_NV[1])

gifts = dict()
character_num = 97
while True:
    gift = input("Please input price and favorite number (e for exit): ")
    if gift == "e":
        break
    
    gifts[chr(character_num)] = [int(item) for item in gift.split(",")]
    character_num = character_num + 1

gift_choice = None
favorite_num = 0
for n in range(1, N+1):
    for item in combinations(gifts.keys(), n):
        gifts_price = sum([gifts[i][0] for i in item])
        gifts_favorite_num = sum([gifts[i][1] for i in item])
        if gifts_price > V:
            continue
        else:
            if gifts_favorite_num > favorite_num:
                favorite_num = gifts_favorite_num
                gift_choice  = item

print(f"Gifts {[(item, gifts[item]) for item in gift_choice]} are chosen. Favorite number is {favorite_num}!")

# 或者使用自定义函数
for n in range(1, N+1):
    for item in com(list(gifts.keys()), n):
        item = item.split("*")
        gifts_price = sum([gifts[i][0] for i in item])
        gifts_favorite_num = sum([gifts[i][1] for i in item])
        if gifts_price > V:
            continue
        else:
            if gifts_favorite_num > favorite_num:
                favorite_num = gifts_favorite_num
                gift_choice  = item

print(f"Gifts {[(item, gifts[item]) for item in gift_choice]} are chosen. Favorite number is {favorite_num}!")