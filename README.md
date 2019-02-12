# EECS 293 Project 2

### Running This Project
This project is built for use as a command-line tool. Run the following command inside the project directory to see it work:

```
py . "a+b/c" -v
```

You should see the resulting expression tree outputted using the root node's to_list() method. Feel free to change the expression argument as you please.

The *expression* argument to this command should be fairly self-explanatory, and the *-v* option tells the program to print the final output to the console.

### Testing This Project
This project was tested using pytest. Run the following command inside the project directory to run the test suite:

```
py -m pytest
```