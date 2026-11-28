# print(2 * 5)
# print(2 // 5)
# print(20 % 3)

# 文字列の型とインデックスとスライス
# print(type("Python"))

# word = "Python"
# # インデックス
# print(word[0])  # P
# # スライス
# print(word[1:5])  # ytho

# エスケープシーケンス
# print("こんにち\n世界")
# print(r"あいうえお\nかきくけこ")

# # f-string
# year = 2026
# price = 1000
# print(f"今年は{year}年で、価格は{price}円です。")

# # str.format
# print("今年は{}年で、価格は{}円です。".format(year, price))

# 文字列の反復
# print("Hello" * 5)
# 改行あり
print("お疲れ様です\n" + "國上です。")

# 複合代入演算子
# a = 100
# a += 1
# print("a += 1の結果は？")
# print(a)

# b = 100
# b -= 1
# print("b -= 1の結果は？")
# print(b)

# c = 4
# c *= 2
# print("c *= 1の結果は？")
# print(c)

# d = 24
# print(type(d))
# d /= 3
# print("d /= 1の結果は？")
# print(d)
# print(type(d))

name_list = ["Yamada","Suzuki","Takahashi"]
# print(name_list[0:2])

number_list = [1,2,3,4,5,6,7,8,9,10]
# print(number_list[::3])

# .copyの例
# listB  =  number_list.copy()
# print(listB)

# .extendの例
name_list.extend(number_list)
print(name_list)

# .indexの例 indexはあくまでリストの位置つまり(n-1)番目の数値を返す
print(name_list.index(9)) # 11 

