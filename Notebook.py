from datetime import datetime

class Notebook:
	def __init__(self):
		self.notes = []

	def add(self, note):
		new_note = {}
		new_note['label'] = note.label
		new_note['text'] = note.text
		new_note['edit_date'] = note.edit_date
		self.notes.append(new_note)
		self.notes = self.sort()

	def update(self, index, new_text):
		self.notes[index]['text'] = new_text
		self.notes[index]['edit_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.notes = self.sort()

	def remove(self, index):
		self.notes.pop(index)
		self.notes = self.sort()

	def get_all(self):
		notes =  self.notes
		return notes
	
	def sort(self):
		notes =  self.notes
		sorted_list = sorted(notes, key=lambda x: datetime.strptime(x['edit_date'], '%Y-%m-%d %H:%M:%S'), reverse=True)
		return sorted_list
