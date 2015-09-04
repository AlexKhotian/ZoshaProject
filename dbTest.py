__author__ = 'Alex'

import BoardDataBases
from BoardDataBases import BoardDataBase

if __name__ == '__main__':
    dbHandle = BoardDataBase.BoardDatabase()
    dbHandle.createDataBase()
    dbHandle.insertDataIntoLoginDatabase("user1", "12345")
    dbHandle.getUserDataFromDB("user1")
