from collections import defaultdict


def maxNumberOfBalloons(text: str) -> int:
    mp = defaultdict(int)
    for c in text:
        if c in "balon":
            mp[c] += 1
    
    if len(mp) < 5:
        return 0
    
    mp['l'] //= 2
    mp['o'] //= 2
    return min(mp.values())

print(maxNumberOfBalloons('balon'))