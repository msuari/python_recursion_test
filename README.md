# PYTHON_RECURSION_TEST

## Scope of the test
Write a production-ready function that sums the numbers in a file.
The function will receive as input the path to a file.
Each line of the file will contain either a number or a path to another file.
For each file, output the file path and the sum of the numbers contained
both directly in the file or in any of the sub files listed (or their sub files, etc).

For example, if file A.txt contains:
```
3
19
B.txt
50

```
And file B.txt contains:
```
C.txt
27

```
And file C.txt contains:
```
10
2

```
The sum of A.txt and its subfiles is 111, sum for B.txt is 39, and sum for C.txt is 12.

## Installation
- To use the script it's recommended to use a virtual envirnoment.
```
pip install virtualenvwrapper
mkvirtualenv --python /usr/bin/python3.8 test
pip install -r requierements.txt
```

## Usage

```
PYTHONPATH=".:$PYTHONPATH" python scripts/sum_files.py tests/data/file_a.txt
```

## Tests
```
# Install tox
pip install tox

# run tox
tox
```
