import pandas as pd

# 1. 读取 CSV 文件
# 假设文件编码为 utf-8，如果有乱码可以尝试改成 'gbk' 或 'utf-8-sig'
df = pd.read_csv("./zxfmxx_260220.csv")

# 打印原始数据行数
print(f"处理前的数据行数: {len(df)}")

# 2. 核心过滤逻辑：
# df['content'].str.contains('撤回了一条消息', na=False) 会返回一个布尔数组，包含该字符串的为 True
# 前面的 ~ 表示取反，也就是保留那些“不包含”该字符串的记录
# na=False 的作用是防止 content 列中有空值(NaN)导致报错
df_cleaned = df[(~df['msg'].str.contains('撤回了一条消息', na=False)) & (df['type_name'] == 'text')]

# 打印处理后的数据行数
print(f"处理后的数据行数: {len(df_cleaned)}")
print(f"删除了 {len(df) - len(df_cleaned)} 条记录")

# 3. 将处理后的数据保存到新的 CSV 文件中
# index=False 表示不将行索引写入文件
# encoding='utf-8-sig' 推荐用于包含中文的CSV，用 Excel 打开时不会乱码
df_cleaned.to_csv("zxfmxx_cleaned_260220.csv", index=False)