'''
2023/08/14
今年の経過した割合と残り日数を出力するコード
'''
from datetime import date

today = date.today()
years = date(today.year + 1, 1, 1)

diff_date = years - today
elapsed_rate = diff_date.days / 365 * 100
percentage_of_days_left = 100 - elapsed_rate

print(f'今年({today.year})は{"{:.5g}".format(percentage_of_days_left)}%経過しました。')
print(f'残り{diff_date.days}日です。')