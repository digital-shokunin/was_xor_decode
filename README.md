was_xor_decode
==============

Decodes xor'ed passwords stored in the security.xml for Websphere Application Server (and related products)

Can be run in python or wsadmin.sh using jython

Usage: decode_xor.py <xor'ed string>

Example: wsadmin.sh -f decode_xor.py {xor}Lz4sLCgwLTs=

or

Example: python decode_xor.py {xor}Lz4sLCgwLTs=
