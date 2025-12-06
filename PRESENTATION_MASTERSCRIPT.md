# CSE 451: Concepts of Programming Languages
## Presentation Masterscript
### Python vs Ruby - Array Shuffle Problem

---

# SLIDE 1: TITLE SLIDE

**[SPEAKER NOTES]**

> "Good [morning/afternoon], everyone. Today we'll be presenting our CSE 451 course project, where we compare **Python** and **Ruby** by implementing the **Array Shuffle Problem**. My name is [Your Name], and I'm presenting with [Team Member Names]."

---

# SLIDE 2: AGENDA

**[DISPLAY ON SLIDE]**
1. Problem Statement
2. Python Language Overview
3. Ruby Language Overview
4. Code Implementation & Comparison
5. Strengths & Weaknesses Analysis
6. Challenges Faced
7. Conclusion

**[SPEAKER NOTES]**

> "Here's our agenda for today. We'll start by explaining the problem, then dive deep into each language's characteristics, compare our implementations, and wrap up with our findings."

---

# SLIDE 3: PROBLEM STATEMENT

**[DISPLAY ON SLIDE]**

**Array Shuffle Problem:**
- Given a string `s` and an integer array `indices` of the same length
- The character at position `i` moves to `indices[i]` in the shuffled string
- Return the shuffled string

**Example:**
```
Input:  s = "art", indices = [1, 0, 2]
Output: "rat"

Explanation:
- 'a' (index 0) -> position 1
- 'r' (index 1) -> position 0  
- 't' (index 2) -> position 2
Result: "rat"
```

**[SPEAKER NOTES]**

> "Our selected problem is the Array Shuffle Problem. We're given a string and an array of indices. Each character at position i in the original string should be placed at positions indices[i] in the result. For example, with the string 'art' and indices [1, 0, 2], the letter 'a' moves to position 1, 'r' moves to position 0, and 't' stays at position 2, giving us 'rat'."

---

# SLIDE 4: PYTHON - INTRODUCTION

**[DISPLAY ON SLIDE]**

## Python Overview
- **Creator:** Guido van Rossum (1991)
- **Philosophy:** "Readability counts" - Simple, clean syntax
- **Current Version:** Python 3.12+
- **Usage:** Web development, Data Science, AI/ML, Scripting, Automation

**[SPEAKER NOTES]**

> "Let's start with Python. Python was created by Guido van Rossum in 1991 with a focus on code readability and simplicity. Its philosophy emphasizes that code should be easy to read and write. Today, Python is one of the most popular programming languages, widely used in web development, data science, artificial intelligence, and automation."

---

# SLIDE 5: PYTHON - LANGUAGE CHARACTERISTICS

**[DISPLAY ON SLIDE]**

| Characteristic | Python |
|----------------|--------|
| **Type of Language** | Multi-paradigm: Imperative, Object-Oriented, Functional |
| **Implementation** | Interpreted (CPython bytecode) |
| **Variable Allocation** | Dynamic typing |
| **Typing Discipline** | Strong, Duck typing |

**[SPEAKER NOTES]**

> "Python is a **multi-paradigm language** - it supports imperative, object-oriented, and functional programming styles. It's **interpreted**, meaning the code is executed line by line by the Python interpreter, specifically CPython which compiles to bytecode. Python uses **dynamic typing** - you don't need to declare variable types; they're determined at runtime. Despite being dynamic, Python is **strongly typed** - you can't implicitly convert between incompatible types like adding a string to an integer."

---

# SLIDE 6: PYTHON - DATA TYPES

**[DISPLAY ON SLIDE]**

## Simple Data Types
- **Numeric:** `int`, `float`, `complex`
- **Boolean:** `bool` (True/False)
- **String:** `str` (immutable sequences of characters)
- **None:** `NoneType` (null value)

## Structured Data Types
- **List:** `[1, 2, 3]` - mutable, ordered
- **Tuple:** `(1, 2, 3)` - immutable, ordered
- **Dictionary:** `{'key': 'value'}` - key-value pairs
- **Set:** `{1, 2, 3}` - unordered, unique elements

**[SPEAKER NOTES]**

