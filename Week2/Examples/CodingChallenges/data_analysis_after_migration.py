#https://www.codewars.com/kata/5bc5cfc9d38567e29600019d


def check_dates(data):
    """
    Analyze date records to determine if they're correct, recoverable, or uncertain.
    
    Args:
        data: List of [start_date, end_date] pairs in yyyy-mm-dd format
    
    Returns:
        [correct_count, recoverable_count, uncertain_count]
    """
    correct = 0
    recoverable = 0
    uncertain = 0
    
    for record in data:
        start_date, end_date = record
        
        # Get all valid interpretations for each date
        start_variants = get_date_variants(start_date)
        end_variants = get_date_variants(end_date)
        
        # Find all valid combinations where start <= end
        valid_combinations = []
        for start in start_variants:
            for end in end_variants:
                if start <= end:
                    valid_combinations.append((start, end))
        
        # Classify based on valid combinations
        if len(valid_combinations) == 0:
            # No valid interpretation exists
            uncertain += 1
        elif len(valid_combinations) == 1:
            # Exactly one valid interpretation
            if valid_combinations[0] == (start_date, end_date):
                # Current form is the only valid one
                correct += 1
            else:
                # Current form is wrong, but can be recovered
                recoverable += 1
        else:
            # Multiple valid interpretations exist
            uncertain += 1
    
    return [correct, recoverable, uncertain]


def get_date_variants(date_str):
    """
    Get all possible valid date interpretations (original and day/month swapped).
    
    Args:
        date_str: Date string in yyyy-mm-dd format
    
    Returns:
        List of valid date strings
    """
    year, month, day = date_str.split('-')
    
    variants = []
    
    # Original interpretation (yyyy-mm-dd)
    if is_valid_date(year, month, day):
        variants.append(date_str)
    
    # Swapped interpretation (yyyy-dd-mm)
    if month != day:  # Only swap if different
        swapped = f"{year}-{day}-{month}"
        if is_valid_date(year, day, month):
            variants.append(swapped)
    
    return variants


def is_valid_date(year, month, day):
    """
    Check if year-month-day forms a valid date.
    
    Args:
        year, month, day: String components of a date
    
    Returns:
        Boolean indicating validity
    """
    try:
        y, m, d = int(year), int(month), int(day)
        
        # Check basic ranges
        if m < 1 or m > 12 or d < 1 or d > 31:
            return False
        
        # Days in each month
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Check for leap year
        if is_leap_year(y):
            days_in_month[1] = 29
        
        # Check if day is valid for the month
        if d > days_in_month[m - 1]:
            return False
        
        return True
    except (ValueError, IndexError):
        return False


def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

records = [
    ["2015-04-04", "2015-05-13"],  # correct
    ["2013-06-18", "2013-08-05"],  # correct
    ["2001-02-07", "2001-03-01"],  # correct
    ["2011-10-08", "2011-08-14"],  # recoverable
    ["2009-08-21", "2009-04-12"],  # recoverable
    ["1996-01-24", "1996-03-09"],  # uncertain
    ["2000-10-09", "2000-11-20"],  # uncertain
    ["2002-02-07", "2002-12-10"]]  # uncertain
    
print(check_dates(records))
#[3, 2, 3])