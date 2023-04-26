from Notebook import Notebook
from View import View
from Presenter import Presenter

if __name__ == "__main__":
	model = Notebook()
	view = View()
	presenter = Presenter(model, view)
	presenter.start()
	