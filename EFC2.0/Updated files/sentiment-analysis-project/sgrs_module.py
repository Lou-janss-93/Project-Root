class SGRSModule:
    def __init__(self, name):
        self.name = name
        self.paths = []

    def add_path(self, path):
        """ Adds a path to the SGRS """
        self.paths.append(path)

    def process(self, context):
        """ Process data through the paths based on context """
        split_path = self.splitter(context)
        for path in self.paths:
            print(f"Processing path: {path.name} with context: {context}")
        # Example implementation
        if context in ["happy", "joy", "positive"]:
            return "positive"
        elif context in ["sad", "anger", "negative"]:
            return "negative"
        else:
            return "neutral"

    def splitter(self, context):
        """ Splits the context into manageable parts """
        return context.split()

class Path:
    def __init__(self, name):
        self.name = name

# Voorbeeld gebruik
if __name__ == "__main__":
    sgrs_module = SGRSModule("SGRS Example")
    sgrs_module.add_path(Path("D post"))
    sgrs_module.add_path(Path("output"))
    sgrs_module.process("DR")
    sgrs_module.process("output")