import os

# 取得目前工作目錄
current_directory = os.getcwd()

# 取得上一層資料夾
parent_directory = os.path.dirname(current_directory)

print("現在的資料夾路徑是：", current_directory)
print("上一層資料夾路徑是：", parent_directory)