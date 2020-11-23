# 撰寫一排序程式，檔案名稱 sort2.py
# 提示使用者輸入三個數字，將數字由大至小分行顯示
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
x=max(a,b,c)
y=min(a,b,c)
z=a+b+c-x-y
print(x)
print(z)
print(y)
