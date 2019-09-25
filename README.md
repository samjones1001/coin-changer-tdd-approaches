# Code Changer Kata - TDD Approaches ![Build Status](https://travis-ci.com/samjones1001/coin-changer-tdd-approaches.svg?branch=master) [![codecov](https://codecov.io/gh/samjones1001/coin-changer-tdd-approaches/branch/master/graph/badge.svg)](https://codecov.io/gh/samjones1001/coin-changer-tdd-approaches)

An exploration of different approaches to TDDing the same simple application.

This repo contains two branches `tdd-by-input` and `tdd-by-output`, both containing versions of the same coin-changer kata written in Python. The approach to testing is the only difference between the two versions.

### Setup

This project uses [pipenv](https://github.com/pypa/pipenv) to manage dependencies.

- Clone this repository and navigate to its root directory in the command line
- If not already present on your system, install pipenv using `pip install pipenv`
- Install dependencies using `pipenv sync -d`

### Tests

In order to run the test suite, navigate to the projects root directory in the command line, checkout the desired branch using either `git checkout tdd-by-input` or `git-checkout-tdd-by-output` and then run `pytest`.
