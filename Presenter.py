from Note import Note
import json

backup_file = 'backup.json'

def read_notebook_from_backup():

	try:
		with open(backup_file, 'r', encoding='utf-8') as file:
			my_list = json.load(file)
		return my_list
	except:
		return []


def backup_notebook(my_list):

	with open(backup_file, 'w', encoding='utf-8') as file:
		json.dump(my_list, file, ensure_ascii=False)


class Presenter:
	def __init__(self, notebook, view):
		self.notebook = notebook
		self.view = view

	def start(self):

		self.notebook.notes = read_notebook_from_backup()
		
		choice = -1
		while choice != 0:
			self.view.show_menu()
			choice = self.view.get_choice()
			if choice == 1:
				self.add_note()
			elif choice == 2:
				self.update_note()
			elif choice == 3:
				self.remove_note()
			elif choice == 4:
				self.view_notes()
			elif choice == 0:
				backup_notebook(self.notebook.notes)
				self.view.show_message("До новых встреч!")
			else:
				self.view.show_message("Неправильный выбор.")

	def add_note(self):
		label, text = self.view.get_note()
		note = Note(label, text)
		self.notebook.add(note)
		self.view.show_message("Заметка добавлена.")

	def remove_note(self):
		notes = self.notebook.get_all()
		if not notes:
			self.view.show_message("Заметок нет.")
			return
		self.view.show_notes(notes)
		index = input("\nВведите индекс заметки для удаления: ")
		if index.isnumeric():
			index = int(index)
			if 0 <= index < len(notes):
				self.notebook.remove(index)
				self.view.show_message("Заметка удалена.")
			else:
				self.view.show_message("Нет такого индекса.")
		else:
			self.view.show_message("Неправильный индекс.")

	def update_note(self):
		notes = self.notebook.get_all()
		if not notes:
			self.view.show_message("Заметок нет.")
			return
		self.view.show_notes(notes)
		index = input("\nВведите индекс заметки для редактирования: ")
		if index.isnumeric():
			index = int(index)
			if 0 <= index < len(notes):
				new_text = self.view.get_note_update()
				self.notebook.update(index, new_text)
				self.view.show_message("Заметка обновлена.")
			else:
				self.view.show_message("Нет такого индекса.")
		else:
			self.view.show_message("Неправильный индекс.")

	def view_notes(self):
		notes = self.notebook.get_all()
		if not notes:
			self.view.show_message("Заметок нет.")
			return
		self.view.show_notes(notes)
