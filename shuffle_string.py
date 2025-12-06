"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  CSE 451: Concepts of Programming Languages                                  ║
║  String Shuffle Algorithm - Demonstrating Python's Elegance                  ║
║  Team: [Your Team Name]                                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

Problem Description:
    Given a "scrambled" string and a map of where each letter should go,
    reconstruct the original word. Think of it like solving a word puzzle
    where you know exactly which slot each letter belongs in!
"""

from typing import List, Tuple
from functools import reduce


class StringShuffler:
    """
    A class that handles string reconstruction using index mapping.
    Demonstrates Python's OOP capabilities alongside functional programming.
    """
    
    def __init__(self, scrambled: str, position_map: List[int]):
        """Initialize with the scrambled string and its position mapping."""
        self._scrambled = scrambled
        self._positions = position_map
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Ensure the input is valid before processing."""
        if len(self._scrambled) != len(self._positions):
            raise ValueError("String length must match position map length!")
        if set(self._positions) != set(range(len(self._positions))):
            raise ValueError("Position map must contain each index exactly once!")
    
    def reconstruct(self) -> str:
        """
        Reconstruct the original string using a functional approach.
        
        Uses reduce to build the result character by character,
        demonstrating functional programming in Python.
        """
        # Create index-character pairs for processing
        char_position_pairs: List[Tuple[int, str]] = list(
            zip(self._positions, self._scrambled)
        )
        
        # Sort by target position and extract characters
        sorted_pairs = sorted(char_position_pairs, key=lambda pair: pair[0])
        
        # Use reduce to concatenate (demonstrating functional style)
        original = reduce(
            lambda accumulated, pair: accumulated + pair[1],
            sorted_pairs,
            ""  # Start with empty string
        )
        
        return original
    
    def reconstruct_visual(self) -> str:
        """
        Same reconstruction but with visual step-by-step output.
        Great for understanding and demonstrating the algorithm!
        """
        print("\n" + "="*50)
        print("RECONSTRUCTION PROCESS")
        print("="*50)
        
        result_slots = ['_'] * len(self._scrambled)
        
        for idx, (char, target_pos) in enumerate(zip(self._scrambled, self._positions)):
            result_slots[target_pos] = char
            current_state = ''.join(result_slots)
            print(f"  Step {idx + 1}: '{char}' -> slot {target_pos} | Result: [{current_state}]")
        
        final_result = ''.join(result_slots)
        print("="*50)
        print(f"FINAL: '{final_result}'")
        print("="*50 + "\n")
        
        return final_result


def shuffle_string(s: str, indices: List[int]) -> str:
    """
    Standalone function for quick usage.
    Wraps the StringShuffler class for convenience.
    """
    shuffler = StringShuffler(s, indices)
    return shuffler.reconstruct()


def demonstrate_algorithm():
    """
    Comprehensive demonstration with multiple test scenarios.
    Shows both the algorithm logic and Python's features.
    """
    print("\n" + "+" + "="*58 + "+")
    print("|" + " STRING SHUFFLE ALGORITHM - PYTHON IMPLEMENTATION ".center(58) + "|")
    print("+" + "="*58 + "+\n")
    
    # Test scenarios with real-world analogies
    test_cases = [
        {
            "name": "Basic Word Puzzle",
            "scrambled": "art",
            "positions": [1, 0, 2],
            "expected": "rat",
            "story": "Unscrambling a 3-letter animal name"
        },
        {
            "name": "Programmer's Magic",
            "scrambled": "codeleet",
            "positions": [4, 5, 6, 7, 0, 2, 1, 3],
            "expected": "leetcode",
            "story": "Revealing a famous coding platform"
        },
        {
            "name": "Simple Swap",
            "scrambled": "ba",
            "positions": [1, 0],
            "expected": "ab",
            "story": "Alphabetical ordering"
        },
        {
            "name": "Complete Reversal",
            "scrambled": "dcba",
            "positions": [3, 2, 1, 0],
            "expected": "abcd",
            "story": "Mirror image restoration"
        },
    ]
    
    all_passed = True
    
    for i, test in enumerate(test_cases, 1):
        print(f"Test {i}: {test['name']}")
        print(f"   Story: {test['story']}")
        print(f"   Input:    scrambled='{test['scrambled']}', positions={test['positions']}")
        
        result = shuffle_string(test["scrambled"], test["positions"])
        passed = result == test["expected"]
        
        status = "[PASS]" if passed else "[FAIL]"
        print(f"   Output:   '{result}' (expected: '{test['expected']}') {status}")
        print()
        
        if not passed:
            all_passed = False
    
    # Show visual reconstruction for the first example
    print("\nDETAILED VISUALIZATION:")
    visualizer = StringShuffler("art", [1, 0, 2])
    visualizer.reconstruct_visual()
    
    # Summary
    print("-"*60)
    if all_passed:
        print("All tests passed! Algorithm working correctly.")
    else:
        print("Some tests failed. Please review the implementation.")
    print("-"*60)


# Entry point
if __name__ == "__main__":
    demonstrate_algorithm()
