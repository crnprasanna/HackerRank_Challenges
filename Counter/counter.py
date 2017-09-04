x = int(input())
shoe_size = list(map(int,input().split()))
n = int(input())
earnings = 0
for i in range(n):
    s, p = map(int,input().split())
    if s in shoe_size:
        earnings += p
        shoe_size.remove(s)
print(earnings)
