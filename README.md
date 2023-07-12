# Cricket Simulator
```bash
|   .gitignore			-- 	ignores certain files / file types from being tracked
|   driver.py           --  driver code
|   generator.py        --  generates a csv file containing 10 random players
|	globals.py			--	contains the global constants
|   player.py           --  player class
|   players.csv         --  pre-generated team
|   players_two.csv     --  pre-generated team
|   README.md           --  this file
+---outcome
|   |	ball_outcomes.py	-- TBE: generates ball by ball outcomes
|	|	probabilities.py	-- generates ball by ball probabilities
|   |   __init__.py
|
|
+---team                     --  'team' package
|   |    team.py             --  contains the Team class
|   |    teamInterace.py     --  contains the ITeam (interface) that every Team must abide by
|   |    team_generator.py   --  generates Team classes from a csv file
|   |    __init__.py
```