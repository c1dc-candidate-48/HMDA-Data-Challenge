{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\ftech\fcharset77 Symbol;\f2\fmodern\fcharset0 CourierNewPSMT;
\f3\fnil\fcharset128 HiraginoSans-W3;\f4\ftech\fcharset0 Wingdings-Regular;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid2\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li1440\lin1440 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid3\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li2160\lin2160 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\ri0\partightenfactor0

\f0\b\fs24 \cf0 # HMDA-Data-Challenge\
\pard\pardeftab720\ri0\partightenfactor0

\b0 \cf0 \
Analysis of HMDA data to determine the geography for Change Financial to enter into the Home Loans market.\
\
\
\pard\pardeftab720\ri0\partightenfactor0

\b \cf0 Code Organisation\
\pard\pardeftab720\ri0\partightenfactor0

\b0 \cf0 \
data_challenge\
\pard\pardeftab720\li720\fi-360\ri0\partightenfactor0
\ls1\ilvl0
\f1 \cf0 \'a5	
\f0 data\
\pard\pardeftab720\li1440\fi-360\ri0\partightenfactor0
\ls1\ilvl1
\f2 \cf0 o	
\f0 processed\
\pard\pardeftab720\li2160\fi-360\ri0\partightenfactor0
\ls1\ilvl2
\f3 \cf0 \uc0\u9827 
\f4 	
\f0 [file].json\
\ls1\ilvl2
\f3 \uc0\u9827 
\f4 	
\f0 outlier.txt\
\ls1\ilvl2
\f3 \uc0\u9827 
\f4 	
\f0 duplicate.txt\
\ls1\ilvl2
\f3 \uc0\u9827 
\f4 	
\f0 missing.txt\
\pard\pardeftab720\li720\fi-360\ri0\partightenfactor0
\ls1\ilvl2
\f1 \cf0 \'a5	
\f0 notebooks\
\pard\pardeftab720\li1440\fi-360\ri0\partightenfactor0
\ls1\ilvl1
\f2 \cf0 o	
\f0 visualization.ipynb\
\pard\pardeftab720\li720\fi-360\ri0\partightenfactor0
\ls1\ilvl1
\f1 \cf0 \'a5	
\f0 src\
\pard\pardeftab720\li1440\fi-360\ri0\partightenfactor0
\ls1\ilvl1
\f2 \cf0 o	
\f0 data_munging.py\
\ls1\ilvl1
\f2 o	
\f0 data_quality.py\
\ls1\ilvl1
\f2 o	
\f0 visualization.py\
\pard\pardeftab720\li720\fi-360\ri0\partightenfactor0
\ls1\ilvl1
\f1 \cf0 \'a5	
\f0 README.txt\
\pard\pardeftab720\ri0\partightenfactor0
\cf0 \
\pard\pardeftab720\ri0\partightenfactor0

\b \cf0 Data\
\pard\pardeftab720\ri0\partightenfactor0

\b0 \cf0 \
The data was obtained from the Consumer Financial Protection Bureau. The following data are used for the analysis (as obtained from the metadata included with the source data files)\
\
\pard\pardeftab720\ri0\partightenfactor0

\b \cf0 Metadata\
\pard\pardeftab720\ri0\partightenfactor0

\b0 \cf0 \
Data file(s)	Description\
2012_to_2014_loans_data.csv	Data on home loans.\
2012_to_2014_institutions_data.csv	Data about the institutions.\
\
Here is the schema of the expanded loans data.\
\
Field	Type\
As_of_Year	integer\
Agency_Code	integer\
Agency_Code_Description	string\
Respondent_ID	string\
Sequence_Number	integer\
Loan_Amount_000	integer\
Applicant_Income_000	integer\
Loan_Purpose_Description	string\
Loan_Type_Description	string\
Lien_Status_Description	string\
State_Code	integer\
State	string\
County_Code	integer\
MSA_MD	integer\
MSA_MD_Description	string\
Census_Tract_Number	integer\
FFIEC_Median_Family_Income	integer\
Tract_to_MSA_MD_Income_Pct	integer\
Number_of_Owner_Occupied_Units	integer\
County_Name	integer\
Conforming_Limit_000	integer\
Conventional_Status	string\
Conforming_Status	string\
Conventional_Conforming_Flag	string\
Respondent_Name_TS	string\
Loan_group string\
\
\pard\pardeftab720\ri0\partightenfactor0

\b \cf0 Getting Started\
\pard\pardeftab720\ri0\partightenfactor0

\b0 \cf0 \
Copy the csv data files on the desktop. Please note that the path for the data retrieval from csv files has been given in accordance with MAC OS system. The path file as mentioned in the python codes may change depending on the Operating System.\
\
\pard\pardeftab720\ri0\partightenfactor0

\b \cf0 Data Munging\
\pard\pardeftab720\ri0\partightenfactor0

\b0 \cf0 \
Data munging is done by running the data_munging.py module. This module will load the Loans and Institutions data from their respective csv files, assign a 'Respondent_Name' to each loan application and create a new categorical field 'Loan_Group'. Further it will dump all the data into a json file.Run the data munging module by going into the ./src subdirectory and type the following command\
\
python data_munging.py\
\
This will create a new json file that contains the merged loan and institution data and additional column (loan_group)\
\
\pard\pardeftab720\ri0\partightenfactor0

\b \cf0 Data Quality\
\pard\pardeftab720\ri0\partightenfactor0

\b0 \cf0 \
Data quality reports have been provided by using 'Loan_Amount_000' and 'Respondent_Name_TS' fields.This module will provide outlier, duplicate and missing data.\
Run the data quality module by going into the ./src subdirectory and type the following command\
\
python data_quality.py\
\
This will create three reports respective to above mentioned parameters.\
\pard\pardeftab720\ri0\partightenfactor0

\b \cf0 Analysis and Visualization\
\pard\pardeftab720\ri0\partightenfactor0

\b0 \cf0 \
Jupyter notebook has been used to provide analysis of the hypothesis. A source file has been provided in the ./src subdirectory with name visualization.py. Additionaly ./notebooks directory has visualization.ipynb file with full analysis and plots.\
\
}