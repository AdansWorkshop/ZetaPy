# ZetaPy
A custom language with a parser made in python

# Requirements
Python >= 3.7

# Methods
out {operator} {value1} {value2} values can be args variables or numbers - Evaluates equation and prints answer

out {text} - Prints text

out {args} - Prints args from "each" for example

set {varName} {value} - Value can be rand {start} {stop}, index {listName} {index}, in {prompt}, mathematics, or iter {values seperated by space} - sets the variable name to equal the value

unset {varName} - Unsets variable

each {listName} {codeToRun} - For loop. args equals the current value in the list

each {amount of times to run} {codeToRun} - For loop. args equals the current amount of times the loop has been run

incremental controls {varName} ++, {varName} --, {varName} += {increment value}, and {varName} -= {decrement value}
