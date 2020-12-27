# Dynamic Programming

''' ###### Fibonacci ######'''

# Brute-Force


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Memoized
def fib2(n):
    memo = {0: 0, 1: 1}

    def hlperFunction(n):
        if n not in memo:
            memo[n] = hlperFunction(n - 1) + hlperFunction(n - 2)
        return memo[n]

    return hlperFunction(n)


# Tabulation
def fib3(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(n - 1):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    table[-1] += table[-2]
    return table[-1]


''' ######  Grid Traveller ######'''

# Brute-Force


def grid_traveller(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)


# Memoized
def grid_traveller2(m, n):
    memo = {"1,1": 1}

    def hlperFunction(m, n):
        if m == 0 or n == 0:
            return 0
        key = f"{m},{n}"
        if key in memo:
            return memo[key]
        key = f"{n},{m}"
        if key in memo:
            return memo[key]
        memo[key] = hlperFunction(m - 1, n) + hlperFunction(m, n - 1)
        return memo[key]

    return hlperFunction(m, n)


# Tabulation
def grid_traveller3(m, n):
    table = [[0] * (n + 1) for _ in range(m + 1)]
    table[1][1] = 1
    for i in range(1, m):
        for j in range(1, n):
            table[i][j + 1] += table[i][j]
            table[i + 1][j] += table[i][j]
    # right-most column
    for i in range(1, m):
        table[i + 1][-1] += table[i][-1]
    # bottom row
    for j in range(1, n):
        table[-1][j + 1] += table[-1][j]
    return table[m][n]


''' ######  Can Sum ######'''

# Brute-Force


def can_sum(target_sum, numbers):
    if target_sum == 0:
        return True
    for num in numbers:
        remainder = target_sum - num
        if remainder >= 0:
            if can_sum(remainder, numbers):
                return True
    return False


# Memoized
def can_sum2(target_sum, numbers):
    memo = {}

    def hlperFunction(target_sum, numbers):
        if target_sum == 0:
            return True
        if target_sum in memo:
            return memo[target_sum]
        for num in numbers:
            remainder = target_sum - num
            if remainder >= 0:
                if hlperFunction(remainder, numbers):
                    memo[target_sum] = True
                    return True
        memo[target_sum] = False
        return memo[target_sum]

    return hlperFunction(target_sum, numbers)


# Tabulation
def can_sum3(targert_sum, numbers):
    table = [False] * (targert_sum + 1)
    table[0] = True
    for i in range(targert_sum):
        if table[i]:
            numbers = [num for num in numbers if i + num <= targert_sum]
            for num in numbers:
                table[i + num] = True
    return table[-1]


'''######  How Sum ######'''

# Brute-Force


def how_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    for num in numbers:
        remainder = target_sum - num
        if remainder >= 0:
            combination = how_sum(remainder, numbers)
            if combination is not None:
                combination = combination + [num]
                return combination
    return None


# Memoized
def how_sum2(target_sum, numbers):
    memo = {}

    def hlperFunction(target_sum, numbers):
        if target_sum == 0:
            return []
        if target_sum in memo:
            return memo[target_sum]
        for num in numbers:
            remainder = target_sum - num
            if remainder >= 0:
                combination = hlperFunction(remainder, numbers)
                if combination is not None:
                    memo[target_sum] = combination + [num]
                    return memo[target_sum]
        memo[target_sum] = None
        return memo[target_sum]

    return hlperFunction(target_sum, numbers)


# Tabulation
def how_sum3(targert_sum, numbers):
    table = [None] * (targert_sum + 1)
    table[0] = []
    for i in range(targert_sum):
        if table[i] is not None:
            numbers = [num for num in numbers if i + num <= targert_sum]
            for num in numbers:
                table[i + num] = table[i] + [num]
    return table[-1]


'''######  Best Sum ######'''

# Brute-Force


def best_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        if remainder >= 0:
            combination = best_sum(remainder, numbers)
            if combination is not None:
                combination = combination + [num]
                if shortest_combination is None or len(combination) < len(
                    shortest_combination
                ):
                    shortest_combination = combination
    return shortest_combination


# Memoized
def best_sum2(target_sum, numbers):
    memo = {}

    def hlperFunction(target_sum, numbers):
        if target_sum == 0:
            return []
        if target_sum in memo:
            return memo[target_sum]
        shortest_combination = None
        for num in numbers:
            remainder = target_sum - num
            if remainder >= 0:
                combination = hlperFunction(remainder, numbers)
                if combination is not None:
                    combination = combination + [num]
                    if shortest_combination is None or len(combination) < len(
                        shortest_combination
                    ):
                        shortest_combination = combination
        memo[target_sum] = shortest_combination
        return memo[target_sum]

    return hlperFunction(target_sum, numbers)


# Tabulation
def best_sum3(targert_sum, numbers):
    table = [None] * (targert_sum + 1)
    table[0] = []
    for i in range(targert_sum):
        if table[i] is not None:
            numbers = [num for num in numbers if i + num <= targert_sum]
            for num in numbers:
                if table[i + num] is None or len(table[i]) < len(table[i + num]):
                    table[i + num] = table[i] + [num]
    return table[-1]


'''######  Can Construct ######'''

# Brute-Force


def can_construct(target, word_bank):
    if target == "":
        return True
    for word in word_bank:
        if len(target) >= len(word) and target[: len(word)] == word:
            remainder = target[len(word):]
            if can_construct(remainder, word_bank):
                return True
    return False


# Memoized
def can_construct2(target, word_bank):
    memo = {}

    def hlperFunction(target, word_bank):
        if target == "":
            return True
        if target in memo:
            return memo[target]
        for word in word_bank:
            if len(target) >= len(word) and target[: len(word)] == word:
                remainder = target[len(word):]
                if hlperFunction(remainder, word_bank):
                    memo[target] = True
                    return memo[target]
        memo[target] = False
        return False

    return hlperFunction(target, word_bank)


# Tabulation
def can_construct3(target, word_bank):
    table = [False] * (len(target) + 1)
    table[0] = True
    for i in range(len(target)):
        if table[i]:
            for word in word_bank:
                if target[i: i + len(word)] == word:
                    table[i + len(word)] = True
    return table[-1]


'''######  Count Construct ######'''

# Brute-Force


def count_construct(target, word_bank):
    if target == "":
        return 1
    totalCount = 0
    for word in word_bank:
        if len(target) >= len(word) and target[: len(word)] == word:
            remainder = target[len(word):]
            totalCount += count_construct(remainder, word_bank)
    return totalCount


# Memoized
def count_construct2(target, word_bank):
    memo = {}

    def hlperFunction(target, word_bank):
        if target == "":
            return 1
        if target in memo:
            return memo[target]
        totalCount = 0
        for word in word_bank:
            if len(target) >= len(word) and target[: len(word)] == word:
                remainder = target[len(word):]
                totalCount += hlperFunction(remainder, word_bank)
        memo[target] = totalCount
        return totalCount

    return hlperFunction(target, word_bank)


# Tabulation
def count_construct3(target, word_bank):
    table = [0] * (len(target) + 1)
    table[0] = 1
    for i in range(len(target)):
        if table[i]:
            for word in word_bank:
                if target[i: i + len(word)] == word:
                    table[i + len(word)] += table[i]
    return table[-1]


'''######  All Construct ######'''

# Brute-Force


def all_construct(target, word_bank):
    if target == "":
        return [[]]
    result = []
    for word in word_bank:
        if len(target) >= len(word) and target[: len(word)] == word:
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [way + [word] for way in suffix_ways]
            if target_ways:
                result.extend(target_ways)
    return result


# Memoized
def all_construct2(target, word_bank):
    memo = {}

    def hlperFunction(target, word_bank):
        if target == "":
            return [[]]
        if target in memo:
            return memo[target]
        result = []
        for word in word_bank:
            if len(target) >= len(word) and target[: len(word)] == word:
                suffix = target[len(word):]
                suffix_ways = hlperFunction(suffix, word_bank)
                target_ways = [way + [word] for way in suffix_ways]
                if target_ways:
                    result.extend(target_ways)
        memo[target] = result
        return result

    return hlperFunction(target, word_bank)


# Tabulation
def all_construct3(target, word_bank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]
    for i in range(len(target)):
        for word in word_bank:
            if target[i: i + len(word)] == word:
                new_combinations = [combination + [word]
                                    for combination in table[i]]
                table[i + len(word)].extend(new_combinations)
    return table[-1]

# print(fib())
# print(fib2())
# print(fib3())

# print(grid_traveller())
# print(grid_traveller2())
# print(grid_traveller3())

# print(can_sum())
# print(can_sum()2)
# print(can_sum()3)

# print(how_sum())
# print(how_sum2())
# print(how_sum3())

# print(best_sum())
# print(best_sum()2)
# print(best_sum()3)

# print(can_construct)
# print(can_construct2)
# print(can_construct3)

# print(count_construct)
# print(count_construct2)
# print(count_construct3)

# print(all_construct)
# print(all_construct2)
# print(all_construct3)
