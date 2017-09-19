import datetime
import os
from os import path
import numpy as np
import pandas as pd


def check_outlier(data, col):
    """
    :param df:
    :param col:
    :return:
    """
    outlier_df = data[((data[col] - data[col].mean()) / data[col].std()).abs() > 6]
    base_filename = 'outlier.txt'
    with open(os.path.join(os.path.realpath('Desktop/'), 'processed', base_filename), 'w') as outfile:
        outlier_df.to_string(outfile)
    return


def check_duplicate(data, name):
    """
    :param df:
    :param name:
    :return:
    """

    # Composite key
    key_cols = ['Agency_Code', 'Respondent_ID', 'As_of_Year'] \
        if name == 'institutions' else ['Agency_Code', 'Respondent_ID', 'As_of_Year', 'Sequence_Number']

    duplicate_df = data[data.duplicated(key_cols, keep=False)]
    base_filename = 'duplicate.txt'
    with open(os.path.join(os.path.realpath('Desktop/'), 'processed', base_filename), 'w') as outfile:
        duplicate_df.to_string(outfile)
    return


def check_missing(data, col):
    """
    :param data:
    :param col:
    :return:
    """
    if data[col].dtype in ['str', 'O']:
        nans_df = data[data[col].str.strip().str.len() <= 3][data[col].str.upper().str.contains('NA')]
        missing_df = data[nans_df.index.values]
    else:
        missing_df = data[np.where(list(np.isnan(data[col])))[0]]

    base_filename = 'missing.txt'
    with open(os.path.join(os.path.realpath('Desktop/'), 'processed', base_filename), 'w') as outfile:
        missing_df.to_string(outfile)
    return


def data_quality(data, col, data_name):
    missing_list = check_missing(data, col)
    duplicates_list = check_duplicate(data, data_name)
    outliers_list = check_outlier(data, col)


if __name__ == '__main__':
    INSTITUTIONS_DF = {'Agency_Code': 'str',
                       'As_of_Year': 'int64',
                       'Assets_000_Panel': 'int64',
                       'Parent_City_TS': 'str',
                       'Parent_Name_TS': 'str',
                       'Parent_State_TS': 'str',
                       'Parent_ZIP_Code': 'str',
                       'Respondent_City_TS': 'str',
                       'Respondent_ID': 'str',
                       'Respondent_Name_TS': 'str',
                       'Respondent_State_TS': 'str',
                       'Respondent_ZIP_Code': 'str'}

    LOANS_DF = {'Agency_Code': 'str',
                'Agency_Code_Description': 'str',
                'Applicant_Income_000': 'str',
                'As_of_Year': 'int64',
                'Census_Tract_Number': 'str',
                'Conforming_Limit_000': 'float64',
                'Conforming_Status': 'str',
                'Conventional_Conforming_Flag': 'str',
                'Conventional_Status': 'str',
                'County_Code': 'str',
                'County_Name': 'str',
                'FFIEC_Median_Family_Income': 'float64',
                'Lien_Status_Description': 'str',
                'Loan_Amount_000': 'int64',
                'Loan_Purpose_Description': 'str',
                'Loan_Type_Description': 'str',
                'MSA_MD': 'str',
                'MSA_MD_Description': 'str',
                'Number_of_Owner_Occupied_Units': 'float64',
                'Respondent_ID': 'str',
                'Sequence_Number': 'int64',
                'State': 'str',
                'State_Code': 'int64',
                'Tract_to_MSA_MD_Income_Pct': 'float64'}

    fname1 = path.expanduser('~/Desktop/2012_to_2014_loans_data.csv')
    fname2 = path.expanduser('~/Desktop/2012_to_2014_institutions_data.csv')

    institutions = pd.read_csv(fname2, dtype=INSTITUTIONS_DF,
                               na_values=['NA      ', 'NA    ', 'NA   ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', ''],
                               error_bad_lines=False, skipinitialspace=True)

    loans = pd.read_csv(fname1, dtype=LOANS_DF,
                        na_values=['NA      ', 'NA    ', 'NA   ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', ''],
                        error_bad_lines=False, skipinitialspace=True)
    cols = 'Loan_Amount_000'
    data_quality(loans, cols, 'loans')
    cols = 'Respondent_Name_TS'
    data_quality(institutions, cols, 'institutions')