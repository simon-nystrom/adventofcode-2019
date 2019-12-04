from utils.printing import printed

def check_password(s):
    has_adjacent = False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]: 
            has_adjacent = True
        if int(s[i]) > int(s[i + 1]):
            return False
    return has_adjacent

def check_password_2(s):
    has_two_adjacent = False
    i = 0
    while i < len(s) - 1:
        if int(s[i]) > int(s[i + 1]):
            return False
        if s[i] == s[i + 1]:
            j = i + 1
            num_adjacent = 2
            while j < len(s) - 1 and s[j] == s[j + 1]:
                if int(s[j]) > int(s[j + 1]):
                    return False
                j += 1
                num_adjacent += 1
            i += j - i
            if num_adjacent == 2:
                has_two_adjacent = True
        else:
            i += 1
    return has_two_adjacent

@printed
def part1(lower_bound, upper_bound):
    num_ok_passwords = 0
    for i in range(lower_bound, upper_bound):
        if check_password(str(i)):
            num_ok_passwords += 1
    return num_ok_passwords

@printed
def part2(lower_bound, upper_bound):
    num_ok_passwords = 0
    for i in range(lower_bound, upper_bound):
        if check_password_2(str(i)):
            num_ok_passwords += 1
    return num_ok_passwords

part1(206938, 679128)
part2(206938, 679128)
