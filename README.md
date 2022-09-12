# Project Euler __ Python

A Python solution set for the first 100 problems corresponding to the [Project Euler](https://projecteuler.net/archives) challenges.

80/100 solved: :snake: :snake: :snake: :snake: :snake: :snake: :snake: :snake: :snake: :black_circle:

Problem content on the Project Euler site is licensed under [CC BY-NC-SA 4.0](https://projecteuler.net/copyright).

Some problems have been altered to either generalise their goal or implement further constraints, as influenced by the 
problem outlines found on [HackerRank](https://www.hackerrank.com/contests/projecteuler/challenges).

## :open_file_folder: Structure Guideline

Inside the **solution package**, problem solutions are separated into batches with 10 solution modules per sub-package.

Each problem has a corresponding test class located in the matching batch inside the **test package**.

If a function is used in multiple solutions, it is elevated out of its original module and placed in the 
**util package**. This package contains custom classes and helper functions (as well as their unit tests) for 
combinatorics, mathematics, search algorithms, string processing, and test automation.

## :handshake: Sibling Repository

The original solution set was written in Kotlin :desert_island:
- [Project Euler __ Kotlin](https://github.com/bog-walk/project-euler-kotlin)

Another project repository has been created to practise C++ :zap:
- [Project Euler __ C++](https://github.com/bog-walk/project-euler-cpp)