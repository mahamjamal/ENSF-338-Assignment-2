def func_memo(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        result = func_memo(n-1, memo) + func_memo(n-2, memo)
        memo[n] = result
        return result


