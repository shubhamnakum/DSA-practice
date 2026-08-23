# Arrays - Medium

This folder contains medium-level array and matrix problems solved in Python. The solutions are organized by problem, and several problems include multiple approaches so their time and space trade-offs can be compared.

## Problems Covered

| Topic | Implementations | Main concepts |
| --- | --- | --- |
| 2 Sum | `2_sum/two_sum_1.py` to `two_sum_3.py` | Brute force, hashing, sorting, two pointers |
| Count subarrays with sum `k` | `count subarray with sum k/subarray_count_1.py` to `subarray_count_3.py` | Nested loops, prefix sum, frequency map |
| Leaders in an array | `leaders/leader_1.py`, `leader_2.py` | Nested scan, right-to-left traversal |
| Longest consecutive sequence | `longest consecutive sequence/lcs_1.py` to `lcs_3.py` | Brute force, sorting, set lookup |
| Majority element | `majority_element_1/majority_element_1.py` to `majority_element_3.py` | Brute force, hashing, Boyer-Moore voting |
| Maximum subarray sum | `max_sub_arrray_sum/max_sum_1.py` to `max_sum_3.py` | Brute force, running sum, Kadane's algorithm |
| Best time to buy and sell stock | `max_sub_arrray_sum/buy_sell_stocks.py` | Minimum-so-far, one-pass scan |
| Next permutation | `next_permutations/next_permutation_1.py` | Pivot, successor, in-place reversal |
| Rearrange by sign | `Rearange_by_sign/rearrange_by_sign_1.py`, `rearrange_by_sign_2.py` | Separate positive and negative values, one-pass placement |
| Rotate a matrix by 90 degrees | `rotate_matrix/rotate_matrix_1.py`, `rotate_matrix_2.py` | Extra matrix, transpose and reverse |
| Set matrix zeroes | `set matrix to zeros/matrix_to_zero_1.py`, `matrix_to_zero_2.py` | Marking, row/column state, in-place update |
| Sort an array of 0s, 1s and 2s | `sort_array_0_1_2s/sort_0s_1s_2s_1.py` to `sort_0s_1s_2s_3.py` | Sorting, counting, Dutch National Flag algorithm |
| Spiral matrix traversal | `spiral matrix/spiral_matrix.py` | Boundary-controlled traversal |

## Approach Progression

Many problem files are numbered from a straightforward solution to a more efficient one:

- `_1`: brute-force or simplest implementation
- `_2`: improved implementation using an additional observation or data structure
- `_3`: optimal or near-optimal implementation where available

This makes the folder useful for studying how an algorithm evolves from a direct solution to an optimized one.

## Complexity Themes

- One-pass scans generally run in `O(n)` time.
- Matrix traversal usually takes `O(rows * columns)` time.
- Hash maps and sets often reduce time to `O(n)` while using `O(n)` extra space.
- In-place approaches aim for `O(1)` auxiliary space, excluding the input itself.
- Sorting-based solutions commonly take `O(n log n)` time.

## Suggested Study Order

1. 2 Sum
2. Leaders in an array
3. Maximum subarray sum and stock profit
4. Majority element
5. Sort 0s, 1s and 2s
6. Longest consecutive sequence
7. Count subarrays with sum `k`
8. Rearrange by sign
9. Next permutation
10. Matrix rotation and set matrix zeroes
11. Spiral matrix traversal

For each topic, first understand the invariant used by the optimal approach, then compare it with the earlier implementations.

## Notes

- The examples are executable Python scripts and generally include sample input at the bottom of each file.
- Some scripts print their answer and some also mutate the input list or matrix in place.
- `set matrix to zeros/matrix_to_zero_2 copy.py` appears to be a copy of the second implementation and is retained as a backup/reference file.
- Folder and file names preserve the current project structure, including names such as `Rearange_by_sign`, `max_sub_arrray_sum`, and `spiral matrix`.
empty file just dumping