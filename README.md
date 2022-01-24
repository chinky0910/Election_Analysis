# Election-Analysis

Overview of Election Audit

Tom, a Colorado Board of Elections employee, needs assistance with the following tasks to complete the election audit of a recent local congressional election.
Calculate the total number of votes cast.
Get a complete list of counties that had a turnout.
Calculate the voter turnout for each county.
Calculate the percentage of votes each county cast.
Determine the county with the largest turnout.
Get a complete list of candidates who received votes.
Calculate the total number of votes each candidate received.
Calculate the percentage of votes each candidate won.
Determine the winner of the election based on popular vote.
Tom's manager wants to automate the process of generating a vote count report using Python.

Election-Audit Results

The analysis of the election shows that:
There were 369,711 total votes cast in this congressional election.
The counties results:
Jefferson county had 10.5% of the total vote with 38,855 votes.
Denver county had 82.8% of the total vote with 306,055 votes.
Arapahoe county had 6.7% of the total vote with 24,801 votes.
Denver county had the largest number of votes.
The candidate results:
Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
Diana DeGette received 73.8% of the vote and 272,892 votes.
Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
The winner of the election was Diana DeGette, who received 73.8% of the vote and 272,892 votes.

<img width="532" alt="Election_result_terminal" src="https://user-images.githubusercontent.com/95595378/150712727-13ea19b7-3857-4c8d-92fd-decf1ccdf0dc.png">

Election-Audit Summary

This script is extremely useful since it can be modified for any election, one can use this script in any election in general by entering a dataset that consists of a number for the ballot ID and a name for the county and candidate to determine: total number of votes cast, a complete list of candidates who received votes, total number of votes each candidate received, percentage of votes each candidate won, the winner of the election based on popular vote, the voter turnout for each county, the percentage of votes from each county out of the total count, and the county with the highest turnout. 
This script can be modified to fit any type of election. For example, if we wanted to analysis a federal congressional election, all we need to do is change the counties to states i.e by replacing the ”county list” with the “state list” and run an analysis for each state rather than for each county.
