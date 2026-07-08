import pandas as pd

my_dataset={
    'cars': ['BMW', 'Volvo', 'Ford'],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(my_dataset)

print(myvar)