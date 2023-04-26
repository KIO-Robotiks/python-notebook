class View:
	def show_menu(self):
		print("\nГлавное меню:")
		print("1. Добавить заметку.")
		print("2. Редактировать заметку.")
		print("3. Удалить заметку.")
		print("4. Посмотреть заметки.")
		print("0. Выход.")

	def get_choice(self):
		choice = input("\nВыберите пункт меню: ")
		if choice.isnumeric():
			return int(choice)

	def get_note(self):
		label = input("Заголовок заметки: ")
		text = input("Тело заметки: ")
		return label, text
	
	def get_note_update(self):
		text = input("Тело заметки: ")
		return text

	def show_notes(self, notes):
		print("\n               Все заметки:")
		print('------------------------------------------------------')

		for i in range(len(notes)):
			print(f"{i}. {notes[i]['label']}:")
			print(f"{notes[i]['text']}")
			print(f"(Время последнего редактирования: {notes[i]['edit_date']})")
			print('------------------------------------------------------')

	def show_message(self, message):
		print(message)
