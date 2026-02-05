#https://www.codewars.com/kata/64607242d3560e0043c3de25

#Helper: count palindromes ≤ n
def count_palindromes_upto(n: int) -> int:
    if n < 0:
        return 0

    s = str(n)
    length = len(s)
    count = 0

    # Count palindromes with fewer digits
    for l in range(1, length):
        half = (l + 1) // 2
        count += 9 * (10 ** (half - 1))

    # Count palindromes of same length
    half_len = (length + 1) // 2
    prefix = int(s[:half_len])

    # Build palindrome from prefix
    if length % 2 == 0:
        pal = int(str(prefix) + str(prefix)[::-1])
    else:
        pal = int(str(prefix) + str(prefix)[-2::-1])

    count += prefix - (10 ** (half_len - 1))
    if pal <= n:
        count += 1

    return count

#final solution
def palindromes_between(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    return count_palindromes_upto(b) - count_palindromes_upto(a - 1)

print(palindromes_between(32,93))