# Euro 2020 Guesser

Just some stupid guesser to compare ones own betting performance :-)

## Usage

One needs to update the matches excel under data/input and run main.py.

## Guesser

The Age-guesser bets 1-0, resp. 2-1 for the team which has the higher mean age. 
"It's all about experience", so one could also name it the Oliver-Kahn guesser. 

The Ranking-guesser bets 1-0 resp. 2-1 for the team with the higher points regarding the fifa world ranking, last updated on the 27th of May 2021.

## Betting points

The scoring is based on the "classic" Kicktipp scoring system. 4 points for a correct result, 3 points for the correct goal difference, 2 points for the correct tendency. 

## Data

Ages taken from https://www.reddit.com/r/soccer/comments/nqjys5/the_average_age_of_every_squad_in_the_euro/

FIFA world ranking taken from https://www.kaggle.com/cashncarry/fifaworldranking?select=fifa_ranking-2021-05-27.csv

## Evaluation 

After 11 matches :

| Guesser        |   Points |
|:---------------|---------:|
| AgeGuesser_10  |       22 |
| RankGuesser_10 |       21 |
| AgeGuesser_21  |       21 |
| RankGuesser_21 |       19 |