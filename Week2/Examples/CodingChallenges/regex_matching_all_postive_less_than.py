#https://www.codewars.com/kata/615da209cf564e0032b3ecc6

def regex_less_than(n: int) -> str:
    # No positive integers less than 1
    if n <= 1:
        return r'^(?!)$'

    s = str(n)
    L = len(s)
    parts = []

    # Numbers with fewer digits (must start 1–9)
    if L > 1:
        parts.append(r'[1-9]\d{0,%d}' % (L - 2))

    # Same-length numbers smaller than n
    for i, ch in enumerate(s):
        digit = int(ch)
        if digit == 0:
            continue

        rest = r'\d' * (L - i - 1)

        if i == 0:
            # First digit cannot be 0
            if digit - 1 >= 1:
                parts.append(f'[1-{digit-1}]' + rest)
        else:
            if digit - 1 >= 0:
                parts.append(s[:i] + f'[0-{digit-1}]' + rest)

    return r'^(?:' + '|'.join(parts) + r')$'