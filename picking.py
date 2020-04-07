import pickle

car = (
    'tesla',
    'black',
    '2020',
    (
      (1, 'vano'),
      (2, 'lerok')
    )
)

with open('tesla.pickle', 'wb') as tesla_file:
    pickle.dump(car, tesla_file)