import sys
input = sys.stdin.readline


def solution(players, callings):
    rank = {}
    name = {}
    for i, p in enumerate(players):
        rank[p] = i+1
        name[i+1] = p
    for now in callings:
        i = rank[now]
        rank[name[i-1]] += 1
        rank[now] -= 1
        name[i], name[i-1] = name[i-1], name[i]
    return list(name.values())
