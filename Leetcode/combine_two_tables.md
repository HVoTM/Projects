```py

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df2 = person.merge(address, how = 'left', on = 'personId')
    return df2[['firstName','lastName', 'city', 'state']]

```