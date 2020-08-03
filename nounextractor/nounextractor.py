#!/usr/bin/env python
# encoding: utf-8

import argparse
import csv
import json
import nltk
import os
import sys


class Extractor(object):
    
    def find_entities(self, text):
        text = text.replace('-', ' '). \
                            replace('_', ' '). \
                            replace(';', ' '). \
                            replace("'", ' '). \
                            replace('"', ' '). \
                            replace(':', ' '). \
                            replace('’', ' ')
        text = nltk.word_tokenize(text)
        nes = nltk.ne_chunk(nltk.pos_tag(text))
        tokens = {}
        for ne in nes:
            if type(ne) is nltk.tree.Tree:
                if (ne.label() in ('GPE', 'PERSON', 'ORGANIZATION', 'LOCATION', 'FACILITY')):
                    tokens[u' '.join([i[0] for i in ne.leaves()])] = {'Label': ne.label()}
            else:
                if ne[1] in ('NN', 'NNPS', 'NNS', 'NNP'):
                    tokens[ne[0]] = {'Label': 'NOUN'}
        return tokens

  
def extract(file, column, args):
   e = Extractor()
   result = []
   if file is None or column is None:
       for text in args:
           result.append(e.find_entities(text))
   else:
       with open(file, 'r') as file:
           reader = csv.reader(file)
           first_row = True
           for row in reader:
               if not first_row and len(row) >= column +1:
                   text = row[column]
                   result.append(e.find_entities(text))
               first_row = False
   print(json.dumps(result))


def main():
    parser = argparse.ArgumentParser(description='Extract Noun from csv file')
    parser.add_argument('-f', '--file', help="CSV file path")
    parser.add_argument('-c', '--column', help="Index of parsing row", type=int)
    parser.add_argument('args', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    return extract(args.file, args.column, args.args)


if __name__ == "__main__":
    sys.exit(main())
