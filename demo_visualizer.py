"""
CSE 451: Concepts of Programming Languages
String Shuffle Algorithm Visualizer - Python vs Ruby
With Execution Logs showing step-by-step processing
"""

import tkinter as tk
from tkinter import ttk, font
import time
import threading
import random


class ModernColors:
    BG_DARK = "#0a0a0f"
    BG_CARD = "#12121a"
    PYTHON_BLUE = "#3776ab"
    PYTHON_YELLOW = "#ffd43b"
    RUBY_RED = "#cc342d"
    RUBY_PINK = "#ff6b9d"
    ACCENT_PRIMARY = "#6366f1"
    ACCENT_SECONDARY = "#8b5cf6"
    ACCENT_SUCCESS = "#10b981"
    ACCENT_WARNING = "#f59e0b"
    ACCENT_ERROR = "#ef4444"
    TEXT_PRIMARY = "#ffffff"
    TEXT_SECONDARY = "#a1a1aa"
    TEXT_MUTED = "#52525b"
    SLOT_EMPTY = "#27272a"
    SLOT_HIGHLIGHT = "#22c55e"
    SLOT_PYTHON = "#3776ab"
    SLOT_RUBY = "#cc342d"
    CHAR_BOX = "#3f3f46"


class AnimatedButton(tk.Canvas):
    def __init__(self, parent, text, command, color=ModernColors.ACCENT_PRIMARY, 
                 width=200, height=50, **kwargs):
        super().__init__(parent, width=width, height=height, 
                        bg=parent.cget('bg'), highlightthickness=0, **kwargs)
        self.color = color
        self.text = text
        self.command = command
        self.width = width
        self.height = height
        self._draw(color)
        self.bind("<Enter>", lambda e: self._draw(self._lighten(color)))
        self.bind("<Leave>", lambda e: self._draw(color))
        self.bind("<Button-1>", lambda e: command() if command else None)
    
    def _lighten(self, c):
        return f"#{min(255,int(c[1:3],16)+30):02x}{min(255,int(c[3:5],16)+30):02x}{min(255,int(c[5:7],16)+30):02x}"
    
    def _draw(self, color):
        self.delete("all")
        r = 12
        pts = [2+r,2, self.width-2-r,2, self.width-2,2, self.width-2,2+r, 
               self.width-2,self.height-2-r, self.width-2,self.height-2,
               self.width-2-r,self.height-2, 2+r,self.height-2, 2,self.height-2,
               2,self.height-2-r, 2,2+r, 2,2]
        self.create_polygon(pts, smooth=True, fill=color, outline="")
        self.create_text(self.width//2, self.height//2, text=self.text,
                        fill=ModernColors.TEXT_PRIMARY, font=("Segoe UI", 11, "bold"))
        self.config(cursor="hand2")


class CharacterSlot(tk.Canvas):
    def __init__(self, parent, size=50, index=0, lang_color=None, **kwargs):
        super().__init__(parent, width=size, height=size+20,
                        bg=ModernColors.BG_CARD, highlightthickness=0, **kwargs)
        self.size = size
        self.index = index
        self.lang_color = lang_color
        self.clear()
    
    def _rect(self, x1, y1, x2, y2, r, **kw):
        pts = [x1+r,y1, x2-r,y1, x2,y1, x2,y1+r, x2,y2-r, x2,y2, x2-r,y2, x1+r,y2, x1,y2, x1,y2-r, x1,y1+r, x1,y1]
        return self.create_polygon(pts, smooth=True, **kw)
    
    def set_char(self, char, highlight=False):
        self.delete("all")
        color = ModernColors.SLOT_HIGHLIGHT if highlight else (self.lang_color or ModernColors.SLOT_PYTHON)
        if highlight:
            self._rect(2, 2, self.size-2, self.size-2, 10, fill=ModernColors.ACCENT_SUCCESS, outline="")
        self._rect(4, 4, self.size-4, self.size-4, 8, fill=color, outline="")
        self.create_text(self.size//2, self.size//2, text=char,
                        fill=ModernColors.TEXT_PRIMARY, font=("Consolas", 18, "bold"))
        self.create_text(self.size//2, self.size+10, text=str(self.index),
                        fill=ModernColors.TEXT_SECONDARY, font=("Consolas", 9))
    
    def clear(self):
        self.delete("all")
        self._rect(4, 4, self.size-4, self.size-4, 8, fill=ModernColors.SLOT_EMPTY, outline=ModernColors.TEXT_MUTED)
        self.create_text(self.size//2, self.size+10, text=str(self.index),
                        fill=ModernColors.TEXT_MUTED, font=("Consolas", 9))


