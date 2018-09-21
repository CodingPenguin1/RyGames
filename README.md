# RyGames

Python games by Ryan J Slater<br>
[GitHub](https://github.com/rjslater2000/RyGames)

Note: this repository has been replaced by [SlaterPythonGames](https://github.com/rjslater2000/SlaterPythonGames)

To install:<br>
`pip install rygames`

## Games

* CoinGame
* CountryGuessingGame
* Hangman
* TicTacToe1Player
* TicTacToe2Player
* TwentyFortyEight
* Warships

Run any of them by importing `rygames`, then calling, for example:

```
>>import rygames as rg
>>rg.Warships()
```

Make sure to install nltk, and run in ipython:

```
>>import nltk
>>nltk.download()
```

and:<br>
Change Here: /python3.6/site-packages/bs4/__init__.py, see end of file (last few lines)<br>
Change: soup = BeautifulSoup(sys.stdin) to soup = BeautifulSoup(sys.stdin, "html.parser")<br>
Then comment out the warning

```
#warnings.warn(self.NO_PARSER_SPECIFIED_WARNING % dict(
        #    filename=filename,
        #    line_number=line_number,
        #    parser=builder.NAME,
        #    markup_type=markup_type))
```

Save and close<br>
Do this to ensure that the Hangman game functions as intended.

## Requirements

* pygame >= 1.9.3
* numpy >= 1.13.3
* matplotlib >= 2.1.0
* PyDictionary >= 1.5.1
* nltk >= 3.2.4
* names >= 0.3.0
