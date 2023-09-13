'''
2023/09/13
pythonで掛け算九九を行う
'''

def times_tables():
    '''
    1の段から9の段までの掛け算九九を行います。
    結果を表形式で出力します。
    '''
    for x in range(1, 10):
        for y in range(1, 10):
            #幅を2桁にすることで綺麗に出力
            print(f'{x * y:2}', end=' ')
        print()

if __name__ == '__main__':
    times_tables()