# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n < 1:
        return " "

    result = ""
    i = 0

    while i < n:
        if i == 0 or i == n - 1 :
            result += "*" * n
        else:
            if n > 1:
              result += "*" + " " * (n - 2) + "*" 
            else:  "*"
        
        result += "\n"
        i += 1

    return result.strip()

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    i = 1
    
    while i <= n:
        j = 1
        while j <= i:
            result += str(j)
            j += 1
        result += "\n" 
        i += 1
        
    return result.strip()  

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0  
    x = 1     

    while x <= n:
        total += x
        x += 1
        
    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range(1, n + 1):
        result += " " * (n - i) 
        result += "*" * (2 * i - 1) + "\n"
        
    return result.rstrip()