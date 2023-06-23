from collections import Counter
winners = []
for user_members in range(1, 65):
    k = 78
    members_list = list(range(1, user_members + 1))
    if k >= user_members:
        while len(members_list) != 1:
            result = abs(len(members_list) - k)
            if result > len(members_list):
                while result >= len(members_list):
                    result -= len(members_list)
            if result <= len(members_list):
                members_list.remove(members_list[result - 1])
    else:
        while len(members_list) != 1 and k <= len(members_list):
            members_list.remove(members_list[k - 1])
        else:
            while len(members_list) != 1:
                result = abs(len(members_list) - k)
                if result > len(members_list):
                    while result >= len(members_list):
                        result -= len(members_list)
                if result <= len(members_list):
                    members_list.remove(members_list[result - 1])
    winners.append(members_list[0])
print(Counter(winners))
