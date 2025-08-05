class Car(object):
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model

    def __str__(self):
        return f"Марка {self.mark} Модель {self.model}"

    def __eq__(self, other):
        return True if ((self.mark == other.mark.title()) and (self.model == other.model.title())) else False

    def __ne__(self, other):
        return True if ((self.mark == other.mark) or (self.model == other.model)) else False