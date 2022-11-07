"""
tomlファイルの読み込み
"""
import toml

with open('setting.toml', 'r') as f:
    data = toml.load(f)

print(data)

# tittleだけ取り出す
print(data['tittle'])

print(data["setting"]["app_name"])