#1037 약수
# n=a*1,2,3.. and a!=1 and a!=n
# n 출력
c = int(input()) #진짜 약수의 개수
a = list(map(int,input().split()))
print(max(a)*min(a))
