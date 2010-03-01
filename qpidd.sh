#!/bin/bash

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
# under the License.
#

# This is Qpid Python client location
QPID_PYTHON=.

function usage {
    echo "Usage: $0 [[HOST] PORT] QUEUENAME";
    exit 1;
}

script=qpidd.py
python=`which python`

host="localhost"
port=5672

if [ -n "$3" ]; then
    host=$1
    port=$2
    queue=$3
elif [ -n "$2" ]; then
    port=$1
    queue=$2
elif [ -n "$1" ]; then
    queue=$1
else
    usage
fi

PYTHONPATH=$QPID_PYTHON:. $python $script -p $port -x $host $queue
exit $?