> "Python has rich data types. For simple types, we have integers with unlimited precision, floating-point numbers, complex numbers, booleans, and strings which are immutable. For structured types, Python offers Lists which are mutable ordered collections, Tuples which are immutable, Dictionaries for key-value storage, and Sets for unique unordered elements. This variety makes Python very flexible for different programming needs."

---

# SLIDE 7: PYTHON - CONTROL STRUCTURES

**[DISPLAY ON SLIDE]**

## Loop Statements
```python
# For loop (iterating over sequence)
for item in collection:
    print(item)

# For loop with range
for i in range(10):
    print(i)

# While loop
while condition:
    do_something()
```

## Other Controls
- `break` - exit loop
- `continue` - skip to next iteration
- `else` clause on loops (executes if no break)
- List comprehensions: `[x*2 for x in range(5)]`

**[SPEAKER NOTES]**

> "Python's control structures are elegant and readable. The **for loop** iterates directly over sequences - no need for index management. We use `range()` when we need numeric iteration. **While loops** run as long as a condition is true. Python has a unique feature: an `else` clause on loops that executes only if the loop completes without a `break`. List comprehensions provide a concise way to create lists from iterations."

---

# SLIDE 8: PYTHON - SUBPROGRAMS

**[DISPLAY ON SLIDE]**

## Functions
```python
def function_name(param1: str, param2: int = 10) -> str:
    """Docstring explaining the function"""
    return result
```

## Other Subprogram Features
- **Lambda functions:** `lambda x: x * 2`
- **Exception handling:** `try/except/finally`
- **Decorators:** `@decorator` for modifying functions
- **Generators:** `yield` for lazy evaluation
- **Async/Await:** Concurrent programming with `asyncio`

**[SPEAKER NOTES]**

> "Python functions are defined with the `def` keyword. They support optional type hints, default parameter values, and docstrings for documentation. Python also supports **lambda functions** for small anonymous functions, robust **exception handling** with try/except/finally blocks, **decorators** for modifying function behavior, **generators** for memory-efficient iteration, and **async/await** for concurrent programming."

---

# SLIDE 9: RUBY - INTRODUCTION

**[DISPLAY ON SLIDE]**

## Ruby Overview
- **Creator:** Yukihiro Matsumoto "Matz" (1995)
- **Philosophy:** "Programmer happiness" - Optimized for developer joy
- **Current Version:** Ruby 3.3+
- **Famous Quote:** "Ruby is designed to make programmers happy"
- **Usage:** Web development (Rails), Scripting, DevOps

**[SPEAKER NOTES]**

> "Now let's look at Ruby. Ruby was created by Yukihiro Matsumoto, known as 'Matz', in 1995. His philosophy was to optimize for **programmer happiness** rather than computer efficiency. Matz famously said 'Ruby is designed to make programmers happy.' Ruby gained massive popularity through Ruby on Rails, a web framework that revolutionized web development. It's also widely used for scripting and DevOps automation."

---

# SLIDE 10: RUBY - LANGUAGE CHARACTERISTICS

**[DISPLAY ON SLIDE]**

| Characteristic | Ruby |
|----------------|------|
| **Type of Language** | Multi-paradigm: Object-Oriented (pure), Functional, Imperative |
| **Implementation** | Interpreted (YARV bytecode) |
| **Variable Allocation** | Dynamic typing |
| **Typing Discipline** | Strong, Duck typing |

**Key Difference:** In Ruby, **EVERYTHING is an object** - even numbers and `nil`!

**[SPEAKER NOTES]**

> "Ruby is also a **multi-paradigm language**, but with a stronger emphasis on **pure object-orientation**. Unlike Python where primitives exist, in Ruby **everything is an object** - even numbers, booleans, and nil. You can call methods on the number 5 directly! Ruby is **interpreted** by YARV (Yet Another Ruby VM) which compiles to bytecode. Like Python, Ruby uses **dynamic typing** with **strong type checking** - meaning variables don't have declared types, but type errors are caught at runtime."

---

# SLIDE 11: RUBY - DATA TYPES

**[DISPLAY ON SLIDE]**

## Simple Data Types
- **Numeric:** `Integer`, `Float`, `Rational`, `Complex`
- **Boolean:** `true`, `false` (TrueClass, FalseClass)
- **String:** `String` (mutable by default!)
- **Symbol:** `:symbol` - immutable, memory-efficient identifiers
- **Nil:** `nil` (NilClass)

## Structured Data Types
- **Array:** `[1, 2, 3]` - mutable, ordered
- **Hash:** `{key: 'value'}` or `{'key' => 'value'}`
- **Range:** `(1..10)` or `(1...10)`
- **Set:** `Set.new([1, 2, 3])` (requires 'set' library)

**[SPEAKER NOTES]**

> "Ruby's data types are similar to Python but with key differences. Strings in Ruby are **mutable by default**, unlike Python. Ruby has **Symbols** - immutable identifiers that are memory-efficient and commonly used as hash keys. Arrays are like Python lists, and Hashes are like Python dictionaries. Ruby also has built-in **Range** objects for representing sequences. Notice that even `true`, `false`, and `nil` are objects of their respective classes."

---

# SLIDE 12: RUBY - CONTROL STRUCTURES

**[DISPLAY ON SLIDE]**

## Loop Statements
```ruby
# Each iterator (most Ruby-like way)
collection.each do |item|
  puts item
end

# For loop
for item in collection
  puts item
end

# While loop
while condition
  do_something
end

# Times iterator
5.times { |i| puts i }

# Until loop (opposite of while)
until condition
  do_something
end
```

**[SPEAKER NOTES]**

> "Ruby offers multiple ways to loop, but the most idiomatic is using **iterators** like `.each`. The `each` method with a block is preferred over traditional for loops. Ruby also has the `times` iterator which is very readable - '5.times' does something 5 times. A unique Ruby feature is the `until` loop, which runs until a condition becomes true - the opposite of while. Ruby blocks can use either `do...end` for multi-line or curly braces for single-line."

---

# SLIDE 13: RUBY - SUBPROGRAMS

**[DISPLAY ON SLIDE]**

## Methods (Functions)
```ruby
def method_name(param1, param2 = 10)
  # Last expression is automatically returned
  result
end
```

## Other Subprogram Features
- **Blocks:** `{ |x| x * 2 }` or `do |x| x * 2 end`
- **Procs:** `Proc.new { |x| x * 2 }` - stored blocks
- **Lambdas:** `-> (x) { x * 2 }` - stricter procs
- **Exception handling:** `begin/rescue/ensure`
- **Threads:** `Thread.new { ... }` for concurrency

**[SPEAKER NOTES]**

> "Ruby uses `def` to define methods. A key feature is **implicit return** - the last expression's value is automatically returned without needing a `return` keyword. Ruby has powerful **blocks** - anonymous code chunks passed to methods. **Procs** store blocks as objects, and **Lambdas** are stricter procs that check argument count. Exception handling uses `begin/rescue/ensure` instead of Python's `try/except/finally`. Ruby also supports threads for concurrent programming."

---

# SLIDE 14: CODE IMPLEMENTATION - PYTHON

**[DISPLAY ON SLIDE]**

```python
def shuffle_string(s: str, indices: list) -> str:
    """
    Restores the shuffled string based on the given indices.
    """
    # Create a list of the same length, initialized with empty strings
    result = [''] * len(s)
    
    # Place each character at its corresponding index
    for i, char in enumerate(s):
        result[indices[i]] = char
    
    # Join the list into a string and return
    return ''.join(result)

# Example usage
s = "art"
indices = [1, 0, 2]
print(shuffle_string(s, indices))  # Output: "rat"
```

**[SPEAKER NOTES]**

> "Here's our Python implementation. We define a function `shuffle_string` with **type hints** for clarity. We create a result list initialized with empty strings. Using `enumerate()`, we iterate through the string getting both the index and character. Each character is placed at its target position specified by indices[i]. Finally, we use `''.join()` to convert the list back to a string. This solution has O(n) time complexity."

---

# SLIDE 15: CODE IMPLEMENTATION - RUBY

**[DISPLAY ON SLIDE]**

```ruby
def shuffle_string(s, indices)
  # Create an array of the same length, initialized with empty strings
  result = Array.new(s.length, '')
  
  # Place each character at its corresponding index
  s.each_char.with_index do |char, i|
    result[indices[i]] = char
  end
  
  # Join the array into a string and return (implicit return)
  result.join
end

# Example usage
s = "art"
indices = [1, 0, 2]
puts shuffle_string(s, indices)  # Output: "rat"
```

