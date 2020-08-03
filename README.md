# noun-extractor

A simple python for extracting NOUN from CSV file


# Prerequisites

* Python 3.7
* nltk

# Install 

```
$ python setup.py install
```

# Usage

1. Input string directly
Input: array of string
Ouput: Json String
[
  {Token: {Label: Token_label},..
]

```
$ noun-extractor "I am from Taiwan" "This is a pen from Japan"
[{"Taiwan": {"Label": "GPE"}}, {"pen": {"Label": "NOUN"}, "Japan": {"Label": "GPE"}}]
```

2. Input csv file with header and column index
Input: array of string
Ouput: Json string
[
  {Token: {Label: Token_label},..
]


```
# Create a csv file with header
$ echo "col1,col2" > /tmp/test.csv
$ echo "1,I am from Taiwan" >> /tmp/test.csv

# Run: -f $FILE_PATH -c COLUMN_INDEX
$ noun-extractor -f /tmp/test.csv -c 1
[{"Taiwan": {"Label": "GPE"}}]
```

Noun Label 'GPE', 'PERSON', 'ORGANIZATION', 'LOCATION', 'FACILITY', 'NOUN'
