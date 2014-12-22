#
# This module is imported and sets common settings
#

import coloredlogs, logging
coloredlogs.install()
logging.basicConfig(level=logging.INFO)


from kazoo.client import KazooClient
from kazoo.client import KazooState

#
# This is the main znode that we'll be working with in this demo
#
key = "/zkdemo"


#
# Connect to Zookeeper and return the handle.
#
def connect():
	retval = KazooClient(hosts='127.0.0.1:2181')

	def my_listener(state):
		if state == KazooState.LOST:
			# Register somewhere that the session was lost
			logging.warn("Lost connection to Zookeeper")

		elif state == KazooState.SUSPENDED:
			# Handle being disconnected from Zookeeper
			logging.warn("Zookeeper connection suspended")

		elif state == KazooState.CONNECTED:
			pass

		else:
			# Handle being connected/reconnected to Zookeeper
			logging.info("Other state: %s" % state)

	retval.add_listener(my_listener)
	retval.start()

	return(retval)



