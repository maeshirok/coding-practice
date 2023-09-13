'''
2023/08/22
足し算
'''

def add(a: float, b: float) -> float:
    return a + b

if __name__ == '__main__':
    a = 5
    b = 6
    print(f'{a} + {b} = {add(a, b)}')