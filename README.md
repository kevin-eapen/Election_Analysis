# Election Analysis (Audit)

## Election Audit Overview
The Colorado Board of Elections election commssion has requested an election audit of a recent local congressional election. I have been tasked with the following objectives to complete the election audit.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate the voter turnout for each county.
7. Calculate the percentage of votes from each county of the total count.
8. Determine the county with the highest turnout.

## Resources
- Data Source: election_results.csv
- Software: Python: 3.8.9, Visual Studio Code: 1.68.1

## Election Audit Results
- There were 369,711 total votes cast in the congressional election.

    <img src="https://github.com/kevin-eapen/Election_Analysis/blob/main/Images/Total_Votes.png" width="360">

- There are three counties in the precinct; Jefferson County, Denver County, and Arapahoe County. This is the breakdown of the number of votes and           percentage of total votes for each respective county.

  - Jefferson: 38,855 votes, accounting for 10.5% of the total votes cast in the election.
  - Denver: 306,055 votes, accounting for 82.8% of the total votes cast in the election.
  - Arapahoe: 24,801, accounting for 6.7% of the total votes cast in the election.

    <img src="https://github.com/kevin-eapen/Election_Analysis/blob/main/Images/County_Votes.png" width="360">

- Denver county had the largest voter turnout, with 306,855 votes cast.

    <img src="https://github.com/kevin-eapen/Election_Analysis/blob/main/Images/Largest_Turnout_County.png" width="420">

- There are three candidates, who received votes, running for the election; Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. This is the     breakdown of the number of votes and percentage of total votes for each respective candidate.
    
  - Charles Casper Stockham: 85,213 votes, accounting for 23.0% of the total votes cast in the election.
  - Diana DeGette: 272,892 votes, accounting for 73.8% of the total votes cast in the election.
  - Raymon Anthony Doane: 11,606, accounting for 3.1% of the total votes cast in the election.

    <img src="https://github.com/kevin-eapen/Election_Analysis/blob/main/Images/Candidate_Votes.png" width="500">

- Congressional election candidate, Diana DeGette, won the election by receiving the most votes among the candidates in the race. In the final results,       Diana DeGette received 272,892 votes, accounting for 73.8% of the total votes in the election.

    <img src="https://github.com/kevin-eapen/Election_Analysis/blob/main/Images/Winner_Votes.png" width="400">

## Election Audit Summary
It may prove helpful to the 'Colorado Board of Elections' election commission, that the logic used in this election audit analysis can be applied to run a similar audit analysis accross any election (given a dataset with like features as in the 'election_results.csv' resource). The code script may have to be minimally modified for the same program and underlying logic to work for a different election. Here are two examples of such cases:
- Example 1: Tied Candidate Votes
  - For this case we must modify the code in lines 145-148, as well as add a new conditional method to printing the election results depending on either a     numerical victory outcome or election tie outcome.
    - This could be accomplished by including an elif statment to the conditional in lines 145-148, and then another conditional statment under line 156         to decide which result to print. These modifications could be implemented in the code such as...
      
      (First, intialize 3 new variables under line 30 of the script. variable #1: "tie_candidate_votes = 0", variable #2: "tie_candidates = []", and             variable #3: tie_percentage = 0
      (Next,under line 148)
      ...
          elif votes == winning_count:
              tie_candidate_votes = votes
              tie_candidates.append(candidate_name)
              tie_percentage = vote_percentage
      (under line 156, and eventually move print statment on line 157 to following conditional)
      (intialize variable for number of tied candidates. variable: n_candidate_ties = range(tie_candidates))
      (add the conditional for which results to print and the code for what will be printed)
      if tie_candidate_votes == winning_count:
        print(
        f"\n{'-'*25}\n"
        f"The following canidates are tied for the election lead:\n"
        )
        for i in n_candidate_ties
            print(f"{tie_candidates[i]}\n")
        print(
        f"Tie Vote Count: {tie_candidate_votes:,}\n"
        f"Tie Precentage: {tie_percentage:.1}%\n" 
        f"\n{'-'*25}\n"
        )
      else:
        print(winning_candidate_summary)
      ...
- Example 2: Tied County Voter Turnout
  - For this case we must modify the code in lines 112-115, as well as add a new conditional method to printing the largest county turnout results             depending on either a numerical lead for one county or a tie in voter turnout.
      - This could be accomplished by including an elif statment to the conditional in lines 112-115, and then another conditional statment under line 122         to decide which result to print. These modifications could be implemented in the code such as...
      
      (First, intialize 2 new variables under line 37 of the script. variable #1: "tie_turnout_votes = 0" and variable #2: "tie_turnout_counties = []"
      (Next,under line 115)
      ...
          elif county_total_votes == largest_turnout_votes:
              tie_turnout_votes = county_total_votes
              tie_turnout_counties.append(county_name)
      (under line 122, and eventually move print statment on line 123 to following conditional)
      (intialize variable for number of tied counties. variable: n_county_ties = range(tie_turnout_counties))
      (add the conditional for which results to print and the code for what will be printed)
      if largest_turnout_votes == tie_turnout_votes:
        print(
        f"\n{'-'*25}\n"
        f"The following counties are tied for the largest voter turnout:\n"
        )
        for i in n_county_ties
            print(f"{tie_turnout_counties[i]}\n")   
        print(f"\n{'-'*25}\n")
      else:
        print(largest_turnout_result)
      ...

Essentially, the underlying logic for the election audit analysis program can be applied to future elections' analyses. However, edge cases (like the two examples above) must be considered, and necessary modifications to the existing script should be considered on a case-to-case basis.
