# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  CSE 451: Concepts of Programming Languages                                  ║
# ║  String Shuffle Algorithm - Demonstrating Ruby's Elegance                    ║
# ║  Team: [Your Team Name]                                                       ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# Problem Description:
#     Given a "scrambled" string and a map of where each letter should go,
#     reconstruct the original word. Like solving a word puzzle where
#     you know exactly which slot each letter belongs in!


# A class that handles string reconstruction using index mapping.
# Demonstrates Ruby's pure OOP nature - even our algorithm is an object!
class StringShuffler
  attr_reader :scrambled, :positions
  
  def initialize(scrambled, positions)
    @scrambled = scrambled
    @positions = positions
    validate_inputs!
  end
  
  # Reconstruct using Ruby's powerful enumerable methods
  def reconstruct
    # Create pairs of [target_position, character] using zip
    char_position_pairs = @positions.zip(@scrambled.chars)
    
    # Sort by target position (first element of each pair)
    sorted_pairs = char_position_pairs.sort_by { |pos, _char| pos }
    
    # Extract just the characters and join them
    # Using map with block - very Ruby-esque!
    sorted_pairs.map { |_pos, char| char }.join
  end
  
  # Alternative: Using inject (Ruby's reduce) for functional style
  def reconstruct_functional
    @positions
      .zip(@scrambled.chars)           # Pair positions with characters
      .sort_by(&:first)                 # Sort by position (Symbol#to_proc magic!)
      .inject('') { |acc, (_, ch)| acc + ch }  # Build string functionally
  end
  
  # Visual step-by-step reconstruction
  def reconstruct_visual
    puts "\n#{'=' * 50}"
    puts "RECONSTRUCTION PROCESS"
    puts '=' * 50
    
    result_slots = Array.new(@scrambled.length, '_')
    
    @scrambled.each_char.with_index do |char, idx|
      target_pos = @positions[idx]
      result_slots[target_pos] = char
      current_state = result_slots.join
      puts "  Step #{idx + 1}: '#{char}' -> slot #{target_pos} | Result: [#{current_state}]"
    end
    
    final_result = result_slots.join
    puts '=' * 50
    puts "FINAL: '#{final_result}'"
    puts "#{'=' * 50}\n"
    
    final_result
  end
  
  private
  
  def validate_inputs!
    unless @scrambled.length == @positions.length
      raise ArgumentError, 'String length must match position map length!'
    end
    
    unless @positions.sort == (0...@positions.length).to_a
      raise ArgumentError, 'Position map must contain each index exactly once!'
    end
  end
end


# Module for standalone function - shows Ruby's module system
module ShuffleAlgorithm
  # Standalone convenience function that wraps the class
  def self.shuffle_string(s, indices)
    StringShuffler.new(s, indices).reconstruct
  end
  
  # One-liner using Ruby's expressive syntax
  def self.shuffle_oneliner(s, indices)
    indices.zip(s.chars).sort.map(&:last).join
  end
end


# Demonstration with comprehensive test cases
def demonstrate_algorithm
  puts "\n+#{'=' * 58}+"
  puts "|#{' STRING SHUFFLE ALGORITHM - RUBY IMPLEMENTATION '.center(58)}|"
  puts "+#{'=' * 58}+\n"
  
  # Test scenarios with real-world analogies
  test_cases = [
    {
      name: 'Basic Word Puzzle',
      scrambled: 'art',
      positions: [1, 0, 2],
      expected: 'rat',
      story: 'Unscrambling a 3-letter animal name'
    },
    {
      name: "Programmer's Magic",
      scrambled: 'codeleet',
      positions: [4, 5, 6, 7, 0, 2, 1, 3],
      expected: 'leetcode',
      story: 'Revealing a famous coding platform'
    },
    {
      name: 'Simple Swap',
      scrambled: 'ba',
      positions: [1, 0],
      expected: 'ab',
      story: 'Alphabetical ordering'
    },
    {
      name: 'Complete Reversal',
      scrambled: 'dcba',
      positions: [3, 2, 1, 0],
      expected: 'abcd',
      story: 'Mirror image restoration'
    }
  ]
  
  all_passed = true
  
  test_cases.each_with_index do |test, i|
    puts "Test #{i + 1}: #{test[:name]}"
    puts "   Story: #{test[:story]}"
    puts "   Input:    scrambled='#{test[:scrambled]}', positions=#{test[:positions]}"
    
    result = ShuffleAlgorithm.shuffle_string(test[:scrambled], test[:positions])
    passed = result == test[:expected]
    
    status = passed ? '[PASS]' : '[FAIL]'
    puts "   Output:   '#{result}' (expected: '#{test[:expected]}') #{status}"
    puts
    
    all_passed = false unless passed
  end
  
  # Show visual reconstruction for the first example
  puts "\nDETAILED VISUALIZATION:"
  visualizer = StringShuffler.new('art', [1, 0, 2])
  visualizer.reconstruct_visual
  
  # Bonus: Show Ruby's one-liner capability
  puts 'BONUS - Ruby One-Liner Solution:'
  puts "   indices.zip(s.chars).sort.map(&:last).join"
  puts "   Result: '#{ShuffleAlgorithm.shuffle_oneliner('art', [1, 0, 2])}'"
  puts
  
  # Summary
  puts '-' * 60
  if all_passed
    puts 'All tests passed! Algorithm working correctly.'
  else
    puts 'Some tests failed. Please review the implementation.'
  end
  puts '-' * 60
end


# Entry point - demonstrates Ruby's scripting capability
if __FILE__ == $PROGRAM_NAME
  demonstrate_algorithm
end
