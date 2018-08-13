#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License
#

"""
Mechanisms for handling timeouts.
"""

import threading
import time


class TimeoutCallback(threading.Thread):
    """
    This class can be used to start a timer as a non-blocking thread,
    and optionally invoke a callback_method (or list of methods)
    if a timeout has occurred.
    To start the timer, the start() method must be called.
    Once your task is completed, you must call the interrupt() method,
    which will cause timer to stop and the callback method won't be
    called.
    """

    def __init__(self, timeout, callback_method=None):
        """
        Timeout must be provided in seconds and callback_method can be either
        a function or a list of functions.
        :param timeout:
        :param callback_method:
        """
        threading.Thread.__init__(self)
        self.timeout = timeout
        self.callback_method = callback_method
        self._interrupted = False
        self.started_at = time.time()
        self.start()

    def timed_out(self):
        """
        Returns a bool indicating whether a timeout has occurred or not.
        :return:
        """
        return time.time() - self.started_at > self.timeout

    def run(self):
        """
        Starts the timer
        :return:
        """
        # Wait till interrupted or timed out
        while not self._interrupted and not self.timed_out():
            pass

        if not self._interrupted and self.callback_method:
            if isinstance(self.callback_method, list):
                for callback_method in self.callback_method:
                    callback_method()
            else:
                self.callback_method()

    def interrupt(self):
        """
        Marks timer as interrupted, meaning caller has completed its
        task before a time out has occurred.
        :return:
        """
        self._interrupted = True
