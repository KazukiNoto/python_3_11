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

"""
配列の読み込み
[2018, 2019, 2020]
"""
year_list = data["setting"]["year_list"]
print(year_list)
 

"""
マイナス値の読み込み
-10
"""
print(data["setting"]["minus_value"])


"""
ブーリアン値の読み込み
True
False
"""
print(data["setting"]["is_true"])
print(data["setting"]["is_false"])
