
import BLE_GATT
fan_speed_id = 'cc4b8741-59e8-47d3-a23b-5890fcc50a0b'
direction_delay_id = 'd49165ac-1bd1-49f8-896f-52aa73f95785'

class fanDevice:

	def __init__(self, mac):
		print("ble_init" , mac)
		self.mac = mac;
		self.esp = BLE_GATT.Central(mac);

	def connect(self):
		print("ble_connect")
		self.esp.connect()
		self.speed = self.esp.char_read(fan_speed_id)
		self.directionDelay = self.esp.char_read(direction_delay_id)

	def writeSpeed(self, newSpeed):
		if self.speed != newSpeed:
			self.esp.char_write(fan_speed_id, [newSpeed])
			self.speed = newSpeed

	def writeDirectionDelay(self, newDirectionDelay):
		if (self.directionDelay != newDirectionDelay):
			self.esp.char_write(direction_delay_id, [newDirectionDelay])
			self.directionDelay = newDirectionDelay
