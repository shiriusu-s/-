import pandas as pd
import matplotlib.pyplot as plt

# Excelファイルからデータを読み込む
excel_file = '/Users/takanorishimada/Desktop/python_lesson/data.xlsx'  # ファイル名を適切に変更してください
df = pd.read_excel(excel_file)

# データの最初の数行を表示
print(df.head(n=47))

# グラフ化
plt.figure(figsize=(6, 6))

# 例として、1つの列をグラフ化する（実際の列名に置き換える）
plt.plot(df['2009年'], label='2009 year')
plt.plot(df['2023年'], label='2023 year')

# グラフにタイトルとラベルを追加
plt.title('Data Visualization')
plt.xlabel('X-axis Label')
plt.ylabel('Minimum wage hourly amount')

# 凡例を追加
plt.legend()

# グラフを表示
plt.show()
