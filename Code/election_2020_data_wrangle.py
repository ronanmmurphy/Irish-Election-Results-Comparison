#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd
import csv
import numpy as np

#import 2020 excel file
xls_file = pd.ExcelFile('GalwayWest-2020.xlsx')
#get the specific sheet
xls_file.sheet_names

#parse the first sheet, the sheet with data
election_2020 = xls_file.parse('Sheet1')

#drop unneccessary columns
election_2020 = election_2020.drop(['2020 general election: Galway West','Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8',
             'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14',
             'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17'], axis = 1)

#rename columns needed
election_2020 = election_2020.rename(columns = {'Unnamed: 1': "Party",
                          'Unnamed: 2': "Candidate",
                        'Unnamed: 3': "Share",
                         'Unnamed: 4': "Votes"})

#return the rows needed in the file
election_2020 = election_2020.iloc[1:16] 
#get the party count of votes 
party_count = election_2020.groupby('Party').Votes.sum()
#print(party_count)

#export this to new excel file
#party_count.to_excel(r"C:\Users\ronan\Documents\AI Masters\Coursework\Data Visualisation\Assignment 3\party_count_2020.xlsx")

#convert the votes column to integer
election_2020['Votes'] = election_2020['Votes'].astype('int') 

#import 2016 significant candidates
xls_sign_2016 = pd.ExcelFile('significant_candidates.xlsx')
#get sheet 1 of this file
xls_sign_2016.sheet_names
sign_2016 = xls_sign_2016.parse('Sheet1')

#get top 5 candidates with highest votes
significant_candidates = election_2020.nlargest(5,'Votes')
#append the year 2020 to new column 'Year'
significant_candidates.insert(3,"Year", ["Year_2020","Year_2020","Year_2020","Year_2020","Year_2020"])
#print(significant_candidates)

#merge the two dataframes, this contains most significant candidates in both years
frames = [sign_2016, significant_candidates]

result = pd.concat(frames)
#drop the column for count number as all are from the first count
result = result.drop(['Count Number'], axis=1)
result.insert(4, "Rank", [1,2,3,4,5,1,2,3,4,5])
#print(result)
#export significant candidates to new excel file
#result.to_excel(r"C:\Users\ronan\Documents\AI Masters\Coursework\Data Visualisation\Assignment 3\All_significant_candidates.xlsx", index = False)

party_count_compare =party_count.to_frame()
party_count_compare.insert(1,"Year", ["Year_2020","Year_2020","Year_2020","Year_2020","Year_2020","Year_2020","Year_2020","Year_2020","Year_2020"])

party_count_compare.insert(0,"Party",["Aon","FF","FG","GP","Ind","LP","SF","SD","SPBP"])

indexNamesArr = party_count_compare.index.values
indexNamesArr
party_count_compare =party_count_compare.drop(["Aontú ","Solidarity–PBP "],axis=0)
party_count_compare

party_count_compare.to_excel(r"C:\Users\ronan\Documents\AI Masters\Coursework\Data Visualisation\Assignment 3\Compare_Party_2020.xlsx",index=False)
party_count_compare.reset_index(drop=True)
party_count_compare.reset_index(inplace=True) # Resets the index, makes factor a column
party_count_compare.drop("Factor",axis=1,inplace=True) 


average_percent =election_2020.groupby('Party').Share.sum()
average_percent = average_percent.to_frame()
average_percent.insert(1,"Year", ["Year_2020","Year_2020","Year_2020","Year_2020","Year_2020","Year_2020","Year_2020","Year_2020","Year_2020"])

average_percent.insert(0,"Party",["Aontú","Fianna Fáil","Fine Gael","Green Party","Independent","Labour Party","Sinn Féin","Social Democrats","Solidarity–PBP"])
average_percent
average_percent.to_excel(r"C:\Users\ronan\Documents\AI Masters\Coursework\Data Visualisation\Assignment 3\local_average.xlsx",index=False)


# In[ ]:




