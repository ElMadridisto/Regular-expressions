import csv

from input_pattern import input_pattern
from creates_dictionary import create_dict
from dictionary_convert_list import dict_conv_list

pattern = r"(^[А-Я][а-я]+)(\s|,)([А-Я][а-я]+)(\s|,)(([А-Я][а-я]+)((\s|,)+)(([А-Я][а-я]+|[А-Я]+),)((\w+\s\w+[\s,–]+(\w+\s)+\w+))?)?,((8|\+7)\s?\(?(\d{3})\)?[\s|-]?(\d{3})[\s|-]?(\d{2})[\s|-]?(\d{2})((\s)\(?(\w*.)\s(\d*)\)?)?)?"

with open('phonebook_raw.csv',encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    dict = create_dict(input_pattern(rows, pattern))

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(dict_conv_list(dict))