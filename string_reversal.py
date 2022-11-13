# Recursion-Repeating.
def string_reverse(str):
    if len(str)==0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]


str="gameoflife"
print(string_reverse(str))


#str[start:stop:step]

trial="reversal"
new_trial=trial[::-1]
print(new_trial)