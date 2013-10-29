was_xor_decode
==============

Decodes xor'ed passwords stored in the security.xml for Websphere Application Server (and related products)

Can be run in python or wsadmin.sh using jython

----

Usage: xor_decode.py <xor string>

Example: wsadmin.sh -f xor_decode.py {xor}Lz4sLCgwLTs=

or

Example: python xor_decode.py {xor}Lz4sLCgwLTs=
