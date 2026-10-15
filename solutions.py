#Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    frequency={}
    for i in sentence.split():
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    return frequency

# Q2. Find the Frequency of Each Character in a Word
def char_frequency(word):
    frequency={}
    for i in word:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    return frequency

# Q3. Find the First Non-Repeating Character in a Word

def non_repeating_char(word):
    frequency = char_frequency(word)
    for i in word:
        if frequency[i] == 1:
            return i
    return None

# Q4. Check Whether Two Strings Are Anagrams
def are_anagram(word1,word2):
    if sorted(word1)==sorted(word2):
        return True
    else:
        return False

# Q5. Find the First Repeating Character in a String
def rep_char(word):
    frequency={}
    for i in word:
        if i in frequency:
            return i
        else:
            frequency[i]=1
    return None

# Q6. Move All Zeros to the End of a List
def move_zeros(numbers):
    result = []
    for i in numbers:
        if i != 0:
            result.append(i)
    for i in numbers:
        if i == 0:
            result.append(i)
    return result

# Q7. Find the Second Highest Distinct Number in a List
def second_highest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[-2]

# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(numbers):
    result=[]
    for i in numbers:
        if i not in result:
            result.append(i)
    return result

# Q9. Find the Missing Number from 1 to N
def missing_numbers(numbers,n):
    for i in range(1,n+1):
        if i not in numbers:
            return i
    return None

# Q10. Find Two Numbers Whose Sum Equals a Target
def pair_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [numbers[i], numbers[j]]
    return None

# Q11. Find the Number Closest to Zero
def closest_to_zero(numbers):
    if not numbers:
        return None
    closest = numbers[0]
    for num in numbers:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest) and num > closest:
            closest = num
    return closest

# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    result = []
    for num in list1:
        if num in list2 and num not in result:
            result.append(num)
    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(numbers, k):
    if not numbers:
        return []
    k = k % len(numbers)
    return numbers[-k:] + numbers[:-k] if k != 0 else numbers

# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_adjacent_sum(numbers):
    if len(numbers) < 2:
        return None
    max_sum = numbers[0] + numbers[1]
    for i in range(1, len(numbers) - 1):
        current_sum = numbers[i] + numbers[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_pairs_sum(numbers, target):
    result = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pair = tuple(sorted((numbers[i], numbers[j])))

                if pair not in result:
                    result.append(pair)
    result.sort()
    return result


