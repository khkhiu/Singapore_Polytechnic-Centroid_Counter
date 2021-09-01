
class fanDevice:
	def __init__(self, mac):
		print("dummy_ble_init" , mac)

	def connect(self):
		print("dummy_ble_connect")
		self.speed = 0
		self.directionDelay = 0

	def writeSpeed(self, newSpeed):
		if self.speed != newSpeed:
			print("speed=", newSpeed)
			self.speed = newSpeed

	def writeDirectionDelay(self, newDirectionDelay):
		if (self.directionDelay != newDirectionDelay):
			print("directionDelay=", newDirectionDelay)
			self.directionDelay = newDirectionDelay

