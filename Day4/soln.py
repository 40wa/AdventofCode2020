import re

# Globals
required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
eye_colours = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

#p1
def count_valid_simple(bigstring):
    passports = bigstring.split('\n\n')

    validctr = 0
    for pp in passports:
        fields = {kv.split(':')[0] for kv in pp.split()}
        if required_fields.issubset(fields):
            validctr += 1

    return validctr

#p2
# All take naked values as they are in pp
class Pp_checker:
    # NB: Need to regex check byr, iyr, eyr
    # NB: Any regex can be precompiled and left as members of Pp_checker
    #     rather than recompiled each time
    def check_byr(byr):
        if len(byr) != 4:
            return False
        else:
            byr = int(byr)
            return (1920 <= byr <= 2002)

    def check_iyr(iyr):
        if len(iyr) != 4:
            return False
        else:
            return (2010 <= int(iyr) <= 2020)

    def check_eyr(eyr):
        if len(eyr) != 4:
            return False
        else:
            return (2020 <= int(eyr) <= 2030)

    def check_hgt(hgt):
        p = re.compile('^([1-9]+[0-9]*)(cm|in)$')
        res = p.match(hgt)
        if res is not None:
            if res[2] == 'cm':
                # cm check
                return (150 <= int(res[1]) <= 193)
            else:
                # in check
                return (59 <= int(res[1]) <= 76)
        else:
            return False

    def check_hcl(hcl):
        p = re.compile('^#([0-9]|[a-f]){6}$')
        return (p.match(hcl) is not None)

    def check_ecl(ecl):
        return ecl in eye_colours
        
    def check_pid(pid):
        p = re.compile('^[0-9]{9}$')
        return (p.match(pid) is not None)

#p2
def validate_strict(pp):
    # Takes a field name, applies appropriate checker
    # NB: Can be made global
    field_checker = {
        'byr': Pp_checker.check_byr,
        'iyr': Pp_checker.check_iyr,
        'eyr': Pp_checker.check_eyr,
        'hgt': Pp_checker.check_hgt,
        'hcl': Pp_checker.check_hcl,
        'ecl': Pp_checker.check_ecl,
        'pid': Pp_checker.check_pid,
    }

    # Check that all required fields are present
    if not required_fields.issubset(pp.keys()):
        # Fail fast
        return False
    else:
        # NB: Can replace this whole clause with a generator
        # ie: return all((field_checker[field](pp[field]) for field in required_fields))
        for field in required_fields:
            v = field_checker[field](pp[field])
            print(field, pp[field], v)
            if not v:
                return False

    return True
            

#p2
def count_valid_strict(bigstring):
    passports = bigstring.split('\n\n')

    validctr = 0
    for pp in passports:
        data = {kv.split(':')[0]:kv.split(':')[1] for kv in pp.split()}
        if validate_strict(data):
            validctr += 1

    return validctr


def main():

    # Part One
    print("Part One")

    # Get data
    largestring = open('data').read()

    validctr = count_valid_simple(largestring)
    print(validctr)

    # Part Two
    print("Part Two")
    validstrictctr = count_valid_strict(largestring)
    print(validstrictctr)

if __name__=="__main__":
    main()
