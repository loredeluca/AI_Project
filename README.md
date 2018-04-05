

# AI_Project

The project solves 18.9 problem of S.Russell, P.Norvig ["Artificial Intelligence: A Modern Approach"](https://www.pearson.com/us/higher-education/program/Russell-Artificial-Intelligence-A-Modern-Approach-3rd-Edition/PGM156683.html)

## Getting Started

Using this program is simple, you must insert in "main.py" the dataSet that you wish to classify.

There are 3 data sets already loaded in the project, chosen by the [UCI](http://archive.ics.uci.edu/ml/index.php) repository.
For the correct reading of the DataSet:
 - The first line must be the list of attributes
 - The last attribute must be the targetAttribute

### How read the output

The accuracy of the test was evaluated with CrossValidation, so the output will return a vector containing the accuracy for each test, followed by the average of accuracy

## Acknowledgments

* Thanks to S.Russell, P.Norvig ["Artificial Intelligence: A Modern Approach"](https://www.pearson.com/us/higher-education/program/Russell-Artificial-Intelligence-A-Modern-Approach-3rd-Edition/PGM156683.html) for theoretical explanations
* Thanks to [Christopher Roach](http://www.oreilly.com/pub/au/1904) and his article [Building Decision Trees in Python](http://archive.oreilly.com/pub/a/python/2006/02/09/ai_decision_trees.html?page=1) for helping me to structure decision trees correctly
