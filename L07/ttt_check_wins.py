# 撰寫一程式，檔案名稱 ttt_check_wins.py
# 定義棋盤格狀態變數 cell_1 ~ cell_9 與目前的棋子變數 chess 如下，
# 檢查該棋子是否已經在該盤面上取得勝利條件，
# （任意直線上的三個格子的棋子皆和目前的棋子相同），
# 如果已經取得勝利條件，顯示 '{棋子} 勝利，結束程式'，並退出程式
# （請替換其值）

# 棋盤格變數：保存棋盤狀態的變數
# 變數編號對應的棋盤位置如下
#  1 | 2 | 3 
# ---+---+---
#  4 | 5 | 6 
# ---+---+---
#  7 | 8 | 9 
cell_1 = ' '
cell_2 = ' '
cell_3 = 'o'
cell_4 = 'x'
cell_5 = 'o'
cell_6 = 'o'
cell_7 = 'x'
cell_8 = ' '
cell_9 = 'x'
# 目前棋子變數：保存目前使用的棋子
chess = 'x'

# 使用者指定棋子位置
# TODO: 程式寫這裡
position=int(input())
if position == 1 and cell_1 !=' ':
  print('錯誤')
  exit()
elif position ==2 and cell_2 !=' ':
  print('錯誤')
  exit()
elif position ==3 and cell_3 !=' ':
  print('錯誤')
  exit()
elif position ==4 and cell_4 !=' ':
  print('錯誤')
  exit()
elif position ==5 and cell_5 !=' ':
  print('錯誤')
  exit()
elif position ==6 and cell_6 !=' ':
  print('錯誤')
  exit()
elif position ==7 and cell_7 !=' ':
  print('錯誤')
  exit()
elif position ==8 and cell_8 !=' ':
  print('錯誤')
  exit()
elif position ==9 and cell_9 !=' ':
  print('錯誤')
  exit()
# 根據指定位置，更新對應的棋盤格狀態變數 cell_1 ~ cell_9，
# TODO: 程式寫這裡
if position == 1:
  cell_1=chess
elif position ==2:
  cell_2=chess
elif position ==3:
  cell_3=chess
elif position ==4:
  cell_4=chess
elif position ==5:
  cell_5=chess
elif position ==6:
  cell_6=chess
elif position ==7:
  cell_7=chess
elif position ==8:
  cell_8=chess
elif position ==9:
  cell_9=chess


# 判斷是否勝利並顯示結果
# TODO: 程式寫這裡
if position==1 or position==8:
  print('勝利')