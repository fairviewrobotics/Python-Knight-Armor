from knight_emitter import KnightEmitter
import datetime, enum

#Log levels
KnightScribeLogLevel = enum.Enum("KnightScribeLogLevel", "INFO ERROR WARNING DEBUG KNIGHT_ARMOR")

#A logged message
class KnightScribeMessage:
    def __init__(self, message, logLevel):
        self.message = message
        self.logLevel = logLevel
        self.time = datetime.datetime.now()

    def __str__(self):
        return "[%s ; %s] -> %s" % (self.time, self.logLevel.name, self.message)

#KnightScribe uses messages of type KnightScribeMessage
class _KnightScribeClass(KnightEmitter):
    def log(self, message, logLevel):
        msg = KnightScribeMessage(message, logLevel)
        self.emit(msg)

KnightScribe = _KnightScribeClass()
#print out all knightScribe messages
KnightScribe.addListener(lambda msg: print(msg))
