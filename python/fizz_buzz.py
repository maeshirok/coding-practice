'''
2023/09/12
pythonでFizzBuzzを行うコード
'''

def fizz_buzz():
    '''
    1から順に数を数えていき、3の倍数だと「Fizz」、5の倍数なら「Buzz」
    3と5の倍数なら「FizzBuzz」と出力
    '''
    for i in range(1, 50):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    fizz_buzz()