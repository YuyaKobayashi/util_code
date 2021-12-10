#!/usr/bin/env python3

import funtools
import itertools


# TODO: Python version check
class Iter:
    def __init__(self, iterable):
        self.x = iterable

    def cast_to(self, cls):
        return cls(self.x)

    def __iter__(self):
        return iter(self.x)

    ######################
    # Built-in functions #
    ######################

    def filter(self, func):
        return Iter(filter(func, self))

    def map(self, func):
        return Iter(map(func, self))

    def sort(self, *, key=None, reverse=False):
        return Iter(sorted(self, key=key, reverse=reverse))

    def enumerate(self):
        return enumerate(self)

    def zip(self, *iterables, strict=False):
        arg = [self] + iterable
        return Iter(zip(*arg, strict=strict))

    ############################
    # Common Reduce Operations #
    ############################

    def all(self):
        return all(self)

    def any(self):
        return any(self)

    def max(self):
        return max(self)

    def min(self):
        return min(self)

    def sum(self):
        return self.reduce(lambda x, y: x + y)

    #############
    # functools #
    #############

    def reduce(self, func, initializer=None):
        return functools.reduce(func, self, initializer)

    #############
    # itertools #
    #############

    def accumulate(self, func, initial=None):
        x = itertools.accumulate(func, self, initial=initial)
        return Iter(x)

    def chain(self, *iterable):
        arg = [self] + iterable
        return Iter(itertools.chain(*arg))

    def chain_from_iterable(self):
        return Iter(itertools.chain.from_iterable(self))

    def combinations(self, r):
        return Iter(itertools.combinations(self, r))

    def combinations_with_replacement(self, r):
        return Iter(itertools.combinations_with_replacement(self, r))

    def compress(self, selectors):
        return Iter(itertools.compress(self, selectors))

    def cycle(self):
        return Iter(itertools.cycle(self))

    def dropwhile(self, predicate):
        return Iter(itertools.dropwhile(self, predicate))

    def filterfalse(self, predicate):
        return Iter(itertools.filterfalse(self, predicate))

    def groupby(self, key=None):
        return Iter(itertools.groupby(self, key=key))

    def islice(self, start_or_stop, stop=None, step=1):
        # Use something like function overload for more elegant code
        if stop is None:
            x = itertools.islice(self, start_or_stop)
        else:
            x = itertools.islice(self, start_or_stop, stop, step)
        return Iter(x)

    def pairwise(self):
        return Iter(itertools.pairwise(self))

    def permutations(self, r=None):
        return Iter(itertools.permutations(self, r=r))

    def product(self, *iterables, repeat=1):
        arg = [self] + iterables
        return Iter(itertools.product(arg, repeat=repeat))

    def statmap(self, func):
        return Iter(itertools.starmap(func, self))

    def takewhile(self, predicate):
        return Iter(itertools.takewhile(self, predicate))

    def zip_longest(self, iterables, fillvalue=None):
        arg = [self] + iterables
        return Iter(itertools.product(arg, fillvalue=fillvalue))

