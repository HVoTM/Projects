# 181. Employees Earning more than Their Managers

import pandas as pd

# Example DataFrame (replace this with your actual DataFrame)
data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 80000, 60000, 90000],
    'managerId': [3, 4, None, None]
}

df = pd.DataFrame(data)
print(df)

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # extend the table, adding a new column of manager salary corresponding to the managerid
    # for comparison. if null, then salary value is 0

    # we will perform a merge, or table join to compare between the two columns
    # perform an inner join should do, so that we can see the corresponding managers with their employees
    # REMINDER: maybe should look at other join type to see what fits best
    merged_df = employee.merge(employee,how='inner',left_on='managerId', right_on='id', suffixes=('', '_manager'))

    merged_df['salary_manager'].fillna(0, inplace=True)
    merged_df['more_than_manager'] = merged_df['salary'] > merged_df['salary_manager']
    
    # test driver to check:
    # merged_df[['id', 'name', 'salary', 'managerId', 'name_manager', 'salary_manager', 'more_than_manager']]
    # print(merged_df)

    # leetcode's requirement for dataframe with column name is "Employee"
    merged_df.rename(columns={'name':'Employee'}, inplace=True) # inplace: if True, make sure the change is made on the original object (DataFrame)

    return merged_df[['Employee']][merged_df['more_than_manager'] == True] ## NOTE: double brackets [[]] to return a dataframe
    # friendly reminder df[] will return a NumpySeries i guess

print(find_employees(df))