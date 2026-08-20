# Spelling Bee Puzzle Solver

## Use Cases
This is an app to solve a NYT Spelling Bee puzzle. The user enters the letters and date of a puzzle, and the app will return a list of valid solutions. The user can also view a summary of the puzzles they have solved using the app.

## Running the App
To run the app, clone this github repo. From within the root directory, run `docker compose up`. This will set up the docker containers for the database and the app. Once a connection is established, 
open a browser and navigate to `localhost:5000/` to access the UI. This can also be accessed by opening the `puzzle_solver.html` file in a browser.
You can submit requests without the UI using `curl` or tools like Postman. Detailed information about these requests can be found in `docs/documentation.md` or by navigating to `localhost:5000/doc` in the browser. 

## Acknowledgements
This app incorporates code from LING508 course materials. In particular, I referenced Jeff Berry's and Jackson Mostoller's example projects.  
The `lexicon.txt` file contains the master list of English words from which the solutions are chosen. It uses the ENABLE word list, which is freely available online. It has been edited to more closely align with the solutions considered valid by the NYT puzzle's editors. Specifically, all words with `s` are removed, and all words shorter than length 4 are removed.

## Future Updates 
This app can perform some basic functions. Some things I would like to add with more time include... 
- Looking up a past puzzle by date/ keeping a history of recent NYT puzzles in the database that is separate from the user's puzzle history.
- Formatting Improvements, especially with the solutions outputs and layout of the form's text input fields.
- Improving the lexicon/word list from which valid solutions are chosen. The word list currently contains some words that aren't considered valid by the NYT editors. Words longer than 8 letters need to be added to this list, too.