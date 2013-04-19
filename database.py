class database:

	webBase = {}

	def __init__(self):
		return

	def addHomeLink(homeLink):

		if homeLink.getURL not in webBase:
			webBase[homeLink.getURL] = homeLink
			return true

		return false


	def getHomeLink(homeURL):

		if homeURL in webBase:
			return webBase[homeURL]

		return None

	def getDatabase():

		return webBase