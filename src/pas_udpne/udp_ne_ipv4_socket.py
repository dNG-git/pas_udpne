# -*- coding: utf-8 -*-

"""
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
https://www.direct-netware.de/redirect?pas;udpne

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.
----------------------------------------------------------------------------
https://www.direct-netware.de/redirect?licenses;mpl2
----------------------------------------------------------------------------
#echo(pasUdpNEVersion)#
#echo(__FILEPATH__)#
"""

import socket

class UdpNeIpv4Socket(socket.socket):
    """
The UDP Non-Exclusive socket allows multiple applications to receive e.g.
multicast packets over IPV4.

:author:     direct Netware Group et al.
:copyright:  (C) direct Netware Group - All rights reserved
:package:    pas
:subpackage: udpne
:since:      v1.0.0
:license:    https://www.direct-netware.de/redirect?licenses;mpl2
             Mozilla Public License, v. 2.0
    """

    __slots__ = [ ]
    """
python.org: __slots__ reserves space for the declared variables and prevents
the automatic creation of __dict__ and __weakref__ for each instance.
    """

    def __init__(self, listener_data = None):
        """
Constructor __init__(UdpNeIpv4Socket)

:since: v1.0.0
        """

        socket.socket.__init__(self, socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.setblocking(0)

        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if (hasattr(socket, "SO_BROADCAST")): self.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        if (hasattr(socket, "SO_REUSEPORT")): self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        if (listener_data is not None):
            if (type(listener_data) is int): self.bind(( "<broadcast>", listener_data ))
            else: self.bind(listener_data)
        #
    #
#
