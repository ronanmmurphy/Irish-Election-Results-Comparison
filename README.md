# Irish-Election-Results-Comparison
The Irish voting system uses a form of proportional representation called the single transferable vote.  Irish voters indicate their preferences for candidates in ascending order of preference; 1 for the most preferred candidate, 2 for the next preferred candidate and so on. The first preference votes are the ones counted in the first count of the vote counting process.  The counts indicated by the first count give the number of first preference votes that a candidate has received. This assignment uses first preferences votes to compare the performance between the 2016 and 2020 elections.

Data Wrangling: Python Scripts in Code folder (election_2020_data_wrangle.py & election_2020_data_wrangle.py)
The data needed to be transformed from the raw format into an accessible shape which could be easily used to appropriately compare these elections. Two short python script were written to transform the two original files for the 2016 and 2020 results. The unnecessary columns were removed with the rows of first count of votes. The statistics for most significant candidates and party count were added to separate dataframes and were exported as ‘party_count_2016.xlsx’ and ‘party_count_2020.xlsx’ and a combination of 2020 and
2016 top five candidates was added to ‘All_significant_candidates.xlsx’. This completed the data wrangling from the original raw files. Finally, a file was create to get the national average of first percentage votes per party. This was sources online for the 2016 and 2020 through Wikipedia data of the Irish elections. This file
contains three columns: the year, party name, percentage of first preference votes.These files were loaded to R studios rmd file to begin comparisons between the newly formatted data.

Data Visualisation Plots all plotted using R:
1. The vote per party in 2016 and 2020 election
![2016 Votes Per Party - Galway West](https://github.com/ronanmmurphy/Irish-Election-Results-Comparison/blob/main/Images/2016%20Votes%20per%20party.png?raw=true)

![2020 Votes Per Party - Galway West](https://github.com/ronanmmurphy/Irish-Election-Results-Comparison/blob/main/Images/2020%20Votes%20per%20party.png?raw=true)

2. The change in vote per party from 2016-2020

![2020 VS 2016 Votes per Party](https://github.com/ronanmmurphy/Irish-Election-Results-Comparison/blob/main/Images/compares%20votes%20per%20party.png?raw=true)

3. A comparison to the national average for party share of the vote

![National VS Local 1% Votes](https://github.com/ronanmmurphy/Irish-Election-Results-Comparison/blob/main/Images/localvsnational.png?raw=true)

4. The change in vote for the most significant candidates in both elections.

![Compare Most Significant Candidates](https://github.com/ronanmmurphy/Irish-Election-Results-Comparison/blob/main/Images/most_significant_candidates.png?raw=true)
