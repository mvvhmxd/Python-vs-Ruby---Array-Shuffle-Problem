# shuffle_string.py
# CSE 451 - Concepts of Programming Languages
# Solving the Array Shuffle Problem in Python

def shuffle_string(s, indices):
    """
    Takes a string s and shuffles it according to indices array.
    Each character at position i goes to indices[i] in the result.
    """
    result = [''] * len(s)
    for i, char in enumerate(s):
        result[indices[i]] = char
    return ''.join(result)


def visualize_steps(s, indices):
    """Shows how the algorithm works step by step"""
    print(f"\nInput: s = '{s}', indices = {indices}")
    print("-" * 40)
    
    result = ['_'] * len(s)
    
    for i, char in enumerate(s):
        target = indices[i]
        result[target] = char
        print(f"Step {i+1}: '{char}' goes to position {target}")
        print(f"  Result so far: {''.join(result)}")
    
    print("-" * 40)
    print(f"Final result: '{''.join(result)}'")
    return ''.join(result)


# test cases
if __name__ == "__main__":
    print("Testing shuffle_string function...")
    print()
    
    # test 1: basic example from the problem
    s1 = "art"
    idx1 = [1, 0, 2]
    result1 = shuffle_string(s1, idx1)
    print(f"Test 1: shuffle_string('{s1}', {idx1})")
    print(f"  Expected: 'rat', Got: '{result1}'")
    print(f"  {'PASS' if result1 == 'rat' else 'FAIL'}")
    print()
    
    # test 2: codeleet example
    s2 = "codeleet"
    idx2 = [4, 5, 6, 7, 0, 2, 1, 3]
    result2 = shuffle_string(s2, idx2)
    print(f"Test 2: shuffle_string('{s2}', {idx2})")
    print(f"  Expected: 'leetcode', Got: '{result2}'")
    print(f"  {'PASS' if result2 == 'leetcode' else 'FAIL'}")
    print()
    
    # test 3: simple swap
    s3 = "ab"
    idx3 = [1, 0]
    result3 = shuffle_string(s3, idx3)
    print(f"Test 3: shuffle_string('{s3}', {idx3})")
    print(f"  Expected: 'ba', Got: '{result3}'")
    print(f"  {'PASS' if result3 == 'ba' else 'FAIL'}")
    print()
    
    # show step by step for art -> rat
    print("\n" + "=" * 50)
    print("Step-by-step visualization:")
    visualize_steps("art", [1, 0, 2])
