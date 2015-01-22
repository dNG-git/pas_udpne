# -*- coding: utf-8 -*-
##j## BOF

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

class UdpNeIpv6Socket(socket.socket):
#
	"""
The UDP Non-Exclusive socket allows multiple applications to receive e.g.
multicast packets over IPV6.

:author:     direct Netware Group
:copyright:  (C) direct Netware Group - All rights reserved
:package:    pas
:subpackage: udpne
:since:      v0.1.00
:license:    https://www.direct-netware.de/redirect?licenses;mpl2
             Mozilla Public License, v. 2.0
	"""

	def __init__(self, listener_data = None):
	#
		"""
Constructor __init__(UdpNeIpv6Socket)

:since: v0.1.00
		"""

		# pylint: disable=super-init-not-called
		# pylint 1.1.0 fails to identify socket.socket.__init__() as parent constructor call

		socket.socket.__init__(self, socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		self.setblocking(0)

		self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		if (hasattr(socket, "SO_REUSEPORT")): self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

		if (listener_data is not None):
		#
			if (type(listener_data) is int): self.bind(( socket.INADDR_BROADCAST, listener_data ))
			else: self.bind(listener_data)
		#
	#
#

##j## EOF