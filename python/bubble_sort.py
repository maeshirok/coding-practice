'''
2023/08/11
バブルソートを行うコード
'''

def bubble_sort(data):
    '''
    左の数字二つずつを対象に交換ができなくなるまでバブルソートを行う
    '''
    change = True

    for i in range(len(data)):
        if not change:
            break
        change = False
        for j in range(len(data) - i -1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                change = True
    return data

if __name__ == '__main__':
    DATA = [3, 8, 11, 6, 17, 5]
    sorted_data = bubble_sort(DATA.copy())

    print(f'old:{DATA}')
    print(f'new:{sorted_data}')