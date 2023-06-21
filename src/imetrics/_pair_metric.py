#!/usr/bin/env python3

### ---------------------------------------- ###
### Part of iMetrics                         ###
### (C) 2022 Eddy ilg (me@eddy-ilg.net)      ###
### MIT License                              ###
### See https://github.com/eddy-ilg/imetrics ###
### ---------------------------------------- ###

class _PairMetric:
    _name = None
    _has_error_map = False
    _precision = 2

    def name(self): return self._name
    def precision(self): return self._precision
    def has_error_map(self): return self._has_error_map

    def compute(self, data, ref, dims="hwc", compute_map=False):
        raise NotImplementedError