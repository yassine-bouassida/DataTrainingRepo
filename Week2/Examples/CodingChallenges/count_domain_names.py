#https://www.codewars.com/kata/595120ac5afb2e5c1d000001

def count_domains(domains: str, min_hits: int = 0) -> str:
    from collections import defaultdict

    def normalize(domain: str) -> str:
        domain = domain.lstrip("*.")   # remove leading "*."
        parts = domain.split(".")

        # Handle .co.xx and .com.xx
        if len(parts) >= 3 and parts[-2] in ("co", "com"):
            return ".".join(parts[-3:])
        else:
            return ".".join(parts[-2:])

    totals = defaultdict(int)

    for line in domains.splitlines():
        if not line.strip():
            continue
        domain, hits = line.split()
        totals[normalize(domain)] += int(hits)

    # Filter and sort
    results = [
        (domain, hits)
        for domain, hits in totals.items()
        if hits >= min_hits
    ]

    results.sort(key=lambda x: (-x[1], x[0]))

    return "\n".join(f"{domain} ({hits})" for domain, hits in results)