**[SPEAKER NOTES]**

> "Now our Ruby implementation. The logic is identical, but notice the syntax differences. We use `Array.new` to create the result array. The `each_char.with_index` method chains two iterators - one to get characters and one to get indices. We use a **block** with `do...end` to process each character. Notice there's no explicit `return` statement - Ruby automatically returns the last expression, which is `result.join`. This is the idiomatic Ruby way."

---

# SLIDE 16: CODE COMPARISON

**[DISPLAY ON SLIDE]**

| Aspect | Python | Ruby |
|--------|--------|------|
| **Function Definition** | `def func(param):` | `def func(param)` |
| **Type Hints** | Supported `param: str` | Not built-in |
| **Array Creation** | `[''] * len(s)` | `Array.new(s.length, '')` |
| **Iteration** | `enumerate(s)` | `s.each_char.with_index` |
| **Block Syntax** | Indentation-based | `do...end` or `{ }` |
| **Return Statement** | Explicit `return` | Implicit (last expression) |
| **String Join** | `''.join(result)` | `result.join` |
| **Print** | `print()` | `puts` |

**[SPEAKER NOTES]**

> "Let's compare the two implementations side by side. Both languages have similar syntax for function definition, but Python uses a colon and Ruby doesn't. Python supports **type hints** natively, while Ruby requires external tools. For iteration, Python's `enumerate` and Ruby's `each_char.with_index` serve the same purpose but with different syntax. The biggest difference is **return statements** - Python requires explicit returns while Ruby uses implicit returns. Both achieve the same result with similar readability."

---

# SLIDE 17: PYTHON - STRENGTHS & WEAKNESSES

**[DISPLAY ON SLIDE]**

## Strengths
- **Readability:** Clean, English-like syntax
- **Vast Ecosystem:** pip has 400,000+ packages
- **Data Science Dominance:** NumPy, Pandas, TensorFlow, PyTorch
- **Easy to Learn:** Great for beginners
- **Strong Community:** Extensive documentation and support
- **Type Hints:** Optional static typing with mypy

## Weaknesses
- **Performance:** Slower than compiled languages
- **GIL (Global Interpreter Lock):** Limits true multi-threading
- **Mobile Development:** Not ideal for mobile apps
- **Memory Consumption:** Higher than lower-level languages
- **Runtime Errors:** Type errors only caught at runtime (without mypy)

**[SPEAKER NOTES]**

> "Python's main **strengths** are its readability and gentle learning curve, making it excellent for beginners. Its ecosystem is massive - pip has over 400,000 packages. Python dominates data science and machine learning. The **weaknesses** include performance - it's slower than compiled languages. The GIL limits true multi-threading. Python isn't ideal for mobile development, and type errors are only caught at runtime unless you use static type checkers like mypy."

---

# SLIDE 18: RUBY - STRENGTHS & WEAKNESSES

**[DISPLAY ON SLIDE]**

## Strengths
- **Developer Happiness:** Elegant, expressive syntax
- **Rails Framework:** Rapid web development
- **Pure OOP:** Everything is an object - consistent model
- **Metaprogramming:** Powerful DSL creation capabilities
- **Blocks & Iterators:** Elegant functional programming
- **Convention over Configuration:** Less boilerplate

## Weaknesses
- **Performance:** Slower than many alternatives
- **Declining Popularity:** Fewer job opportunities than Python
- **Learning Curve:** Multiple ways to do things can confuse
- **Documentation:** Less comprehensive than Python
- **Startup Time:** Ruby applications can be slow to start

**[SPEAKER NOTES]**

> "Ruby's **strengths** center on developer experience - the syntax is designed to be enjoyable. Ruby on Rails revolutionized web development with 'convention over configuration'. The pure OOP model is very consistent. Ruby excels at metaprogramming, making it great for creating domain-specific languages. The **weaknesses** include performance issues similar to Python. Ruby's popularity has declined, meaning fewer job opportunities. The flexibility of 'multiple ways to do things' can actually make it harder to learn."

---

# SLIDE 19: CHALLENGES FACED

**[DISPLAY ON SLIDE]**

