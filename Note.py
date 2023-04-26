from datetime import datetime


class Note:
	def __init__(self, label, text):
		self.label = label
		self.text = text
		self.edit_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
