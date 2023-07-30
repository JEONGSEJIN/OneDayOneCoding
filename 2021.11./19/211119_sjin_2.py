n = 6
# lines = [[1, 1, 2, 3], [2, 1, 0, 0], [1, 0, 1, 1]]
# lines = [[-1, -1, 1, 1], [-2, -2, 2, 2], [0, 1, -1, 0]]
# lines = [[-1, -1, 1, 1], [-2, -2, 2, 2], [0, 1, -1, 0], [-3, -3, 2, 0], [-3, -3, 0, -2]]
lines = [[-1, -1, 1, 1], [-2, -2, 2, 2], [0, 1, -1, 0], [-3, -3, 2, 0], [-3, -3, 0, -2], [-3, -3, 3, 3]]

who_is_bigger = lambda y1, y2: y1 if y1>=y2 else y2
who_is_smaller = lambda y1, y2: y1 if y1<=y2 else y2
get_inclination = lambda a: (a[1] - a[3]) / (a[0] - a[2]) # 기울기 구하기
get_y_intercept = lambda a: a[1] - a[0] * get_inclination(a) # y절편 구하기
check_double_point = lambda a, x_meet: 1 if (a[0] - x_meet) * (a[2] - x_meet) <= 0 else 0 # 교점 구하기
    
# 그룹 탐색
def is_it_group(a, b):
    # 
    if a[0] == a[2] and b[0] == b[2]:
        if who_is_smaller(a[1], a[3]) > who_is_bigger(b[1], b[3]) or who_is_smaller(b[1], b[3]) > who_is_bigger(a[1], a[3]):
            return 0
        else:
            return 1
    # 
    elif a[0] == a[2]:
        y_of_meet = a[0] * get_inclination(b) + get_y_intercept(b)
        if y_of_meet >= a[1] and y_of_meet <= a[3]:
            return 1
        else:
            return 0
    # 
    elif b[0] == b[2]:
        y_of_meet = b[0] * get_inclination(a) + get_y_intercept(a)
        if y_of_meet >= b[1] and y_of_meet <= b[3]:
            return 1
        else:
            return 0
    # 
    else:
        if get_inclination(a) == get_inclination(b):  # 두 선분의 기울기가 같을 때 --> 같은 x점에서의 y값 비교!
            y_of_a_line = b[0] * get_inclination(a) + get_y_intercept(a)
            if y_of_a_line == b[1]:
                if who_is_smaller(b[0], b[2]) > who_is_bigger(a[0], a[2]) or who_is_smaller(a[0], a[2]) > who_is_bigger(b[0], b[2]):
                    return 0
                else:
                    return 1
            else:
                return 0

        else:
            x_of_meet = (get_y_intercept(b) - get_y_intercept(a)) / (get_inclination(a) - get_inclination(b))
            y_of_meet = x_of_meet * get_inclination(a) + get_y_intercept(a)
            if check_double_point(a, x_of_meet) and check_double_point(b, x_of_meet):
                return 1
            else:
                return 0

semi_groups = []
not_alone_index = []
for i in range(n - 1):
    for k in range(n - 1 - i):
        print('i =', i)
        print('k + i + 1 =', k + i + 1) 
        if is_it_group(lines[i], lines[k + i + 1]):
            temp = [i, k + i + 1]
            chance = 0
            for i in range(len(semi_groups)):
                if (temp[0] in semi_groups[i]) or (temp[1] in semi_groups[i]):
                    semi_groups[i].append(temp[0])
                    semi_groups[i].append(temp[1])
                    semi_groups[i] = list(set(semi_groups[i]))
                    not_alone_index.append(i)
                    not_alone_index.append(k + i + 1)
                    not_alone_index = list(set(not_alone_index))
                    chance = 1
                    break
            if chance == 0:
                semi_groups.append(temp)
                not_alone_index.append(i)
                not_alone_index.append(k + i + 1)
                not_alone_index = list(set(not_alone_index))
            else:
                pass
        else:
            pass

high = 0
for group in semi_groups:
    temp = len(group)
    if temp >= high:
        high = temp

alone_index = list(range(n))
for index in not_alone_index:
    alone_index.remove(index)

print("semi_groups: ", semi_groups)
print("not_alone_index: ", not_alone_index)
print("alone_index: ", alone_index)

print(len(semi_groups) + len(alone_index))
print(high)
