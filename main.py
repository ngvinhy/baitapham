def tong(m, n):
    if m == n*n or n == m*m:
        return m + n
    else:
        return 0


n = int(input('Hãy nhập số cặp số: '))
S = 0
for i in range(1, n+1):
    a = int(input('Nhập vào số a: '))
    b = int(input('Nhập vào số b: '))
    s = tong(a, b)
    S = S + s
print('Tổng các số trong cặp số thỏa mãn bài toán là:', S)
