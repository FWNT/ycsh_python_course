# 撰寫一程式，程式檔名為 is_prime.py
# 提示使用者輸入一數字（100 以內的正整數），判斷此數字是否為質數，
# 若為質數，顯示 '是質數' ，反之顯示 '不是質數' 。
x=int(input('請輸入一數字'))
y=int(x*(1/2))
b=1
for i in range(y):
  b=b+1
  if x%b==0:
    print('不是質數')
    break 
  elif b==y:
    print('是質數')