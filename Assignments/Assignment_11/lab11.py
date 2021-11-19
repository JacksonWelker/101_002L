import time
class Clock:
    def __init__(self):
        self._hours = 12
        self._minutes = 0
        self._seconds = 0

    def getHours(self):
        return self._hours

    def getMinutes(self):
        return self._minutes

    def getSeconds(self):
        return self._seconds

    def show(self):
        print "%d:%02d:%02d" % (self._hours, self._minutes, self._seconds)

    def setTime(self, hours = 12, minutes = 34, seconds = 2):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

if __name__ == '__main__':
    import doctest
    doctest.testmod()



seconds = 0
while True:
    print(seconds)seconds += 1 time.sleep(1)
    
