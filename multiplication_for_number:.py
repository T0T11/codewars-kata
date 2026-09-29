def multiTable(a):
    nums = range(1, 11)
    return "\n".join(f"{i} * {a} = {i * a}" for i in nums)

multiTable(5)