## Setup Challenges

### Python
- [+] Pre-installed on most systems
- [+] Simple pip package management
- [!] Python 2 vs 3 compatibility (legacy issue)
- [!] Virtual environment management needed for projects

### Ruby
- [!] Requires manual installation on Windows
- [!] Version management with rbenv/rvm needed
- [!] Gem dependencies can be complex
- [+] Bundler helps manage dependencies

## Implementation Challenges
- Learning Ruby's block syntax coming from Python
- Understanding implicit returns vs explicit returns
- Different string handling (mutable vs immutable)

**[SPEAKER NOTES]**

> "During our project, we faced several challenges. Python was easier to set up - it's pre-installed on most systems. Ruby required manual installation on Windows and version management tools. For implementation, the main challenge was adapting to Ruby's syntax coming from Python. Understanding when to use `do...end` versus curly braces for blocks took some practice. The implicit return in Ruby felt unusual at first, and we had to remember that Ruby strings are mutable while Python strings are not."

---

# SLIDE 20: DEMONSTRATION

**[SPEAKER NOTES]**

> "Now let's run our code and see it in action."

**[LIVE DEMO - Run both programs]**

**Python:**
```bash
python shuffle_string.py
```

**Ruby:**
```bash
ruby shuffle_string.rb
```

**Expected Output for both:**
```
Test 1:
  Input:  s = 'art', indices = [1, 0, 2]
  Output: 'rat'
  Expected: 'rat'

Test 2:
  Input:  s = 'codeleet', indices = [4, 5, 6, 7, 0, 2, 1, 3]
  Output: 'leetcode'
  Expected: 'leetcode'
...
```

---

# SLIDE 21: CONCLUSION

**[DISPLAY ON SLIDE]**

## Key Takeaways

| Aspect | Python | Ruby |
|--------|--------|------|
| **Best For** | Data Science, AI/ML, Scripting | Web Development, DSLs |
| **Philosophy** | Readability | Developer Happiness |
| **OOP Model** | Multi-paradigm | Pure OOP |
| **Learning Curve** | Easier | Moderate |
| **Job Market** | Larger | Smaller but specialized |

## Our Verdict
Both languages are excellent for solving this problem with similar code structure and readability. Choice depends on project requirements and ecosystem needs.

**[SPEAKER NOTES]**

> "In conclusion, both Python and Ruby solved our problem elegantly with similar code structure. Python is better for data science and has a larger job market, while Ruby excels in web development with Rails. Python prioritizes 'one obvious way' to do things, while Ruby offers flexibility and multiple approaches. Both are excellent high-level languages - the choice depends on your project needs and which ecosystem you need to leverage."

---

# SLIDE 22: QUESTIONS

**[DISPLAY ON SLIDE]**

# Thank You!
## Questions?

**Team Members:**
- [Your Name]
- [Team Member 2]
- [Team Member 3]

**Resources:**
- Python: https://python.org
- Ruby: https://ruby-lang.org

---

# QUICK REFERENCE CARD

## When Professor Asks...

**Q: "Why did you choose these languages?"**
> "We chose Python because it's our familiar language and widely used in industry. Ruby was chosen because it offers an interesting contrast with its pure OOP approach and different syntax philosophy, while still being in the same category of dynamic, interpreted languages."

**Q: "Which language did you find easier to use?"**
> "Python was easier due to our familiarity. However, Ruby's syntax felt very natural once we understood blocks and implicit returns. Both achieve the same readability."

**Q: "What's the time complexity of your solution?"**
> "O(n) for both implementations, where n is the length of the string. We iterate through the string once and array access is O(1)."

**Q: "Could you optimize this further?"**
> "The solution is already optimal at O(n). Any alternative approach would still need to visit each character at least once."

---

# PRESENTATION TIMING GUIDE

| Section | Duration |
|---------|----------|
| Introduction & Problem | 1-2 min |
| Python Overview | 3-4 min |
| Ruby Overview | 3-4 min |
| Code Comparison | 3-4 min |
| Strengths/Weaknesses | 2-3 min |
| Challenges | 1-2 min |
| Demo & Conclusion | 2-3 min |
| **Total** | **~15-20 min** |

---

*Good luck with your presentation!*
