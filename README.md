# Project Euler __ Python
___
A Python solution set for problems corresponding to the
[Project Euler](https://projecteuler.net/archives) challenges.

Some problems have been altered to either generalise their goal or implement constraints, as
influenced by the problem outlines found on [HackerRank](https://www.hackerrank.com/contests/projecteuler/challenges).

Problem content on the Project Euler site is licensed under [CC BY-NC-SA 4.0](https://projecteuler.net/copyright).

### Structure Guideline

---
Problem solutions are separated into packages (*batch#*) with 10 solution modules per package. Each problem has a
corresponding test class that can be found in the matching test package.

If a function gets reused in a later solution, it is elevated out of its original module and
placed in the **util package**. Any custom/helper classes can also be found there.

### Sibling Repositories

---
The original solution set was written in Kotlin and a C++ project has recently been created:
- [Project Euler __ Kotlin](https://github.com/bog-walk/project-euler-kotlin)
- [Project Euler __ C++]()