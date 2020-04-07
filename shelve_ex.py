import shelve

with shelve.open('shel_test') as cars_base:
    cars_base['opel'] = 'DE'
    cars_base['ford'] = 'US'
    cars_base['zaz'] = 'SU'

    print(cars_base['opel'])