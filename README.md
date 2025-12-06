# Python vs Ruby - Array Shuffle Problem

CSE 451: Concepts of Programming Languages

## The Problem

Given a string `s` and an integer array `indices`, shuffle the string so that character at position `i` moves to `indices[i]`.

**Example:**
```
Input: s = "art", indices = [1, 0, 2]
Output: "rat"
```

## Files

- `shuffle_string.py` - Python solution
- `shuffle_string.rb` - Ruby solution
- `demo_visualizer.py` - Desktop demo app (requires Python + tkinter)
- `index.html` - Web demo (open in browser)
- `PRESENTATION_MASTERSCRIPT.md` - Presentation notes

## Run the Code

**Python:**
```bash
python shuffle_string.py
```

**Ruby:**
```bash
ruby shuffle_string.rb
```

## Live Demo

Open `index.html` in your browser for the interactive visualizer.

Or run the desktop version:
```bash
python demo_visualizer.py
```

## How It Works

Both solutions use the same approach:
1. Create an empty result array of the same length
2. For each character, place it at the position specified by indices
3. Join the result back into a string

```python
# Python
result[indices[i]] = char

# Ruby
result[indices[i]] = char
```

Same logic, different syntax!
