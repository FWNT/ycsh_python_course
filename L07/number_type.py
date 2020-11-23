# 撰寫一程式，程式檔名為 number_type.py
# 提示使用者輸入一整數，判斷此數字的奇偶與正負。
# 並顯示結果，結果如 '正偶數'、'偶數'、'負偶數'、'正奇數'、'負奇數'。
a=float(input('輸入一個整數'))
if a>0:
  if  a%2==0:
    print('正偶數')
  else:
    print('正奇數')
else:
  if  a%2==0:
    print('負偶數')
  else:
    print('負奇數')

