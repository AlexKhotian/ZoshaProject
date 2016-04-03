__author__ = 'Alex'

import threading


class BoardThreadPoolImpl(object):
    def __init__(self):
        pass
    m_threadPool = []
    m_threadCounter = 0

    def currentActiveThreads(self):
        return threading.activeCount()

    def createThread(self, function, args):
        self.m_threadPool.insert(self.m_threadCounter,
                                 threading.Thread(None, function, self.m_threadCounter, args))
        self.m_threadCounter += 1
        return self.m_threadCounter - 1

    def runThread(self, threadid):
        self.m_threadPool[threadid].start()

    def joinThread(self, threadid, timeout=None):
        self.m_threadPool[threadid].join(timeout)
        self.m_threadPool.pop(threadid)



