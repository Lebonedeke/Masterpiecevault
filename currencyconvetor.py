
def currency_convertor():



    while True:
        amount = int(input('Enter amount: '))
        dollar = amount * 0.055
        euro = amount * 0.051
        pound = amount * 0.044

        print('here are the options: ')
        print("A. Dollar")
        print('B.Euro')
        print("C.Pound")
        print('')


        currency = input('Enter currency you want to convert to : ')

        if currency.upper() == 'a'.upper():
            print(f'$ {dollar} ')
        elif currency.upper() =='b'.upper():
            print(f'{euro} euros')
        elif currency.upper() =='c'.upper():
            print(f'{pound} pounds')
        else:
            print('unknoun option')
            quit()

currency_convertor()
