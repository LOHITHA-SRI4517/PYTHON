import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    set_a = set(a)
    
    # If 1 exists in a, Alice can remove all elements
    if 1 in set_a:
        if m % 2 == 1:
            print("Alice")
        else:
            print("Bob")
        continue
    
    cnt = 0
    
    # Count how many y are divisible by at least one x in a
    for y in b:
        for x in set_a:
            if y % x == 0:
                cnt += 1
                break
    
    # Winner depends on parity of cnt
    if cnt % 2 == 1:
        print("Alice")
    else:
        print("Bob")
