msg = 'hello users!'
def hello():
    print(msg)

hello()
def pack(one, two, three):
    list = [one, two, three]
    print(list)

pack(1,2,3)

def eat_lunch(list):
    if len(list) == 0:
        print('My lunchbox is empty!')   
        return
    print(f'First I eat {list[0]}.')
    print(f'Then I eat {list[1]}.')

lunchbox = ['sandwich', 'apple']
emptybox = []
eat_lunch(lunchbox)
eat_lunch(emptybox)

