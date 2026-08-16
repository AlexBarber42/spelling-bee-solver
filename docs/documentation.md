# Spelling Bee Puzzle Solver

## Solve a Puzzle
Each NYT Spelling Bee puzzle has one required letter and 6 "outer" letters that the player can use to form words.
To use this solver, enter the required and outer letters in the appropriate fields. A date must also be selected. If you're not sure about the date of the particular puzzle you want to solve, a default date value will be chosen for you.
If you make a mistake while filling out the form or need to restart, you can click "Start Over", and the letter text boxes will be cleared for you.

After entering the puzzle information, simply click "Solve Puzzle" to view a list of valid words formed using the given letters.
The page will display the list of words sorted and grouped by length. The output will also contain the "pangrams" for that puzzle, which are the words formed using all of the given letters at least once.

### Sample Input and Output
If you want to solve August 16, 2026's puzzle, for example, you would input required letter `c` and letters `l`, `u`, `e`, `d`, `b`, and `o`.
The date can be selected using the calendar selection tool. After clicking "Solve Puzzle", the page will display the following output:

```json
{
  "1": {
    "Letters: ": "ldobeuc",
    "Pangrams: ": [
      "becloud",
      "beclouded"
    ],
    "Puzzle Date: ": "2026-08-16"
  },
  "4": [
    "bloc",
    "cede",
    "cell",
    "clod",
    "club",
    "clue",
    "cobb",
    "code",
    "coed",
    "cold",
    "cool",
    "cube",
    "cued",
    "cull",
    "deco",
    "loco"
  ],
  "5": [
    "bocce",
    "ceded",
    "celeb",
    "cello",
    "cloud",
    "clued",
    "coded",
    "cooed",
    "could",
    "cubed",
    "deuce",
    "educe"
  ],
  "6": [
    "boucle",
    "celled",
    "cobble",
    "coddle",
    "cooled",
    "coulee",
    "cuddle",
    "culled",
    "decode",
    "deduce",
    "educed"
  ],
  "7": [
    "clouded",
    "clubbed",
    "cobbled",
    "coddled",
    "collude",
    "cuddled",
    "occlude",
    "decoded",
    "deduced",
    "becloud",
    "cellule"
  ],
  "8": [
    "colluded",
    "occluded"
  ],
  "9": [
    "beclouded"
  ]
}
```

To call the API without the UI, you can submit a POST request to the endpoint `http://localhost:5000/puzzle`.

The POST request must contain a JSON body with the following keys and corresponding values for your particular puzzle:

```shell
curl -X POST "http://localhost:5000/puzzle" -H "Content-Type: application/json" -d '{"req": "c", "let1": "b", "let2": "d", "let3": "o", "let4": "e", "let5": "l", "let6": "u", "puzzdate": "2026-08-16"}'
```
This command gives the following output:
```shell
{"1":{"Letters: ":"bdolecu","Pangrams: ":["becloud","beclouded"],"Puzzle Date: ":"2026-08-16"},"4":["cede","cell","clod","club","clue","cobb","code","coed","cold","cool","cube","cued","cull","deco","loco","bloc"],"5":["bocce","ceded","celeb","cello","cloud","clued","coded","cooed","could","cubed","deuce","educe"],"6":["decode","deduce","educed","boucle","celled","cobble","coddle","cooled","coulee","cuddle","culled"],"7":["becloud","clouded","clubbed","cobbled","coddled","collude","cuddled","occlude","cellule","decoded","deduced"],"8":["colluded","occluded"],"9":["beclouded"]}
```

## Viewing User's Puzzle History
After the user has solved one or more puzzles with the program, the user can view the dates and letters of those puzzles. The user can press the "Get User History" button on the UI, and the "History" section of the page will show the stored information. 

- Sat, 15 Aug 2026 | Letters: a d r o i h c | Required Letter: o
- Sun, 16 Aug 2026 | Letters: b d o l e c u | Required Letter: c
- 
To do this without the API, submit a GET request to the endpoint `http://localhost:5000/history`.

To call directly with `curl`, 
```shell
curl -i -X GET "http://localhost:5000/history"
```
This command gives the following output:
```shell
[{"date":"Sat, 15 Aug 2026 00:00:00 GMT","letters":"adroihc","required_letter":"o"},{"date":"Sun, 16 Aug 2026 00:00:00 GMT","letters":"bdolecu","required_letter":"c"}]
```