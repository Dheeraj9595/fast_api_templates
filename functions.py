def number_to_words(num):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion", "trillion"]

    def helper(num, level):
        if num == 0:
            return ""
        elif num < 10:
            return units[num] + " "
        elif num < 20:
            return teens[num - 10] + " "
        elif num < 100:
            return tens[num // 10] + " " + helper(num % 10, level + 1)
        else:
            return units[num // 100] + " hundred " + helper(num % 100, level + 1)

    if num == 0:
        return "zero"

    result = ""
    level = 0
    while num > 0:
        if num % 1000 != 0:
            result = helper(num % 1000, level) + thousands[level] + " " + result
        num //= 1000
        level += 1

    return result.strip()


# Example usage
# print(number_to_words(6004))  # Output: "one hundred"
import random

def luck_game(n):
    random_number = random.randint(0,9)
    
    n = int(n)
    
    if n == random_number:
        return "Wowww you won....!!!!",random_number
    else:
        return  "sorry..... try again...",random_number


if __name__ == "__main__":
    num = 100
    words = number_to_words(num)
    print(f"The words for the number {num} are: {words}")
