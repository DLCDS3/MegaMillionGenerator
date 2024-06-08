

# MegaMillionGenerator

Scared of the official random generator being rigged? How about this open-sourced generator so you can do-it-yourself! This program generates random draws for the Mega Millions lottery game.

## Terminal Usage


You can run the program from the command line with the following options:

- `-n` or `--number_of_draw`: The number of draws to generate (required).
- `-w` or `--avoid_numbers_white`: A list of white ball numbers to avoid (optional).
- `-y` or `--avoid_numbers_yellow`: A list of yellow ball numbers to avoid (optional).
- `-d` or `--duplicate_number`: Allow duplicate numbers across all sets (optional).

Here's an example:

```bash
python __init__.py -n 5 -w 1 s2 3 -y 1 -d
```
This will generate 5 draws, avoiding the white ball numbers 1, 2, and 3, and the yellow ball number 1. Duplicate numbers are allowed in the draws.

The program will print the generated draws to the console. Each draw is printed as a list of white ball numbers followed by a yellow ball number. For example:
```
White: [4, 5, 6, 7, 8], Yellow: 9
White: [10, 11, 12, 13, 14], Yellow: 15
...
```

## Python Usage
First, import the `Generator` class from the `MegaMillionGenerator` package:

```python
from MegaMillionGenerator import Generator
```

Then, create an instance of the Generator class. The constructor takes the following arguments:

`number_of_draw`: The number of draws to generate.
`avoid_numbers_white`: A list of white ball numbers to avoid.
`avoid_numbers_yellow`: A list of yellow ball numbers to avoid.
`duplicate_number`: A boolean value indicating whether duplicate numbers are allowed in the draws. Defaults to False.\

Here's an example:
```python
generator = Generator(number_of_draw=5, avoid_numbers_white=[1, 2, 3], avoid_numbers_yellow=[1], duplicate_number=False)
```

This will generate 5 draws, avoiding the white ball numbers 1, 2, and 3, and the yellow ball number 1. Duplicate numbers are not allowed in the draws.

To generate the draws, call the `generate_draws` method:
```python
generator.generate_draws()
```

This will generate the specified number of draws and store them in the resulting_draws attribute. You can access the generated draws like this:

```python
print(generator.resulting_draws)
```
