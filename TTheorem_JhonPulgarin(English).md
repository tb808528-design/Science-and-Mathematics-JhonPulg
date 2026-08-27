# JHON PULGARIN'S THEOREM
Treatise on Spatial Discontinuity and Zero

**Author:** Jhon Pulgarin
**Villavicencio, Meta - Colombia**
**August 27, 2026**

### Jhon Pulgarin Theorem
Treatise on Spatial Discontinuity and the Architectural Zero

**1. Introduction and Historical Context: A Centuries-Old Problem**
The contradiction between abstract counting and physical reality is not a modern confusion. It is a logical dilemma with centuries of history that affects how humans organize time, space, and information. The main origin of this conflict lies in the historical difficulty of accepting and integrating the concept of 'zero' as a physical entity and not just a mathematical one.
The clearest example is found in our current calendar. The chronological system goes directly from year 1 Before Christ (B.C.) to year 1 Anno Domini (A.D.). Physically, 'year zero' never existed in official history. This causes that, when calculating the time elapsed between 1 B.C. and 1 A.D., pure mathematics dictates a distance of 2 units, when in the real timeline there is only a change of era with no year in between.

**2. The Logical Discrepancy: Mathematicians vs. Programmers**
This historical gap has provoked a classic debate in science and technology, dividing logic into two well-defined sides:
*   **The Pure Mathematical Approach:** Mathematicians operate under a continuous number line where zero is indispensable.
*   **The Programming and Engineering Approach:** Software developers and engineers constantly collide with this through the famous 'Fencepost Error' or zero-based indexing problems.

**3. Case Study: The Elevator Dilemma**
A person lives on floor 2 and his garage is in basement 1. How many floors separate his house from his parking space?

### OFFICIAL FORMULA

**O = |index(A) - index(B)| - 1**

Where:
- O = Number of things IN BETWEEN A and B, not counting A or B.
- index(A) = Position of the first element
- index(B) = Position of the second element
- | | = Absolute value
- -1 = Because subtracting indices counts one extreme, minus one corrects everything

**THIS IS THE FORMULA THAT REPLACES ALL PREVIOUS ONES.**

**4. FORMAL STATEMENT OF THE THEOREM**
Given two distinct positions A and B with indices index(A) and index(B), the number of strictly intermediate elements between them is equal to:
**O = |index(A) - index(B)| - 1**

**5. PROOF (QED)**
1. The absolute distance between indices is: D = |index(A) - index(B)|
2. D includes the distance from A to B inclusive.
3. To count ONLY the interior, we must exclude the extremes A and B. We subtract 1.
4. Result: O = D - 1 = |index(A) - index(B)| - 1
5. QED

Properties:
- If A and B are consecutive: O = 0
- If A = B: O = -1 (empty interval by definition)
- Symmetric: O(A,B) = O(B,A) thanks to absolute value
- Works in any order

**6. COMPLETE EXAMPLES**
**1. Elevator Problem P2 to S1:** A=2, B=-1 -> D=|2-(-1)|=3, O=2 (Floor 1 and Ground Floor)
**2. Pots Problem:** Pots 1 to 5 -> D=|1-5|=4, O=3 (Pots 2, 3 and 4)
**3. Years Problem 1 B.C. and 1 A.D.:** A=-1, B=1 -> D=2, O=1 (Year 0, which historically does not exist, so real O=0)

**Python Script:**
```python
def intermediates(A, B):
    D = abs(A - B)
    O = D - 1
    return D, O

# 1. ELEVATOR: Floor 2 to S1
D1, O1 = intermediates(2, -1)
print(f"Elevator 2 to S1 -> D={D1}, O={O1}")

# 2. POTS: Pot 1 to 5
D2, O2 = intermediates(1, 5)
print(f"Pots 1 to 5 -> D={D2}, O={O2}")

# 3. YEARS: 1 B.C. (-1) to 1 A.D. (1)
D3, O3 = intermediates(-1, 1)
print(f"Years -1 to 1 -> D={D3}, O={O3} (year 0 does not exist, real O=0)")

**7. APPLICATIONS OF THE THEOREM**

1. Data structures and Arrays
2. Linked lists
3. Theory of open intervals and sets
4. Combinatorial counting and Sequence analysis
5. Programming (solves Fencepost Error)
6. Organization of time and space
7. Civil Engineering and Architecture

**8. FINAL CONCLUSION**

Pulgarin's Theorem is highly useful because it transforms a visual counting problem, which usually generates confusion and errors, into an exact and universal mathematical formula (O = D - 1). Its applicability is scalable, it works the same for counting pots as for calculating the intermediate levels of a 100-story building.

Furthermore, it proves to be a fundamental and transversal tool, used by civil engineers, architects and programmers as a logical basis to optimize structural calculations and to program automated systems such as an elevator route.

---
**Jhon Pulgarin - 2026**
**Villavicencio, Meta - Colombia**

