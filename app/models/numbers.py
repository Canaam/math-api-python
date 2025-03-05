# -*- coding: utf-8 -*-

class Number:
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("A divisao por zero nao e permitida")
        return a / b

class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def average(self):
        if not self.numbers:
            raise ValueError("A lista nao pode estar vazia")
        return self.sum() / len(self.numbers)