import datetime
import os
from os import path
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.pyplot import cm
%matplotlib inline
plt.clf()

LOAN_DF = {'Agency_Code': 'str',
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
INSTITUTION_DF = {'Agency_Code': 'str',
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



fname1 = path.expanduser('~/Desktop/2012_to_2014_loans_data.csv')
loans = pd.read_csv(fname1, dtype=LOAN_DF,
                                na_values=['NA      ', 'NA    ', 'NA   ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', ''],
                                error_bad_lines=False, skipinitialspace=True)
fname2 = path.expanduser('~/Desktop/2012_to_2014_institutions_data.csv')
institutions = pd.read_csv(fname2, dtype=INSTITUTION_DF,
                                       na_values=['NA      ', 'NA    ', 'NA   ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', ''],
                                       error_bad_lines=False, skipinitialspace=True)

flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]

total_amount_group_year = loans[['Loan_Amount_000', 'State', 'As_of_Year']] \
        .groupby(['State', 'As_of_Year']) \
        .agg({"Loan_Amount_000": 'sum'}) \
        .reset_index().sort_values(by=['Loan_Amount_000','State','As_of_Year'], ascending=False)

total_amount_group_year['Loan_Amount_000'] /= 1000
sns.set(style="whitegrid")

# Draw a nested barplot to show total loan amount for state and year
g = sns.factorplot(x="State", y="Loan_Amount_000", hue="As_of_Year", data=total_amount_group_year,
                   kind="bar",size=6, palette=sns.color_palette(flatui))
g.despine(left=True)
g.set_ylabels("Total Loan Amount",fontsize=15)
g.set_xlabels("State",fontsize=15)
g.set(title="Total Loan Amount aggregated by State and Year")
g.set_yticklabels(fontsize=15)
g.set_xticklabels(fontsize=15)

count_amount_group_year = loans[['Loan_Amount_000', 'State', 'As_of_Year']] \
        .groupby(['State', 'As_of_Year']) \
        .agg({"Loan_Amount_000": 'count'}) \
        .reset_index().sort_values(by=['Loan_Amount_000','State','As_of_Year'], ascending=False)

sns.set(style="whitegrid")

# Draw a nested barplot to show count of loans for state and year
g = sns.factorplot(x="State", y="Loan_Amount_000", hue="As_of_Year", data=count_amount_group_year,
                   kind="bar",size=6, palette=sns.color_palette(flatui))
g.despine(left=True)
g.set_ylabels("Count of Loans",fontsize=15)
g.set_xlabels("State",fontsize=15)
g.set(title="Count of Loans aggregated by State and Year")
g.set_yticklabels(fontsize=15)
g.set_xticklabels(fontsize=15)

avg_amount_group_year = loans[['Loan_Amount_000', 'State', 'As_of_Year']] \
        .groupby(['State', 'As_of_Year']) \
        .agg({"Loan_Amount_000": 'mean'}) \
        .reset_index().sort_values(by=['Loan_Amount_000','State','As_of_Year'], ascending=False)

sns.set(style="whitegrid")

# Draw a nested barplot to show Avg loan amount for state and year
g = sns.factorplot(x="State", y="Loan_Amount_000", hue="As_of_Year", data=avg_amount_group_year,
                   kind="bar",size=6, palette=sns.color_palette(flatui))
g.despine(left=True)
g.set_ylabels("Average Loan Amount",fontsize=15)
g.set_xlabels("State",fontsize=15)
g.set(title="Average Loan Amount aggregated by State and Year")
g.set_yticklabels(fontsize=15)
g.set_xticklabels(fontsize=15)

total_amount_purpose_group_year = loans[['Loan_Amount_000', 'State', 'Loan_Purpose_Description']] \
        .groupby(['State', 'Loan_Purpose_Description']) \
        .agg({"Loan_Amount_000": 'sum'}) \
        .reset_index().sort_values(by=['Loan_Amount_000','State','Loan_Purpose_Description'], ascending=False)

total_amount_purpose_group_year['Loan_Amount_000'] /= 1000
sns.set(style="whitegrid")

# Draw a nested barplot to show total loan amount for state and loan purpose
g = sns.factorplot(x="State", y="Loan_Amount_000", hue="Loan_Purpose_Description", data=total_amount_purpose_group_year,
                   kind="bar",size=6, palette=sns.color_palette(flatui))
g.despine(left=True)
g.set_ylabels("Total Loan Amount",fontsize=15)
g.set_xlabels("State",fontsize=15)
g.set(title="Total Loan Amount aggregated by State and Loan Purpose")
g.set_yticklabels(fontsize=15)
g.set_xticklabels(fontsize=15)

total_purpose_group_year = loans[['Loan_Amount_000', 'Loan_Purpose_Description', 'As_of_Year']] \
        .groupby(['Loan_Purpose_Description', 'As_of_Year']) \
        .agg({"Loan_Amount_000": 'sum'}) \
        .reset_index().sort_values(by=['Loan_Amount_000','Loan_Purpose_Description','As_of_Year'], ascending=False)

total_purpose_group_year['Loan_Amount_000'] /= 1000
sns.set(style="whitegrid")

# Draw a nested barplot to show total loan amount for loan purpose and year
g = sns.factorplot(x="Loan_Purpose_Description", y="Loan_Amount_000", hue="As_of_Year", data=total_purpose_group_year,
                   kind="bar",size=6, palette=sns.color_palette(flatui))
g.despine(left=True)
g.set_ylabels("Total Loan Amount",fontsize=15)
g.set_xlabels("Loan Purpose",fontsize=15)
g.set(title="Total Loan Amount aggregated by Year and Loan Purpose")
g.set_yticklabels(fontsize=15)
g.set_xticklabels(fontsize=15)

count_purpose_group_year = loans[['Loan_Amount_000', 'Loan_Purpose_Description', 'As_of_Year']] \
        .groupby(['Loan_Purpose_Description', 'As_of_Year']) \
        .agg({"Loan_Amount_000": 'count'}) \
        .reset_index().sort_values(by=['Loan_Amount_000','Loan_Purpose_Description','As_of_Year'], ascending=False)

sns.set(style="whitegrid")

# Draw a nested barplot to show count of loans for loan purpose and year
g = sns.factorplot(x="Loan_Purpose_Description", y="Loan_Amount_000", hue="As_of_Year", data=count_purpose_group_year,
                   kind="bar", size=6, palette=sns.color_palette(flatui))
g.despine(left=True)
g.set_ylabels("Count of Loans",fontsize=15)
g.set_xlabels("Loan Purpose",fontsize=15)
g.set(title="Count of Loans aggregated by Year and Loan Purpose")
g.set_yticklabels(fontsize=15)
g.set_xticklabels(fontsize=15)

avg_purpose_group_year = loans[['Loan_Amount_000', 'Loan_Purpose_Description', 'As_of_Year']] \
        .groupby(['Loan_Purpose_Description', 'As_of_Year']) \
        .agg({"Loan_Amount_000": 'mean'}) \
        .reset_index().sort_values(by=['Loan_Amount_000','Loan_Purpose_Description','As_of_Year'], ascending=False)

sns.set(style="whitegrid")

# Draw a nested barplot to show average loan amount for loan purpose and year
g = sns.factorplot(x="Loan_Purpose_Description", y="Loan_Amount_000", hue="As_of_Year", data=avg_purpose_group_year,
                   kind="bar",size=6, palette=sns.color_palette(flatui))
g.despine(left=True)
g.set_ylabels("Average Loan Amount",fontsize=15)
g.set_xlabels("Loan Purpose",fontsize=15)
g.set(title="Average Loan Amount aggregated by Year and Loan Purpose")
g.set_yticklabels(fontsize=15)
g.set_xticklabels(fontsize=15)