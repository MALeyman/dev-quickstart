import multiprocessing as mp

def demoFunc(targetDict, targetList):
    targetDict[1] = '1'
    targetDict['2'] = 2
    targetDict[0.25] = None
    targetList.reverse()

if __name__ == '__main__':
    with mp.Manager() as manager:
        myDict = manager.dict()
        myList = manager.list(range(10))

        p = mp.Process(target=demoFunc, args=(myDict, myList))
        p.start()
        p.join()

        print(myDict)
        print(myList)