import pandas as pd
import numpy as np
import random
import names   # random name generator - pip install names
import pandas_profiling    # pip install pandas_profiling

mock_data = []
for x in range(10000):
    person_id = x
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    phone_number = '+61-{}-{:04d}-{:04d}'.format(
        random.randint(2, 9),
        random.randint(1, 9999),
        random.randint(1, 9999)
    )
    some_val_1 = person_id + 1
    some_val_2 = first_name[::-1]  # reversed via slice
    some_val_3 = last_name + first_name
    # randomly leave last two attributes blank for some records
    if random.randint(1, 5) == 1:
        some_val_4 = np.NaN
        some_val_5 = np.NaN
    else:
        some_val_4 = person_id * random.randint(1, 9)
        some_val_5 = random.randint(-9999999, 9999999)
    person_record = {
        'person_id': person_id, 'first_name': first_name, 'last_name': last_name, 
        'phone_number': phone_number, 'some_val_1': some_val_1, 'some_val_2': some_val_2, 
        'some_val_3': some_val_3, 'some_val_4': some_val_4, 'some_val_5': some_val_5 
    }
    mock_data.append(person_record)
	
df = pd.DataFrame.from_dict(mock_data)
profile = pandas_profiling.ProfileReport(df)
profile.to_file(outputfile="/tmp/myoutputfile.html")