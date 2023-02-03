def timer(func):
    def inner(*args, **kwargs):
        from datetime import datetime
        start_time = datetime.now()
        res = func(*args, **kwargs)
        last = datetime.now()
        print(last - start_time)
        return res

    return inner


memo = {1: 1, 2: 1, 3: 1}


@timer
def tribonacci(n):
    result = memo.get(n)
    if result is None:
        result = tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)
        memo[n] = result
    return result


print(tribonacci(7))
