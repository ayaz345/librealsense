# License: Apache 2.0. See LICENSE file in root directory.
# Copyright(c) 2020 Intel Corporation. All Rights Reserved.
import time

# Timer that counts forward in time (vs backwards in the 'timer' class)
# It supply a basic stopwatch API, reset, get elapsed time..
class Stopwatch:

    _start = 0

    def __init__(self):
        self._start = time.perf_counter()

    # Reset the stopwatch time
    def reset(self, new_start_time = None):
        self._start = new_start_time if new_start_time else time.perf_counter()

    # Get elapsed since timer creation
    def get_elapsed(self):
        return time.perf_counter() - self._start

    # Get stopwatch start time
    def get_start(self):
        return self._start

