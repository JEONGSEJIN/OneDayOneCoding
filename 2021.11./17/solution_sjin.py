from itertools import combinations

n, m = map(int, input().split(' '))
card = list(map(int, input().split(' ')))

def BlackJack(n, m, card):
    all_case = list(combinations(card, 3))

    max_sum = 0
    sum = []
    for i in all_case:
        sum.append(i[0] + i[1] + i[2])
    for j in sum:
        if m >= j and j >= max_sum:
            max_sum = j
    return max_sum

print(BlackJack(n, m, card))
