# Stack Implementation in Python

This project demonstrates **stack data structure implementations in Python** using different approaches. It includes three Python files that show how stacks work using **classes** and **lists**, along with a task-based example.

---

## 📁 Project Files

### 1. `stacksusingclass.py`

This file implements a stack using a **Python class**.

#### Features:

* `push(element)` – Adds an element to the stack
* `pop()` – Removes and returns the top element
* `peek()` – Returns the top element without removing it
* `isEmpty()` – Checks if the stack is empty
* `size()` – Returns the number of elements in the stack

#### Example Operations:

* Pushes elements `'a'`, `'b'`, `'c'`
* Displays the stack
* Pops the top element
* Checks the top element using `peek`
* Checks if the stack is empty
* Displays the stack size

This file demonstrates **object-oriented programming (OOP)** for stack implementation.

---

### 2. `stacksusinglists.py`

This file implements a stack using a **Python list only**, without classes.

#### Features:

* Uses `append()` for push
* Uses `pop()` for pop
* Accesses the last element for peek
* Uses `len()` to check size
* Uses boolean logic to check if the stack is empty

#### Example Operations:

* Pushes elements `"a"`, `"b"`, `"c"`
* Pops the top element
* Displays the top element using peek
* Checks if the stack is empty
* Displays the size of the stack

⚠️ **Note:**
The line `stack.peek()` will cause an error because lists do not have a `peek()` method.

---

### 3. `task.py`

This file uses a **class-based stack** to perform a sequence of stack operations as part of a task.

#### Features:

* Same stack methods as `stacksusingclass.py`
* Pushes and pops multiple integer values
* Prints the stack after each operation
* Checks stack state using `isEmpty()`

#### Example Operations:

* Pushes elements: `5`, `12`, `7`, `9`, `3`
* Pops elements and prints results
* Uses `peek()` to view the top element
* Checks if the stack is empty at different stages

This file is useful for **step-by-step understanding of stack behavior**.

---

## ▶️ How to Run

Make sure Python is installed, then run any file using:

```bash
python filename.py
```

Example:

```bash
python stacksusingclass.py
```

---

## 📚 Concepts Covered

* Stack data structure (LIFO – Last In, First Out)
* Python lists
* Classes and objects
* Stack operations (push, pop, peek, isEmpty, size)

---

## ✅ Conclusion

This project helps beginners understand stack implementation in Python using both **procedural** and **object-oriented** approaches.