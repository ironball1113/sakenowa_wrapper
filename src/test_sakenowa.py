from sakenowa_wrapper import SakenowaAPI

# areasなど引数が一つの場合
sakenowa_areas = SakenowaAPI("areas")
print(sakenowa_areas.set_df().head())

# rankingsは総合ランキング（overall）の場合
sakenowa_rank_overall = SakenowaAPI("rankings", "overall")
print(sakenowa_rank_overall.set_df().head())

# 引数が正しくない場合
# sakenowa_failue = SakenowaAPI("failue")
# print(sakenowa_failue.set_df().head())


# --------------------出力結果--------------------

# The current endpoint is areas
# ==============================
#    id name
# 0   1  北海道
# 1   2  青森県
# 2   3  岩手県
# 3   4  宮城県
# 4   5  秋田県

# The current endpoint is rankings
# Rankings type is overall
# ==============================
#    rank     score  brandId
# 0     1  4.412219      109
# 1     2  4.100738      792
# 2     3  4.072851      660
# 3     4  4.072180     1033
# 4     5  4.065659       19

# Traceback (most recent call last):
#   File "test_sakenowa.py", line 12, in <module>
#     sakenowa_failue = SakenowaAPI("failue")
#   File "/app/src/sakenowa.py", line 32, in __init__
#     raise ValueError("引数が正しくありません。改めて指定してください。")
# ValueError: 引数が正しくありません。改めて指定してください。
