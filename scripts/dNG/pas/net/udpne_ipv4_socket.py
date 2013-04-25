# -*- coding: utf-8 -*-
##j## BOF

"""
dNG.pas.net.udpne_ipv4_socket
"""
"""n// NOTE
----------------------------------------------------------------------------
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
http://www.direct-netware.de/redirect.py?pas;udpne

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.
----------------------------------------------------------------------------
http://www.direct-netware.de/redirect.py?licenses;mpl2
----------------------------------------------------------------------------
#echo(pasUdpNEVersion)#
#echo(__FILEPATH__)#
----------------------------------------------------------------------------
NOTE_END //n"""

import socket

class direct_udpne_ipv4_socket(socket.socket):
#
	"""
The UDP Non-Exclusive socket allows multiple applications to receive e.g.
multicast packets over IPV4.

:author:     direct Netware Group
:copyright:  (C) direct Netware Group - All rights reserved
:package:    pas
:subpackage: udpne
:since:      v0.1.00
:license:    http://www.direct-netware.de/redirect.py?licenses;mpl2
             Mozilla Public License, v. 2.0
	"""

	def __init__(self, listener_data = None):
	#
		socket.socket.__init__(self, socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		self.setblocking(0)

		self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		if (hasattr(socket, "SO_REUSEPORT")): self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

		if (listener_data != None):
		#
			if (type(listener_data) == int): self.bind(( socket.INADDR_BROADCAST, listener_data ))
			else: self.bind(listener_data)
		#
	#
#

##j## EOF