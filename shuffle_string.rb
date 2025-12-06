# shuffle_string.rb
# CSE 451 - Concepts of Programming Languages
# Solving the Array Shuffle Problem in Ruby

def shuffle_string(s, indices)
  # create empty result array
  result = Array.new(s.length, '')
  
  # place each character at its new position
  s.each_char.with_index do |char, i|
    result[indices[i]] = char
  end
  
  result.join
end


def visualize_steps(s, indices)
  # shows the algorithm working step by step
  puts "\nInput: s = '#{s}', indices = #{indices}"
  puts "-" * 40
  
  result = Array.new(s.length, '_')
  
  s.each_char.with_index do |char, i|
    target = indices[i]
    result[target] = char
    puts "Step #{i + 1}: '#{char}' goes to position #{target}"
    puts "  Result so far: #{result.join}"
  end
  
  puts "-" * 40
  puts "Final result: '#{result.join}'"
  result.join
end


# run tests
if __FILE__ == $0
  puts "Testing shuffle_string function..."
  puts
  
  # test 1: basic example
  s1 = "art"
  idx1 = [1, 0, 2]
  result1 = shuffle_string(s1, idx1)
  puts "Test 1: shuffle_string('#{s1}', #{idx1})"
  puts "  Expected: 'rat', Got: '#{result1}'"
  puts "  #{result1 == 'rat' ? 'PASS' : 'FAIL'}"
  puts
  
  # test 2: codeleet -> leetcode
  s2 = "codeleet"
  idx2 = [4, 5, 6, 7, 0, 2, 1, 3]
  result2 = shuffle_string(s2, idx2)
  puts "Test 2: shuffle_string('#{s2}', #{idx2})"
  puts "  Expected: 'leetcode', Got: '#{result2}'"
  puts "  #{result2 == 'leetcode' ? 'PASS' : 'FAIL'}"
  puts
  
  # test 3: simple swap
  s3 = "ab"
  idx3 = [1, 0]
  result3 = shuffle_string(s3, idx3)
  puts "Test 3: shuffle_string('#{s3}', #{idx3})"
  puts "  Expected: 'ba', Got: '#{result3}'"
  puts "  #{result3 == 'ba' ? 'PASS' : 'FAIL'}"
  puts
  
  # step by step demo
  puts "\n" + "=" * 50
  puts "Step-by-step visualization:"
  visualize_steps("art", [1, 0, 2])
end