class SourceCharacter(tk.Canvas):
    def __init__(self, parent, char, index, target, size=50, **kwargs):
        super().__init__(parent, width=size, height=size+35,
                        bg=ModernColors.BG_CARD, highlightthickness=0, **kwargs)
        self.size = size
        self.char = char
        self.index = index
        self.target = target
        self.processed = False
        self._draw()
    
    def _rect(self, x1, y1, x2, y2, r, **kw):
        pts = [x1+r,y1, x2-r,y1, x2,y1, x2,y1+r, x2,y2-r, x2,y2, x2-r,y2, x1+r,y2, x1,y2, x1,y2-r, x1,y1+r, x1,y1]
        return self.create_polygon(pts, smooth=True, **kw)
    
    def _draw(self):
        self.delete("all")
        bg = ModernColors.SLOT_HIGHLIGHT if self.processed else ModernColors.CHAR_BOX
        self._rect(4, 4, self.size-4, self.size-4, 8, fill=bg, outline=ModernColors.ACCENT_PRIMARY)
        self.create_text(self.size//2, self.size//2, text=self.char,
                        fill=ModernColors.TEXT_PRIMARY, font=("Consolas", 18, "bold"))
        self.create_text(self.size//2, self.size+10, text=f"[{self.index}]",
                        fill=ModernColors.TEXT_MUTED, font=("Consolas", 8))
        self.create_text(self.size//2, self.size+24, text=f"->[{self.target}]",
                        fill=ModernColors.ACCENT_SECONDARY, font=("Consolas", 8, "bold"))
    
    def set_processed(self, val=True):
        self.processed = val
        self._draw()


class StringShuffleVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("String Shuffle Visualizer | CSE 451 - Python vs Ruby")
        self.geometry("1400x950")
        self.configure(bg=ModernColors.BG_DARK)
        
        self.input_string = ""
        self.indices = []
        self.original_word = ""
        self.is_animating = False
        self.source_chars = []
        self.python_slots = []
        self.ruby_slots = []
        
        self._build_ui()
    
    def _build_ui(self):
        # Header
        hdr = tk.Frame(self, bg=ModernColors.BG_DARK)
        hdr.pack(fill=tk.X, padx=30, pady=(15, 10))
        tk.Label(hdr, text="String Shuffle", font=("Segoe UI", 24, "bold"),
                fg=ModernColors.ACCENT_PRIMARY, bg=ModernColors.BG_DARK).pack(side=tk.LEFT)
        tk.Label(hdr, text=" Algorithm", font=("Segoe UI", 24, "bold"),
                fg=ModernColors.ACCENT_SECONDARY, bg=ModernColors.BG_DARK).pack(side=tk.LEFT)
        tk.Label(hdr, text="CSE 451: Concepts of Programming Languages",
                font=("Segoe UI", 11), fg=ModernColors.TEXT_SECONDARY,
                bg=ModernColors.BG_DARK).pack(side=tk.RIGHT)
        
        # Mode selector
        mode_frm = tk.Frame(self, bg=ModernColors.BG_CARD)
        mode_frm.pack(fill=tk.X, padx=30, pady=5)
        tk.Label(mode_frm, text="MODE:", font=("Segoe UI", 10, "bold"),
                fg=ModernColors.TEXT_PRIMARY, bg=ModernColors.BG_CARD).pack(side=tk.LEFT, padx=15, pady=8)
        self.mode_var = tk.StringVar(value="manual")
        tk.Radiobutton(mode_frm, text="MANUAL (s + indices)", variable=self.mode_var, value="manual",
                      font=("Segoe UI", 10), fg=ModernColors.ACCENT_SUCCESS, bg=ModernColors.BG_CARD,
                      selectcolor=ModernColors.BG_DARK, command=self._switch_mode).pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(mode_frm, text="AUTO (shuffle word)", variable=self.mode_var, value="auto",
                      font=("Segoe UI", 10), fg=ModernColors.ACCENT_SECONDARY, bg=ModernColors.BG_CARD,
                      selectcolor=ModernColors.BG_DARK, command=self._switch_mode).pack(side=tk.LEFT, padx=10)
        
        # Input frame
        self.input_frame = tk.Frame(self, bg=ModernColors.BG_CARD)
        self.input_frame.pack(fill=tk.X, padx=30, pady=5)
        self._create_manual_inputs()
        
        # Status
        self.status = tk.Label(self, text="", font=("Segoe UI", 12),
                              fg=ModernColors.ACCENT_PRIMARY, bg=ModernColors.BG_DARK)
        self.status.pack(pady=5)
        
        # Original word display (for auto mode)
        self.orig_frame = tk.Frame(self, bg=ModernColors.BG_CARD)
        self.orig_frame.pack(fill=tk.X, padx=30, pady=3)
        self.orig_label = tk.Label(self.orig_frame, text="", font=("Segoe UI", 10, "bold"),
                                   fg=ModernColors.ACCENT_SUCCESS, bg=ModernColors.BG_CARD)
        self.orig_label.pack(anchor=tk.W, padx=15, pady=(5,0))
        self.orig_display = tk.Label(self.orig_frame, text="", font=("Consolas", 18, "bold"),
                                     fg=ModernColors.ACCENT_SUCCESS, bg=ModernColors.BG_CARD)
        self.orig_display.pack(pady=(0,5))
        
        # Shuffled/Input string
        inp_frm = tk.Frame(self, bg=ModernColors.BG_CARD)
        inp_frm.pack(fill=tk.X, padx=30, pady=3)
        self.inp_label = tk.Label(inp_frm, text="INPUT STRING (s)", font=("Segoe UI", 10, "bold"),
                                  fg=ModernColors.TEXT_MUTED, bg=ModernColors.BG_CARD)
        self.inp_label.pack(anchor=tk.W, padx=15, pady=(5,0))
        self.source_frame = tk.Frame(inp_frm, bg=ModernColors.BG_CARD)
        self.source_frame.pack(pady=5)
        
        # Results - Python and Ruby side by side with logs
        results = tk.Frame(self, bg=ModernColors.BG_DARK)
        results.pack(fill=tk.BOTH, expand=True, padx=30, pady=5)
        
        # Python section
        py_sec = tk.Frame(results, bg=ModernColors.BG_CARD)
        py_sec.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0,5))
        tk.Frame(py_sec, bg=ModernColors.PYTHON_BLUE, height=30).pack(fill=tk.X)
        tk.Label(py_sec, text="PYTHON", font=("Segoe UI", 11, "bold"),
                fg=ModernColors.TEXT_PRIMARY, bg=ModernColors.PYTHON_BLUE).place(x=10, y=3)
        self.python_frame = tk.Frame(py_sec, bg=ModernColors.BG_CARD)
        self.python_frame.pack(pady=10)
        self.python_result = tk.Label(py_sec, text="", font=("Consolas", 14, "bold"),
                                      fg=ModernColors.PYTHON_YELLOW, bg=ModernColors.BG_CARD)
        self.python_result.pack()
        
        # Python log
        tk.Label(py_sec, text="Execution Log:", font=("Segoe UI", 9, "bold"),
                fg=ModernColors.TEXT_MUTED, bg=ModernColors.BG_CARD).pack(anchor=tk.W, padx=10, pady=(10,0))
        self.python_log = tk.Text(py_sec, font=("Consolas", 9), height=8, width=45,
                                  bg=ModernColors.BG_DARK, fg=ModernColors.PYTHON_YELLOW,
                                  relief=tk.FLAT, state=tk.DISABLED)
        self.python_log.pack(padx=10, pady=5, fill=tk.X)
        
        # Ruby section
        rb_sec = tk.Frame(results, bg=ModernColors.BG_CARD)
        rb_sec.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5,0))
        tk.Frame(rb_sec, bg=ModernColors.RUBY_RED, height=30).pack(fill=tk.X)
        tk.Label(rb_sec, text="RUBY", font=("Segoe UI", 11, "bold"),
                fg=ModernColors.TEXT_PRIMARY, bg=ModernColors.RUBY_RED).place(x=10, y=3)
        self.ruby_frame = tk.Frame(rb_sec, bg=ModernColors.BG_CARD)
        self.ruby_frame.pack(pady=10)
        self.ruby_result = tk.Label(rb_sec, text="", font=("Consolas", 14, "bold"),
                                    fg=ModernColors.RUBY_PINK, bg=ModernColors.BG_CARD)
        self.ruby_result.pack()
        
        # Ruby log
        tk.Label(rb_sec, text="Execution Log:", font=("Segoe UI", 9, "bold"),
                fg=ModernColors.TEXT_MUTED, bg=ModernColors.BG_CARD).pack(anchor=tk.W, padx=10, pady=(10,0))
        self.ruby_log = tk.Text(rb_sec, font=("Consolas", 9), height=8, width=45,
                                bg=ModernColors.BG_DARK, fg=ModernColors.RUBY_PINK,
                                relief=tk.FLAT, state=tk.DISABLED)
        self.ruby_log.pack(padx=10, pady=5, fill=tk.X)
        
        # Code display
        code_frm = tk.Frame(self, bg=ModernColors.BG_DARK)
        code_frm.pack(fill=tk.X, padx=30, pady=5)
        
        py_code = tk.Frame(code_frm, bg=ModernColors.BG_CARD)
        py_code.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0,5))
        tk.Frame(py_code, bg=ModernColors.PYTHON_BLUE, height=2).pack(fill=tk.X)
        py_txt = tk.Text(py_code, font=("Consolas", 9), height=5, bg=ModernColors.BG_CARD,
                        fg=ModernColors.TEXT_PRIMARY, relief=tk.FLAT)
        py_txt.insert("1.0", "def shuffle_string(s, indices):\n  result = [''] * len(s)\n  for i, char in enumerate(s):\n    result[indices[i]] = char\n  return ''.join(result)")
        py_txt.config(state=tk.DISABLED)
        py_txt.pack(padx=10, pady=5)
        
        rb_code = tk.Frame(code_frm, bg=ModernColors.BG_CARD)
        rb_code.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5,0))
        tk.Frame(rb_code, bg=ModernColors.RUBY_RED, height=2).pack(fill=tk.X)
        rb_txt = tk.Text(rb_code, font=("Consolas", 9), height=5, bg=ModernColors.BG_CARD,
                        fg=ModernColors.TEXT_PRIMARY, relief=tk.FLAT)
        rb_txt.insert("1.0", "def shuffle_string(s, indices)\n  result = Array.new(s.length, '')\n  s.each_char.with_index do |char, i|\n    result[indices[i]] = char\n  end\n  result.join\nend")
        rb_txt.config(state=tk.DISABLED)
        rb_txt.pack(padx=10, pady=5)
    
    def _create_manual_inputs(self):
        for w in self.input_frame.winfo_children(): w.destroy()
        inner = tk.Frame(self.input_frame, bg=ModernColors.BG_CARD)
        inner.pack(pady=10, padx=10)
        
        tk.Label(inner, text="s =", font=("Consolas", 12, "bold"),
                fg=ModernColors.ACCENT_SUCCESS, bg=ModernColors.BG_CARD).pack(side=tk.LEFT, padx=(0,5))
        self.s_entry = tk.Entry(inner, font=("Consolas", 12), width=12,
                               bg=ModernColors.BG_DARK, fg=ModernColors.TEXT_PRIMARY,
                               insertbackground=ModernColors.TEXT_PRIMARY, relief=tk.FLAT)
        self.s_entry.insert(0, "art")
        self.s_entry.pack(side=tk.LEFT, padx=5, ipady=5)
        
        tk.Label(inner, text="indices =", font=("Consolas", 12, "bold"),
                fg=ModernColors.ACCENT_WARNING, bg=ModernColors.BG_CARD).pack(side=tk.LEFT, padx=(15,5))
        self.idx_entry = tk.Entry(inner, font=("Consolas", 12), width=18,
                                 bg=ModernColors.BG_DARK, fg=ModernColors.TEXT_PRIMARY,
                                 insertbackground=ModernColors.TEXT_PRIMARY, relief=tk.FLAT)
        self.idx_entry.insert(0, "1,0,2")
        self.idx_entry.pack(side=tk.LEFT, padx=5, ipady=5)
        
        AnimatedButton(inner, "Run", self._run_manual, color=ModernColors.ACCENT_SUCCESS,
                      width=100, height=38).pack(side=tk.LEFT, padx=15)
        AnimatedButton(inner, "Reset", self._reset, color=ModernColors.ACCENT_WARNING,
                      width=80, height=38).pack(side=tk.LEFT, padx=5)
        
        tk.Label(inner, text="Presets:", font=("Segoe UI", 9),
                fg=ModernColors.TEXT_MUTED, bg=ModernColors.BG_CARD).pack(side=tk.LEFT, padx=(15,5))
        for name, s, idx in [("art->rat", "art", "1,0,2"), ("codeleet", "codeleet", "4,5,6,7,0,2,1,3")]:
            tk.Button(inner, text=name, font=("Segoe UI", 8), bg=ModernColors.CHAR_BOX,
                     fg=ModernColors.TEXT_SECONDARY, relief=tk.FLAT,
                     command=lambda s=s, idx=idx: self._load_preset(s, idx)).pack(side=tk.LEFT, padx=2)
    
    def _create_auto_inputs(self):
        for w in self.input_frame.winfo_children(): w.destroy()
        inner = tk.Frame(self.input_frame, bg=ModernColors.BG_CARD)
        inner.pack(pady=10, padx=10)
        
        tk.Label(inner, text="Enter Original Word:", font=("Segoe UI", 11, "bold"),
                fg=ModernColors.TEXT_PRIMARY, bg=ModernColors.BG_CARD).pack(side=tk.LEFT, padx=(0,10))
        self.word_entry = tk.Entry(inner, font=("Consolas", 14), width=15,
                                  bg=ModernColors.BG_DARK, fg=ModernColors.ACCENT_SUCCESS,
                                  insertbackground=ModernColors.TEXT_PRIMARY, relief=tk.FLAT)
        self.word_entry.insert(0, "mahmoud")
        self.word_entry.pack(side=tk.LEFT, padx=5, ipady=5)
        
        AnimatedButton(inner, "Shuffle & Solve", self._run_auto, color=ModernColors.ACCENT_SUCCESS,
                      width=140, height=38).pack(side=tk.LEFT, padx=15)
        AnimatedButton(inner, "Reset", self._reset, color=ModernColors.ACCENT_WARNING,
                      width=80, height=38).pack(side=tk.LEFT, padx=5)
    
    def _switch_mode(self):
        self.original_word = ""
        self.orig_label.config(text="")
        self.orig_display.config(text="")
        if self.mode_var.get() == "manual":
            self._create_manual_inputs()
            self.inp_label.config(text="INPUT STRING (s)")
        else:
            self._create_auto_inputs()
            self.inp_label.config(text="Click 'Shuffle & Solve' to start")
        self._clear_all()
    
    def _load_preset(self, s, idx):
        self.s_entry.delete(0, tk.END)
        self.s_entry.insert(0, s)
        self.idx_entry.delete(0, tk.END)
        self.idx_entry.insert(0, idx)
        self._run_manual()
    
    def _run_manual(self):
        try:
            self.original_word = ""
            self.input_string = self.s_entry.get().strip()
            self.indices = [int(x.strip()) for x in self.idx_entry.get().split(",")]
            if len(self.input_string) != len(self.indices):
                self.status.config(text="Error: s and indices must have same length!", fg=ModernColors.ACCENT_ERROR)
                return
            self.orig_label.config(text="")
            self.orig_display.config(text="")
            self.inp_label.config(text=f"INPUT: s = \"{self.input_string}\", indices = {self.indices}")
            self._setup_display()
            self._animate_threaded()
        except Exception as e:
            self.status.config(text=f"Error: {e}", fg=ModernColors.ACCENT_ERROR)
    
    def _run_auto(self):
        word = self.word_entry.get().strip()
        if not word or len(word) > 12:
            self.status.config(text="Enter word (max 12 chars)!", fg=ModernColors.ACCENT_ERROR)
            return
        
        self.original_word = word
        n = len(word)
        self.indices = list(range(n))
        random.shuffle(self.indices)
        
        # shuffled[i] = original[indices[i]] so that result[indices[i]] = shuffled[i] = original[indices[i]]
        self.input_string = ''.join(word[self.indices[i]] for i in range(n))
        
        self.orig_label.config(text="ORIGINAL WORD (Goal - what algorithms should return):")
        self.orig_display.config(text=f'"{word}"')
        self.inp_label.config(text=f"SHUFFLED STRING (s) - indices = {self.indices}")
        
        self._setup_display()
        self.status.config(text=f"Reconstructing '{word}' from '{self.input_string}'...", fg=ModernColors.ACCENT_PRIMARY)
        self._animate_threaded()
    
    def _setup_display(self):
        for w in self.source_frame.winfo_children(): w.destroy()
        for w in self.python_frame.winfo_children(): w.destroy()
        for w in self.ruby_frame.winfo_children(): w.destroy()
        
        self.source_chars = []
        self.python_slots = []
        self.ruby_slots = []
        
        for i, ch in enumerate(self.input_string):
            src = SourceCharacter(self.source_frame, ch, i, self.indices[i])
            src.pack(side=tk.LEFT, padx=2)
            self.source_chars.append(src)
        
        for i in range(len(self.input_string)):
            ps = CharacterSlot(self.python_frame, index=i, lang_color=ModernColors.SLOT_PYTHON)
            ps.pack(side=tk.LEFT, padx=2)
            self.python_slots.append(ps)
            
            rs = CharacterSlot(self.ruby_frame, index=i, lang_color=ModernColors.SLOT_RUBY)
            rs.pack(side=tk.LEFT, padx=2)
            self.ruby_slots.append(rs)
        
        # Clear logs
        self.python_log.config(state=tk.NORMAL)
        self.python_log.delete("1.0", tk.END)
        self.python_log.insert("1.0", "# Python execution:\nresult = [''] * len(s)\n\n")
        self.python_log.config(state=tk.DISABLED)
        
        self.ruby_log.config(state=tk.NORMAL)
        self.ruby_log.delete("1.0", tk.END)
        self.ruby_log.insert("1.0", "# Ruby execution:\nresult = Array.new(s.length, '')\n\n")
        self.ruby_log.config(state=tk.DISABLED)
        
        self.python_result.config(text="")
        self.ruby_result.config(text="")
    
    def _animate_threaded(self):
        if self.is_animating: return
        self.is_animating = True
        threading.Thread(target=self._animate, daemon=True).start()
    
    def _animate(self):
        result = [''] * len(self.input_string)
        
        for i, ch in enumerate(self.input_string):
            if not self.is_animating: break
            
            target = self.indices[i]
            result[target] = ch
            
            # Update UI
            self.after(0, lambda i=i: self.source_chars[i].set_processed(True))
            self.after(0, lambda t=target, c=ch: self.python_slots[t].set_char(c, highlight=True))
            self.after(0, lambda t=target, c=ch: self.ruby_slots[t].set_char(c, highlight=True))
            
            # Update logs
            py_log_line = f"# i={i}: result[indices[{i}]] = result[{target}] = '{ch}'\n"
            rb_log_line = f"# i={i}: result[indices[{i}]] = result[{target}] = '{ch}'\n"
            
            self.after(0, lambda line=py_log_line: self._append_log(self.python_log, line))
            self.after(0, lambda line=rb_log_line: self._append_log(self.ruby_log, line))
            
            self.after(0, lambda i=i, ch=ch, t=target: self.status.config(
                text=f"Step {i+1}: s[{i}]='{ch}' -> result[{t}]='{ch}'",
                fg=ModernColors.ACCENT_PRIMARY))
            
            time.sleep(0.5)
            
            self.after(0, lambda t=target, c=ch: self.python_slots[t].set_char(c, highlight=False))
            self.after(0, lambda t=target, c=ch: self.ruby_slots[t].set_char(c, highlight=False))
        
        final = ''.join(result)
        
        # Final log entries
        self.after(0, lambda: self._append_log(self.python_log, f"\n# return ''.join(result)\n# Output: \"{final}\""))
        self.after(0, lambda: self._append_log(self.ruby_log, f"\n# result.join\n# Output: \"{final}\""))
        
        if self.original_word and final == self.original_word:
            msg = f"SUCCESS! Both algorithms restored: '{final}'"
        else:
            msg = f"Complete! Output: '{final}'"
        
        self.after(0, lambda: self.status.config(text=msg, fg=ModernColors.ACCENT_SUCCESS))
        self.after(0, lambda: self.python_result.config(text=f'Output: "{final}"'))
        self.after(0, lambda: self.ruby_result.config(text=f'Output: "{final}"'))
        
        self.is_animating = False
    
    def _append_log(self, log_widget, text):
        log_widget.config(state=tk.NORMAL)
        log_widget.insert(tk.END, text)
        log_widget.see(tk.END)
        log_widget.config(state=tk.DISABLED)
    
    def _clear_all(self):
        for w in self.source_frame.winfo_children(): w.destroy()
        for w in self.python_frame.winfo_children(): w.destroy()
        for w in self.ruby_frame.winfo_children(): w.destroy()
        self.source_chars = []
        self.python_slots = []
        self.ruby_slots = []
        self.python_result.config(text="")
        self.ruby_result.config(text="")
        self.python_log.config(state=tk.NORMAL)
        self.python_log.delete("1.0", tk.END)
        self.python_log.config(state=tk.DISABLED)
        self.ruby_log.config(state=tk.NORMAL)
        self.ruby_log.delete("1.0", tk.END)
        self.ruby_log.config(state=tk.DISABLED)
    
    def _reset(self):
        self.is_animating = False
        for s in self.source_chars: s.set_processed(False)
        for s in self.python_slots: s.clear()
        for s in self.ruby_slots: s.clear()
        self.python_result.config(text="")
        self.ruby_result.config(text="")
        self.python_log.config(state=tk.NORMAL)
        self.python_log.delete("1.0", tk.END)
        self.python_log.config(state=tk.DISABLED)
        self.ruby_log.config(state=tk.NORMAL)
        self.ruby_log.delete("1.0", tk.END)
        self.ruby_log.config(state=tk.DISABLED)
        self.status.config(text="Reset!", fg=ModernColors.ACCENT_PRIMARY)


if __name__ == "__main__":
    app = StringShuffleVisualizer()
    app.update_idletasks()
    x = (app.winfo_screenwidth() // 2) - 700
    y = (app.winfo_screenheight() // 2) - 475
    app.geometry(f"+{x}+{y}")
    app.mainloop()
