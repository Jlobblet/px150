def compare_two(x,y):
    try:
        return int((x-y)/abs(x-y))
    except ZeroDivisionError:
        return 0
    except:
        pass