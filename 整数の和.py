# 1000以下の正の整数のうち、

# 3の倍数　もしくは　5の倍数　である
# 15の倍数ではない
# 上記を満たすものの総和を求め、表示させよ。

Normal_number = list(range(1, 1000))

Sum_number = 0
for num in Normal_number:
    if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
        Sum_number += num 

print(Sum_number)