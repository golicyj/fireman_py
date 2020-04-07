import shelve

with shelve.open('shel_test') as cars_base:
    cars_base['opel'] = 'DE'
    cars_base['ford'] = 'US'
    cars_base['lada'] = 'RU'
    cars_base['zaz'] = 'SU'

    #print(ca rs_base['opel'])
