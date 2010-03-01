=======
Install
=======
:Authors: Hubert Iwaniuk <h.iwaniuk@sourcesense.com>
:Date: 2010-03-01

Installation Instructions

------------
Requirements
------------

In order to install *cacti-qpid* you'll need to have following on your system:

1. python

2. qpid-python

qpid-python
===========

You'll get it from Qpid_. Extract it to location that is accessible by cacti process,
usually it is *apache*.

------------
Installation
------------

In package you'll find **qpidd.sh** that needs to be customized.

Please find following line in it:
  # This is Qpid Python client location
  
  QPID_PYTHON=.

And modify it to reference *qpid-python* installation path.

Now you should be able to test it by:
  $ ./qpidd.sh queue_name

Errors
======

If you see:

1. ImportError: No module named qmf.console
It means you haven't provided valid *QPID_PYTHON* location.


.. _Qpid: http://www.apache.org/dist/qpid/0.5/qpid-python-0.5.tar.gz
