def isStepenBroja2(n):
    if n / 2 == 1:
        return True
    else:
        return n % 2 == 0 and isStepenBroja2(n/2)