# -*- coding: utf-8 -*-
##j## BOF

"""
de.direct_netware.classes.pas-udpne_socket

@internal   We are using epydoc (JavaDoc style) to automate the
            documentation process for creating the Developer's Manual.
            Use the following line to ensure 76 character sizes:
----------------------------------------------------------------------------
@author     direct Netware Group
@copyright  (C) direct Netware Group - All rights reserved
@package    pas_complete
@subpackage server
@since      v0.1.00
@license    http://www.direct-netware.de/redirect.php?licenses;mpl2
            Mozilla Public License, v. 2.0
"""
"""n// NOTE
----------------------------------------------------------------------------
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
http://www.direct-netware.de/redirect.php?pas

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.
----------------------------------------------------------------------------
http://www.direct-netware.de/redirect.php?licenses;mpl2
----------------------------------------------------------------------------
#echo(pasCompleteServerVersion)#
pas/#echo(__FILEPATH__)#
----------------------------------------------------------------------------
NOTE_END //n"""

from socket import socket,AF_INET,INADDR_BROADCAST,IPPROTO_UDP,SO_REUSEADDR,SOCK_DGRAM,SOL_SOCKET

try: from socket import SO_REUSEPORT
except ImportError: SO_REUSEPORT = None

class direct_udpne_socket (socket):
#
	"""
The UDP Non-Exclusive socket allows multiple applications to receive e.g. multi
cast packets.

@author     direct Netware Group
@copyright  (C) direct Netware Group - All rights reserved
@package    pas_complete
@subpackage udpne
@since      v0.1.00
@license    http://www.direct-netware.de/redirect.php?licenses;mpl2
            Mozilla Public License, v. 2.0
	"""

	def __init__ (self,listener_data = None):
	#
		socket.__init__ (self,AF_INET,SOCK_DGRAM,IPPROTO_UDP)

		self.setsockopt (SOL_SOCKET,SO_REUSEADDR,1)
		if (SO_REUSEPORT != None): self.setsockopt (SOL_SOCKET,SO_REUSEPORT,1)

		if (listener_data != None):
		#
			if (type (listener_data) == int): self.bind (( INADDR_BROADCAST,listener_data ))
			else: self.bind (listener_data)
		#
	#
#

##j## EOF