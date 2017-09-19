# HMDA-Data-Challenge

Analysis of HMDA data to determine the geography for Change Financial to enter into the Home Loans market. 

**Code Organization** 

data_challenge 
 

 - data
  - processed
     - [file].json
     - outlier.txt
     - duplicate.txt
     - missing.txt
 - notebooks
   - visualization.ipynb
 - src
   - data_munging.py
   - data_quality.py
   - visualization.py
 - Insight_Report.docx
 - README.md
 - requirements.txt


**Data**

The data was obtained from the Consumer Financial Protection Bureau. The following data are used for the analysis (as  obtained from the metadata included with the source data files)

**Metadata**

Data file(s)	Description \
2012_to_2014_loans_data.csv	Data on home loans. \
2012_to_2014_institutions_data.csv	Data about the institutions.

Here is the schema of the expanded loans data.

Field	Type \
As_of_Year	integer \
Agency_Code	integer \
Agency_Code_Description	string \
Respondent_ID	string \
Sequence_Number	integer \
Loan_Amount_000	integer \
Applicant_Income_000	integer \
Loan_Purpose_Description	string \
Loan_Type_Description	string \
Lien_Status_Description	string \
State_Code	integer \
State	string \
County_Code	integer \
MSA_MD	integer \
MSA_MD_Description	string \
Census_Tract_Number	integer \
FFIEC_Median_Family_Income	integer \
Tract_to_MSA_MD_Income_Pct	integer \
Number_of_Owner_Occupied_Units	integer \
County_Name	integer \
Conforming_Limit_000	integer \
Conventional_Status	string \
Conforming_Status	string \
Conventional_Conforming_Flag	string \
Respondent_Name_TS	string \
Loan_group string

**Setup**

Copy the csv data files on the desktop. Please note that the path for the data retrieval from csv files has been given in accordance with MAC OS system. Please change accordingly if you are working on some other operating system. The path file as mentioned in the python codes may change depending on the Operating System.

**Data Munging**

Data munging is done by running the data_munging.py module. This module will load the Loans and Institutions data from their respective csv files, assign a 'Respondent_Name' to each loan application and create a new categorical field 'Loan_Group'. Further it will dump all the data into a json file. Run the data munging module by going into the ./src subdirectory and type the following command

python data_munging.py

This will create a new json file that contains the merged loan and institution data and additional column (loan_group)

**Data Quality**

Data quality reports have been provided by using 'Loan_Amount_000' and 'Respondent_Name_TS' fields.This module will provide outlier, duplicate and missing data. Please create a folder named 'processed' on your desktop before moving onto the next step. Please keep in mind that the path given in the code is according to the MAC OS. Please change accordingly if you are working on some other operating system. After creating the folder, run the data quality module by going into the ./src subdirectory and type the following command

python data_quality.py

This will create three reports respective to above mentioned parameters.

**Analysis and Visualization**

Jupyter notebook has been used to provide analysis of the hypothesis. A source file has been provided in the ./src subdirectory with name visualization.py. Additionaly ./notebooks directory has visualization.ipynb file with full analysis and plots.
