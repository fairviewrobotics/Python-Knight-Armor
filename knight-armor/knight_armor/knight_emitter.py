#a class for message emitters to extend
class KnightEmitter:
    def __init__(self):
        #listeners for messages that accept (msg). msg is a generic type
        self.msgListeners = []

    def addListener(self, listener):
        self.msgListeners.append(listener)

    def emit(self, msg):
        for listener in self.msgListeners:
            listener(msg)