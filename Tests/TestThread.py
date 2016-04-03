__author__ = 'Alex'

from BoardMultithreading import BoardThreadPool

def printTest(t):
    print(t)

if __name__ == '__main__':
    tPool = BoardThreadPool.BoardThreadPoolImpl()
    print(tPool.currentActiveThreads())
    index = tPool.createThread(printTest, "e")
    print("aaaaaaaaaaaa")
    print(index)
    tPool.runThread(index)
    tPool.joinThread(index)
