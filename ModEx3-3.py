def grab_food(*args):
    items = ''
    for item in args:
        items = items + '\n' + item
    print('Your orders are: {}'.format(items))


grab_food('pizza', 'burger', 'hotdog', 'fries', 'adobo')
