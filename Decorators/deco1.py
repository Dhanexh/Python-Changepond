def Demo():
    print('Inside Demo')

def Fun():
    print('Inside Fun')

def Hello(THER):
    print('Inside Hello')
    THER()

Hello(Demo)