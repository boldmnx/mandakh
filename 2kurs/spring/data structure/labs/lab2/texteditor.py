class TextEditor:
    def __init__(self):
        self.__text = ''
        self.__undo_stack = []

    def insert_text(self, text):
        self.__undo_stack.append(self.__text)
        self.__text += text

    def undo(self):
        self.__text = self.__undo_stack.pop()

    def read(self):
        return self.__text


txtedit = TextEditor()
txtedit.insert_text('hello ')
txtedit.insert_text('world ')
print(txtedit.read())
txtedit.undo()
print(txtedit.read())
