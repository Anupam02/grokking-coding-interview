# Two Pointers Technique

## Overview
The two pointers technique is an efficient algorithmic approach that uses two references (pointers) to traverse a data structure (usually an array or linked list). These pointers move at different speeds or directions to solve problems in a single or multiple passes, typically reducing time complexity from O(n²) to O(n).

## Core Concept
Instead of using nested loops that lead to quadratic time complexity, we use two pointers that:
- Start from different positions (beginning and end, or both from start)
- Move towards each other or in the same direction
- Stop when they meet or reach the end
- Compare or manipulate elements based on certain conditions

## Common Problem Types

### 1. **Array/String Manipulation**
   - **Move Zeroes**: Reorder array by moving all zeros to the end
   - **Remove Duplicates**: Keep unique elements and shrink array size
   - **Remove Element**: Remove all instances of a specific value
   - **Reverse String/Array**: Reverse elements in-place
   - **Palindrome Validation**: Check if array/string reads the same forwards and backwards

### 2. **Sorted Array Problems**
   - **Two Sum**: Find two numbers that add up to a target value
   - **Three Sum**: Find all unique triplets that sum to zero
   - **Valid Triangle**: Count valid triangle combinations
   - **Container With Most Water**: Find max area between two lines

### 3. **Merge/Combine Operations**
   - **Merge Sorted Arrays**: Combine two sorted arrays into one
   - **Merge Sorted List**: Combine two sorted linked lists
   - **Intersection of Arrays**: Find common elements between arrays
   - **Union of Arrays**: Combine unique elements from multiple arrays

### 4. **Linked List Problems**
   - **Detect Cycle**: Find if a cycle exists in linked list
   - **Find Cycle Start**: Locate where the cycle begins
   - **Middle of Linked List**: Find the middle element
   - **Remove Nth Node**: Delete a specific node from linked list

### 5. **Partition/Rearrangement**
   - **Sort Colors**: Arrange elements in specific order (0s, 1s, 2s)
   - **Dutch National Flag**: Partition array into three sections
   - **Move Negatives**: Move negative numbers to one side
   - **Separate by Parity**: Group even and odd numbers

## Time & Space Complexity
- **Time Complexity**: O(n) - Linear, typically a single or double pass
- **Space Complexity**: O(1) - Constant, modifications done in-place

## When to Use Two Pointers
✓ Problem involves a sorted or partially sorted array
✓ Need to compare/swap elements at different positions
✓ Want to reduce nested loops to avoid O(n²) complexity
✓ Need to find a pair/triplet with specific properties
✓ Dealing with array rearrangement or partitioning

## Key Patterns

### Pattern 1: Opposite Directions
```
left = 0, right = n-1
while left < right:
    if condition: left += 1
    else: right -= 1
```

### Pattern 2: Same Direction
```
left = 0, right = 0
while right < n:
    if condition: left += 1
    right += 1
```

### Pattern 3: Sliding Window
```
left = 0
for right in range(n):
    while condition: left += 1
    # Process window
```

## Solutions in This Directory
- [Move Zeroes](move-zeroes/solution.py) - Reorder array to move all zeros to the end

