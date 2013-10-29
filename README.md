was_xor_decode
==============

Decodes xor'ed passwords stored in the security.xml for Websphere Application Server (and related products) so you don't
have to trust websites with your passwords, which may be blocked at your workplace anyway.

Can be run in python or wsadmin.sh using jython

----

Usage: xor_decode.py <xor string>

Example: wsadmin.sh -f xor_decode.py {xor}Lz4sLCgwLTs=

or

Example: python xor_decode.py {xor}Lz4sLCgwLTs=
