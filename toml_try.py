"""
3.11から標準ライブラリだけで読み込み可能となったTOMLファイルの読み込み
"""
import toml

with open('setting.toml', 'r') as f:
    data = toml.load(f)

print(data)

# tittleだけ取り出す
print(data['tittle'])
