def is_triangle(a,b,c):
    if max(a,max(b,c)) <= min(a,min(b,c)) + max(a,min(b,c)):
        return True
    else:
        return False