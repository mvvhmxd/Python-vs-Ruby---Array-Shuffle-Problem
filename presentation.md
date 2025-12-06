# CSE 451: Concepts of Programming Languages
## Python vs Ruby - Array Shuffle Problem

### Team Members
- [Your Name Here]

---

## The Problem

Given a string `s` and an integer array `indices` of the same length, the character at position `i` moves to `indices[i]` in the shuffled string.

**Example:**
- Input: `s = "art"`, `indices = [1, 0, 2]`
- Output: `"rat"`

Why? Because:
- 'a' at index 0 goes to index 1
- 'r' at index 1 goes to index 0  
- 't' at index 2 stays at index 2

---

## Python Solution

```python
def shuffle_string(s, indices):
    result = [''] * len(s)
    for i, char in enumerate(s):
        result[indices[i]] = char
    return ''.join(result)
```

### Key Features Used:
- `enumerate()` - gives us both index and character
- List comprehension style with `[''] * len(s)`
- `join()` to convert list back to string

---

## Ruby Solution

```ruby
def shuffle_string(s, indices)
  result = Array.new(s.length, '')
  s.each_char.with_index do |char, i|
    result[indices[i]] = char
  end
  result.join
end
```

### Key Features Used:
- `Array.new()` - creates array with default values
- `each_char.with_index` - iterates with index
- Block syntax with `do |char, i| ... end`

---

## Language Comparison

| Feature | Python | Ruby |
|---------|--------|------|
| Typing | Dynamic | Dynamic |
| Implementation | CPython (C) | MRI (C) |
| Array Creation | `[''] * n` | `Array.new(n, '')` |
| Iteration | `enumerate(s)` | `s.each_char.with_index` |
| Join | `''.join(list)` | `array.join` |

---

## About Python

Python is a high-level interpreted language created by Guido van Rossum in 1991. It's known for:
- Clean, readable syntax
- Huge ecosystem of libraries
- Great for beginners and experts alike
- Used in web dev, data science, AI, scripting

---

## About Ruby

Ruby was created by Yukihiro Matsumoto in 1995. It focuses on:
- Developer happiness
- Everything is an object
- Flexible syntax (multiple ways to do things)
- Popular for web development (Ruby on Rails)

---

## Main Differences We Noticed

1. **Syntax**: Python uses colons and indentation, Ruby uses `do/end` blocks
2. **Iteration**: Python's `enumerate()` vs Ruby's `each_char.with_index`
3. **Array init**: Python's list multiplication vs Ruby's `Array.new()`
4. **Method calls**: Python's `''.join(list)` vs Ruby's `list.join`

---

## Challenges Faced

1. **Installing Ruby** - Had to set up Ruby environment on Windows
2. **Learning Ruby syntax** - Coming from Python, the block syntax was new
3. **Testing** - Made sure both solutions produce identical output

---

## Demo

Check out our interactive visualizer that shows both algorithms working step-by-step!

- **Desktop App**: `demo_visualizer.py`
- **Web Version**: `index.html`

Both show the character movement animation and execution logs.

---

## Conclusion

Both Python and Ruby are capable of solving this problem efficiently. The main differences are in syntax and style rather than capability. Python feels more explicit, while Ruby feels more flexible.

**Time Complexity**: O(n)
**Space Complexity**: O(n)

Both solutions use the same algorithm - just different language syntax.
