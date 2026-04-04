# Python3: Mutable, Immutable... Everything Is Object

![Python objects illustration](https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=1200&q=80)

## Introduction

One of the most important ideas in Python is that everything is an object. Integers, strings, lists, tuples, functions, and even classes are all objects with an identity, a type, and a value. This matters because Python variables do not directly store raw values the way many beginners first imagine. Instead, variables are names bound to objects. Once that idea is clear, a lot of Python behavior stops looking random and starts looking consistent.

For example:

```python
a = 1
b = a
a = 2
print(b)
```

```text
1
```

Here, `a` is rebound to a new integer object, while `b` still refers to the original `1`. Compare that with a mutable object:

```python
l1 = [1, 2, 3]
l2 = l1
l1[0] = "X"
print(l2)
```

```text
['X', 2, 3]
```

Both variables point to the same list object, so mutating that object through one name is visible through the other. That difference is the core of this project.

## `id` and `type`

Every Python object has an identity and a type. The identity can be inspected with `id()`, and the type can be inspected with `type()`. In CPython, the identity commonly matches the memory address of the object.

```python
x = 89
print(type(x))
print(id(x))
```

```text
<class 'int'>
140390176881968
```

The exact number printed by `id()` changes from run to run, but the point is that it identifies the object currently referenced by `x`. If two variables point to the same object, their `id()` values match:

```python
s1 = "Best School"
s2 = s1
print(id(s1) == id(s2))
print(s1 is s2)
```

```text
True
True
```

The operator `is` checks whether two variables refer to the same object, while `==` checks whether their values are equal.

```python
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)
print(l1 is l2)
```

```text
True
False
```

The lists contain the same values, but they are different objects.

## Mutable Objects

A mutable object can be changed after it is created. Common built-in mutable types include lists, dictionaries, and sets. Mutability means an object can keep the same identity while its internal state changes.

```python
l = [1, 2, 3]
print(id(l))
l.append(4)
print(id(l))
print(l)
```

```text
140390175104832
140390175104832
[1, 2, 3, 4]
```

The `id()` stays the same because `append()` mutates the existing list instead of creating a new one.

This also explains aliasing:

```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l1)
print(l2)
print(l1 is l2)
```

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
True
```

Both names point to one mutable object. A change through one alias affects the same object seen through the other alias.

## Immutable Objects

An immutable object cannot be changed after creation. Common built-in immutable types include integers, floats, strings, booleans, and tuples. With immutable objects, what looks like a modification is actually the creation of a new object and the rebinding of a variable name.

```python
n = 3
print(id(n))
n += 1
print(id(n))
print(n)
```

```text
140390176879120
140390176879152
4
```

The value changes, but the identity changes too, because `n += 1` for an integer creates a new integer object.

Strings behave the same way:

```python
s = "Holberton"
print(id(s))
s = s + " School"
print(id(s))
print(s)
```

```text
140390175168880
140390175173424
Holberton School
```

Tuples are also immutable, although they can contain mutable objects inside them:

```python
t = ([1, 2], 3)
t[0].append(4)
print(t)
```

```text
([1, 2, 4], 3)
```

The tuple itself is immutable, so its slots cannot be reassigned, but one of its elements is a list, and that list remains mutable. This is an important nuance: an immutable container can still reference mutable objects.

## Why This Matters, and How Python Treats Mutable and Immutable Objects Differently

This distinction matters because it affects assignment, comparison, side effects, and debugging. With immutable objects, rebinding a variable does not affect other variables that used to reference the same object. With mutable objects, in-place changes are visible through every alias to that object.

Compare these two examples:

```python
a = 89
b = a
a = a + 1
print(a)
print(b)
```

```text
90
89
```

Now with a list:

```python
a = [1, 2, 3]
b = a
a += [4]
print(a)
print(b)
```

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

For lists, `+=` mutates the existing object in place. But this similar-looking code does something different:

```python
a = [1, 2, 3]
b = a
a = a + [4]
print(a)
print(b)
print(a is b)
```

```text
[1, 2, 3, 4]
[1, 2, 3]
False
```

Here, `a = a + [4]` builds a new list and rebinds `a`, leaving `b` attached to the old list. That is exactly why understanding mutation versus rebinding is critical in Python.

## How Arguments Are Passed to Functions, and What That Implies for Mutable and Immutable Objects

Python passes arguments by object reference. A function receives a reference to the same object, but the local parameter name is separate from the caller’s variable name. That means mutating a mutable argument inside a function affects the caller’s object, while rebinding the parameter inside the function does not.

Immutable example:

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

```text
1
```

The function parameter `n` is rebound to a new integer object locally. The caller’s `a` still points to the original integer.

Mutable example:

```python
def add_item(items):
    items.append(4)

l = [1, 2, 3]
add_item(l)
print(l)
```

```text
[1, 2, 3, 4]
```

The list itself is mutated, so the change is visible outside the function.

Rebinding a parameter does not replace the caller’s object:

```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

```text
[1, 2, 3]
```

Inside the function, `n` is only reassigned locally. The original `l1` in the caller is unchanged.

## Conclusion

The biggest lesson from this project is that variables in Python are names bound to objects, not containers that directly hold raw values. Once you understand object identity, equality, mutability, aliasing, and the difference between mutation and rebinding, many behaviors that seem strange at first become predictable. `is` checks identity, `==` checks value, mutable objects can be changed in place, immutable objects cannot, and function arguments follow the same reference model. This is one of the foundations of writing correct Python code and avoiding unintended side effects in larger programs.

## URLs

- Blog post URL: `ADD_YOUR_MEDIUM_OR_LINKEDIN_ARTICLE_URL_HERE`
- LinkedIn share URL: `ADD_YOUR_LINKEDIN_POST_URL_HERE`
