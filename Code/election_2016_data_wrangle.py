#!/usr/bin/env python
# coding: utf-8

# In[58]:


# import csv
import pandas as pd
import numpy as np

#read in csv file with pandas dataframe
election_2016 = pd.read_csv("2016-04-28_general-election-count-details-galway-west-csv_en.csv")

#merge the candidate first and surname column into column 'Candidate' so comparable with 2020 data
election_2016["Candidate"] = election_2016["Candidate First Name"] + [" "] + election_2016["Candidate surname"]

#drop unnecessacary columns
election_2016 = election_2016.drop(['Constituency Name', 'Result', 'Transfers', 'Total Votes', 'Candidate Id','Candidate First Name', 'Candidate surname'], axis = 1) 

#return rows where count number is 1, only want 1st preference candidates
election_2016 = election_2016[election_2016['Count Number'] == 1]
#print(election_2016)

#get the top 5 candidates in 2016 election
significant_candidates = election_2016.nlargest(5,'Votes')
#append the year 2016 to each candidate in new column called 'Year'
significant_candidates.insert(4,"Year", ["Year_2016","Year_2016","Year_2016","Year_2016","Year_2016"])
#print(significant_candidates)

#export this file to new excel file
#significant_candidates.to_excel(r"C:\Users\ronan\Documents\AI Masters\Coursework\Data Visualisation\Assignment 3\significant_candidates.xlsx", index = False)

#get the total party count which is accumulation of all candidates votes in party
party_count = election_2016.groupby('Party').Votes.sum()

#export this to a seperate excel file
#party_count.to_excel(r"C:\Users\ronan\Documents\AI Masters\Coursework\Data Visualisation\Assignment 3\party_count_2016.xlsx")


party_count_compare =party_count.to_frame()
party_count_compare.insert(1,"Year", ["Year_2016","Year_2016","Year_2016","Year_2016","Year_2016","Year_2016","Year_2016","Year_2016","Year_2016","Year_2016"])
#party_count_compare[Party].replace({"Fianna Fail": "FF", "Fine Gael": "FG", "Green Party":"GP", "Labour Party": "LP", "Sinn Fein":"SF"}, inplace=True)
party_count_compare.insert(0,"Party",["AAA","DD","FF","FG","GP","Ind","LP","Ren", "SF","SD"])
party_count_compare

indexNamesArr = party_count_compare.index.values
indexNamesArr
party_count_compare = party_count_compare.drop(["AAA","Direct Democracy Ireland ","Renua"],axis=0)
party_count_compare.to_excel(r"C:\Users\ronan\Documents\AI Masters\Coursework\Data Visualisation\Assignment 3\Compare_Party_2016.xlsx",index=False)


# In[ ]:




