from itertools import combinations
import math

def solution(clothes):
    c_dict = {}
    for cloth in clothes:
        if cloth[1] not in c_dict.keys():
            c_dict[cloth[1]] = 1
        else:
            c_dict[cloth[1]] += 1
            
#    print(c_dict)
            
    ans = 0
    for i in range(2, len(c_dict)):
        comb = list(combinations(list(c_dict.keys()), i))
        print('comb', comb)
        for j in range(len(comb)):
            plus = 1
            for k in range(i):
                print(comb[j][k])
                print(c_dict[comb[j][k]])
                plus *= c_dict[comb[j][k]]
                print('plus', plus)
                
            ans += plus
            # print('ans', ans)
    ans += sum(list(c_dict.values()))

    if len(c_dict) > 1:
        ans += math.prod(list(c_dict.values()))

    return ans


print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
