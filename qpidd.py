#!/usr/bin/python

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

import sys
from optparse import OptionParser
import socket
from qmf.console import Session

stats = {}

parser = OptionParser(usage="usage: %prog [-h] [-p PORT] [-x HOSTNAME] QueueNames\n If multiple queue names are provided results are sum of all queues.")
parser.set_defaults(port = "5672")
parser.add_option("-p", "--port", dest="port", metavar="PORT",
                  help="Qpidd port [default: 5672]")
parser.set_defaults(host = "localhost")
parser.add_option("-x", "--host", dest="host", metavar="HOST",
                  help="Qpidd host [default: localhost]")

(opts, args) = parser.parse_args()

queueNames = []
if (args):
    for q in args:
        queueNames.append(q);
else:
    parser.error("At least one QueueName is required.")
    sys.exit(1)

sess = Session()
try:
    brokerUrl = "amqp://%s:%s" % (opts.host, opts.port)
    broker = sess.addBroker(brokerUrl)
except socket.error:
    sys.stderr.write("Failed to connect to broker at '%s'." % brokerUrl)
    sys.exit(2)

qs = [q for q in sess.getObjects(_class="queue", _package="org.apache.qpid.broker") if q.name in queueNames]

if not qs:
    sys.stderr.write("Didn't found queues matching provided QueueNames.")
    sys.exit()

if (len(qs) > 0):
    for q in qs:
        for k, v in q.getStatistics():
            stats[k] = v + stats.get(k, 0)
            
for stat, count in stats.iteritems():
    print "%s:%s" % (stat, count),

