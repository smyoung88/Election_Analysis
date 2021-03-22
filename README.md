# Election_Analysis

## Project Overview of Election Audit
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election.<br>
The purpose of this project was to break out analysis based on both candidates and counties.

### County Analysis
The Board of Elections employee was interested in a breakdown of each of the following for each county:

1. A complete list of all counties where votes were cast.
2. The total number of votes each county received.
3. The percentage of votes each county had out of the total votes.
4. The county with the largest number of voters.

### Candidate Analysis
The Board of Elections employee was interested in a breakdown of each of the following for each candidate:

1. Total number of votes cast.
2. A complete list of candidates who received votes.
3. The total number of votes each candidate received.
4. The percentage of votes each candidate won.
5. The winner of the election based on popular vote.

## Election-Audit Results

The analysis of the election is summarized in the following image generated from the text file delivered to the Board of Elections:
<p align="left">
    <img src="https://github.com/smyoung88/Election_Analysis/blob/main/analysis/election_results_image.png">
</p>

## Challenge Summary
The script that was generated for this challenge can be utilized in many different ways for future elections. Some of those ways are summarized below:
1. Initially, the commision was only interested in results by candidate and then decided they wanted statistics based off of the county. If any other data is gathered during the election like age, sex, nationality, etc. that is of interest, the code can be modified to include those categories just like it was done with counties. As seen in the following snapshot of code, only a few extra lists, dictionaries, and variable needed to be added to generate those statistics i.e. county_options, county_votes, highest_turnout, cwinning_count, and cwinning_percentage.
<img src="https://github.com/smyoung88/Election_Analysis/blob/main/analysis/Script_categories.png">

2. If the commission employee went from being in charge of only Colorado's results to many states and more election results were received multiple states (more files in 'Resources'), those additional election_results files could be added to the code and seperate results could be pulled within the same script.

<img src="https://github.com/smyoung88/Election_Analysis/blob/main/analysis/resources_and_analysis.png">

The initial variables to load and save could change to "file_to_load_CO and file_to_save_CO" for Colorado results and the respective resources and analysis files would be "election_results_CO.csv and election_results_CO.txt". Each state would have its own data files to open and analysis txt files to write results to. This code could easily scale for the entire United States and would make election result analysis as simple as pressing a button once all information is gathered.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.54
