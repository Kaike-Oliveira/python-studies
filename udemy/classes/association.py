# Association

class Writer:
    def __init__(self, name):
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, tool):
        self._tool = tool


class WriterTool:
    def __init__(self, name):
        self.name = name

    def write(self):
        return f'{self.name} it is writing!'


writer = Writer('Kaike')
pen = WriterTool('Pen')
writer.tool = pen
print(writer.tool.write())

print(20 * '=-')

computer = WriterTool('Computer')
writer.tool = computer
print(writer.tool.write())
