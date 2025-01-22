def getListElement(lst, index):
    try:
        return lst[index]
    except IndexError:
        return 'Index out of range'
    except Exception:
        return 'An error occured'