# Tower of Hanoi
Algorithmic Thinking
* the stacking technique in Python
> [!NOTE]
>In Python, a stack is a data structure that follows the Last-In, First-Out (LIFO) principle. The two fundamental operations are:
* Push: Adding an element to the top of the stack.
* Pop: Removing the topmost element from the stack.
Using a List as a Stack
Python's built-in list can be used as a stack, where:
.append() is used to push elements.
.pop() is used to remove elements from the top.

> [!IMPORTANT]
> Solver function [here](https://github.com/hainguyen1511/tower-of-Hanoi/blob/main/full%20tower%20hanoi.txt) will have repetitive steps that we could shrink down by recursive thinking

> [!WARNING]
>The Tower of Hanoi is a classic mathematical puzzle that follows a set of recursive rules. The objective is to move a stack of disks from one peg to another, following these constraints:

> [!WARNING]
> Rules:
You can only move one disk at a time.
A disk must always be placed on top of another larger disk, never on a smaller one.
You can use a temporary peg to store disks while moving them.

> [!WARNING]
> Recursive Solution:
To solve the puzzle with n disks:
Move n-1 disks from the source peg to the auxiliary peg.
Move the largest disk directly to the destination peg.
Move the n-1 disks from the auxiliary peg to the destination peg.

[![Watch the video](https://github.com/user-attachments/assets/a38a7bf4-98f6-4045-9ae0-0ce5045f5d2b)](https://youtu.be/rf6uf3jNjbo?si=faxTwA2x6dNK_1lz)
