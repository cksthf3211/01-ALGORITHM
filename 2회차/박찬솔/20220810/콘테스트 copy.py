import sys
sys.stdin = open('콘테스트.txt')

W = sorted([int(input())for _ in range(10)])[7:]
K = sorted([int(input())for _ in range(10)])[7:]

print(sum(W), sum(K))