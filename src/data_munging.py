import datetime
import json
import os
from os import path
import pandas as pd

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


class DataMunge(object):
    @staticmethod
    def group_loans(loan):
        """
        a.2 create a new attribute that buckets “Loan_Amount_000” into reasonable groups
        """
        if loan < 200:
            return 'Low (0-200,000)'
        elif loan < 1000:
            return 'Medium (200,000-1,000,000)'
        else:
            return 'High ( > 1,000,000)'

    def hmda_init(self):
        """
        a.1 Merge the application data with institution data such that each loan application is assigned a “Respondent_Name”.
        hmda_init() – Read the data files and return a pointer or object containing the expanded HMDA data from part a.
        :return: pandas DataFrame
        """

        fname1 = path.expanduser('~/Desktop/2012_to_2014_loans_data.csv')
        fname2 = path.expanduser('~/Desktop/2012_to_2014_institutions_data.csv')

        institutions = pd.read_csv(fname2, dtype=INSTITUTIONS_DF,
                                   na_values=['NA      ', 'NA    ', 'NA   ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', ''],
                                   error_bad_lines=False, skipinitialspace=True)

        loans = pd.read_csv(fname1, dtype=LOANS_DF,
                            na_values=['NA      ', 'NA    ', 'NA   ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', ''],
                            error_bad_lines=False, skipinitialspace=True)

        final_loans_data = loans.merge(
            institutions[['As_of_Year', 'Respondent_ID', 'Agency_Code', 'Respondent_Name_TS']],
            how='left', on=['As_of_Year', 'Respondent_ID', 'Agency_Code'])
        final_loans_data['Loan_Groups'] = final_loans_data.Loan_Amount_000.apply(DataMunge.group_loans)
        return final_loans_data

    def hmda_to_json(self, data, states=None, conventional_conforming=None):
        """
        hmda_to_json(data, states, conventional_conforming) – Export the expanded data set to disk for the states 
        filtered by product segment.
        """
        query = ''''''
        if (states and conventional_conforming):
            query = 'State in' + str(states) + 'and Conventional_Conforming_Flag ==' + str(conventional_conforming)

        if query and "" < query:
            data.query(query, inplace=True)

        fname = "loans_inst_merged.json"
        output_path = os.path.join(os.path.realpath('Desktop/'), 'processed', fname)
        try:
            data_dict = json.loads(data.head(5).to_json(orient='records'))
            with open(output_path, 'w+', encoding='utf-8') as f:
                json.dump(data_dict, f, sort_keys=True)
        except:
            raise Exception("Error in exporting to JSON")

        return True


if __name__ == '__main__':
    dlt = DataMunge()
    df = dlt.hmda_init()
    dlt.hmda_to_json(df)