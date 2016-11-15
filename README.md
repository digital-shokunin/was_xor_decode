was_xor_decode
==============

Decodes xor'ed passwords stored in the security.xml for Websphere Application Server (and related products) so you don't
have to trust websites with your passwords, which may be blocked at your workplace anyway.

Can be run in python or wsadmin.sh using jython

----
###Usage:

    xor_decode.py <xor string>

    Example: wsadmin.sh -lang jython -f xor_decode.py {xor}Lz4sLCgwLTs=

    or

    Example: python xor_decode.py {xor}Lz4sLCgwLTs=


###Command to easily find passwords(on Unix/Linux):

    ps -eaf |grep java |grep com.ibm.ws | awk '{for(i=1;i<=NF;i++){if ($i ~ /user\.install\.root/){print $i}}}' | awk -F'=' '{print $2}' |xargs -I % find % -name "security.xml" -exec grep {xor} '{}' \; | awk '{for(i=1;i<=NF;i++){if ($i ~ /password/){print $i}}}'
