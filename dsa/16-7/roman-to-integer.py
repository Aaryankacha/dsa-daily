class Solution(object):
    def romanToInt(self, s):
        # Step 1: Roman to value mapping
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0  # this will store our result

        # Step 2: Traverse the string
        for i in range(len(s)):
            current_value = roman_map[s[i]]

            # Step 3: Check if we should subtract
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= current_value  # subtract if next symbol is bigger
            else:
                total += current_value  # otherwise just add

        return total
