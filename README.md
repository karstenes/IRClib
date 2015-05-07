#IRClib
###Python IRC libraries
This is a set of libraries to be used for easy creation of IRC bots and clients.
##Usage
To use, first import it.

    import IRClib
    
Next, create a new connection.

	irc = IRClib.IRC("HOST", PORT, "Nick", "Real name", "Identity")
Now we need to create a loop for reading new messages and pinging the server

	while True:
		irc.ping()
		data_read = irc.read("nick")
**irc.read("nick")** takes two inputs: nick and hostname. Nick will give the nickname of the latest message, and hostname will give the hostname

**data_read** will be an array with item 0 being the nick/hostname, item 1 being the channel it was said on (if it was a PM it will be the nick of the sender), and item 2 being the message.

We can also send messages and actions.

	irc.send("#channel", "Foo")
will send Foo to the channel #channel. If you replace #channel with a nick, it will message that user.

We can also send actions.

	irc.action("#channel", "foos")
will send ***nick foos**

To close the connection, execute

	irc.close()

##Licence
    Kbot IRC bot
Copyright (C) 2015  Karsten Schnier

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.

		