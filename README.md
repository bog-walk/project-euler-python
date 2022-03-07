# Project Euler __ Python
___
A Python solution set for the first 100 problems corresponding to the [Project Euler](https://projecteuler.net/archives) challenges.

Problem content on the Project Euler site is licensed under [CC BY-NC-SA 4.0](https://projecteuler.net/copyright).

Some problems have been altered to either generalise their goal or implement further constraints, as influenced by the 
problem outlines found on [HackerRank](https://www.hackerrank.com/contests/projecteuler/challenges).

70/100 solved: :snake: :snake: :snake: :snake: :snake: :snake: :snake: :black_circle: :black_circle: :black_circle:

### Structure Guideline

---
Within the **solution package**, problem solutions are separated into batches with 10 solution modules per sub-package. 
Each problem has a corresponding test class located in the matching batch within the **test package**.

If a function is used in multiple solutions, it is elevated out of its original module and placed in the 
**util package**. This package contains custom classes and helper functions (as well as their unit tests) for 
combinatorics, mathematics, search algorithms, string processing, and test automation.

### Sibling Repository

---
The original solution set was written in Kotlin:
- [Project Euler __ Kotlin](https://github.com/bog-walk/project-euler-kotlin)