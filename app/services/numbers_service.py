# -*- coding: utf-8 -*-

from app.models.numbers import Numbers

def sum_numbers(numbers):
    return Numbers(numbers).sum()

def average_numbers(numbers):
    return Numbers(numbers).average()