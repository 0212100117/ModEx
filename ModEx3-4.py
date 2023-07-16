def lazhopee(**kwargs):
    print('Your orders are:')
    for k, v in kwargs.items():
        print(k + ' -> ' + v)


lazhopee(computer='Acer', cellphone='Oppo', mouse='A4Tech', car='Ford')
