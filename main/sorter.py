# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 21:37:51 2016

@author: Solomon
"""
import os
import csv 
from operator import itemgetter
import json

MYDIR = os.path.dirname(__file__)
f = open(os.path.join(MYDIR, 'Violations-2012.csv'))

csv_f = csv.reader(f)

def sort(unsorted_list):
    sorted_list = sorted(unsorted_list, key=itemgetter(1))
    return sorted_list

def separate(sorted_list):
    last_item = len(sorted_list) - 1
    violation_with_dates = [sorted_list[0][0], len(sorted_list),sorted_list[0][1], sorted_list[last_item][1]]
    return violation_with_dates
    
    
def create_violation_list():
    list_set = set()
    for row in csv_f:
        violation_category = str(row[2].replace(';', ' '))
        list_set.add(violation_category)
        list_set.discard('violation_category')
    f.seek(0)
    return sorted(list(list_set))
    
def createFinalList(list_of_violations):
    final_list = list()
    for categories in list_of_violations:
        category_list = list()
        for row in csv_f:
            true_category = str(row[2].replace(';', ' '))
            if true_category == categories:
                violation_with_date = [row[2].replace(';', ' '), row[3].replace(' 00:00:00','')]
                category_list.append(violation_with_date)
        final_list.append(separate(sort(category_list)))     
        f.seek(0)
        category_list = list()
    return final_list

def final_list_to_json(final_list):
    new_json = json.JSONEncoder().encode(final_list)
    return new_json
