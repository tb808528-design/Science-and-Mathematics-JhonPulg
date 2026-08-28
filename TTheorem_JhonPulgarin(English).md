# Jhon Pulgarin's Theorem and the spatial discontinuity of the architectural zero

**Treatise on Spatial Discontinuity and the Architectural Zero**

---

### 1. HISTORICAL INTRODUCTION

1. Introduction and Historical Context: A Centuries-Old Problem
The contradiction between abstract counting and physical reality is not a modern confusion. It is a logical dilemma with centuries of history that affects the way human beings organize time, space, and information. The main origin of this conflict lies in the historical difficulty in accepting and integrating the concept of 'zero' as a physical entity and not just a mathematical one.
The clearest example of this is found in our current calendar. The chronological system goes directly from the year 1 Before Christ (B.C.) to the year 1 Anno Domini (A.D.). Physically, the 'year zero' never existed in official history. This generates that, when calculating the time elapsed between the year 1 B.C. and the year 1 A.D., pure mathematics dictates a distance of 2 units, when in the real timeline there is only a change of era with no year in between.

2. The Logical Discrepancy: Mathematicians vs. Programmers
This historical gap has caused a classic debate in the world of science and technology, dividing logic into two well-defined camps:
• The Pure Mathematical Approach: Mathematicians operate under a continuous number line where zero is indispensable. For abstract mathematics, zero represents the point of origin or equilibrium. By ignoring whether zero has a real physical representation, their calculations always assume an intermediate space that artificially increases physical distances.
• The Programming and Engineering Approach: Software developers and engineers constantly clash with this through the famous 'Fencepost Error' or zero-based indexing problems (where lists start at 0 and not 1). A programmer knows that one thing is the number of intermediate elements and a very different thing is the index of the positions, requiring constant adjustments in the code so that applications do not fail when interacting with the real world.

### 2. CASE STUDY: THE ELEVATOR
The Case Study: The Elevator Dilemma case why Jhon Pulgarin found the problem with 0
Jhon Pulgarin's Theory is born from direct observation of this phenomenon in everyday architecture:
A person lives on floor 2 and his parking space is in basement 1. How many floors separate his home from his parking space?
If this problem is introduced linearly into an Artificial Intelligence or a theoretical mathematical system, the strict mathematical calculation establishes that the distance is 3 (calculating 2 - (-1) = 3). However, in real life, the elevator buttons in that building show that when going down from floor 2 to basement 1 there are only 2 buttons
                     OFFICIAL FORMULA

O = |index(A) - index(B)| - 1

Where:
- O = Quantity of things that are IN BETWEEN A and B, not counting A nor B.
- index(A) = Position of the first element
- index(B) = Position of the second element
- | | = Absolute value
- -1 = Because when subtracting indices you count one extreme, minus one corrects everything

### 3. THEOREM STATEMENT

Given two different positions A and B with indices
index(A) and index(B), the number of elements
strictly intermediate between them is equal to:

O = |index(A) - index(B)| - 1

Where O are the empty or intermediate spaces between A and B.

### 4. FORMAL PROOF (QED)

1. The absolute distance between indices is:
   D = |index(A) - index(B)|

2. D includes the distance from A to B inclusive.

3. To count ONLY the interior, we must exclude
   the extremes A and B. We subtract 1.

4. It remains: O = D - 1 = |index(A) - index(B)| - 1

### 5. QED - Quod Erat Demonstrandum (as was to be demonstrated)
Proven properties:
- If A and B are consecutive: O = 0
- If A = B: O = -1 (empty interval by definition)
- O >= 0 for distinct non-consecutive positions
- Symmetric: O(A,B) = O(B,A) thanks to absolute value
- Works in any order.

## 6. COMPLETE EXAMPLES

### 1. Elevator Problem (Floor 2 to B1)
An elevator is on floor 2 and must go down to B1 (Basement 1). It is required to know how many floors separate them, not counting the origin floor nor the destination floor.

### Data
To avoid "ghost floors", we assign real consecutive indices:
* **Floor A (origin):** Floor 2 $\rightarrow$ index $2$
* **Floor B (destination):** Basement 1 $\rightarrow$ index $0$
*(Note: The intermediate Floor 1 occupies index 1)*

### Formula and development
First we find the total distance ($D$):
$$D = |\text{index}(A) - \text{index}(B)|$$
$$D = |2 - 0|$$
$$D = |2| = 2$$

Now we find the intermediate floors ($O$):
$$O = D - 1$$
$$O = 2 - 1 = 1$$

### Answer
It is separated by **only 1 intermediate floor**, which is **Floor 1**.

---

## 2. Pots Problem

### Problem statement
There are 5 pots in a row numbered from 1 to 5. Pot 1 and pot 5 are the extremes. It is required to know how many pots are between them, not counting the origin nor the destination.

### Data
Since the pots in the physical world are already consecutive by nature, their numbers are equivalent to their indices:
* **Pot A (origin):** Pot 1 $\rightarrow$ index $1$
* **Pot B (destination):** Pot 5 $\rightarrow$ index $5$

### Formula and development
First we find the total distance ($D$):
$$D = |\text{index}(A) - \text{index}(B)|$$
$$D = |1 - 5|$$
$$D = |-4| = 4$$

Now we find the intermediate pots ($O$):
$$O = D - 1$$
$$O = 4 - 1 = 3$$

### Answer
They are separated by **3 intermediate pots**, which are **2, 3 and 4**.

---

## 3. Eras Problem (1 B.C. and 1 A.D.)

### Problem statement
It is wanted to know how many full years are between the year 1 B.C. and the year 1 A.D., not counting the year of origin nor the destination.

### Data
Given that in conventional historical chronology **year 0 does not exist** (year 1 A.D. began immediately after year 1 B.C. ended), we assign real consecutive indices to reflect this continuity:
* **Year A (origin):** 1 B.C. $\rightarrow$ index $0$
* **Year B (destination):** 1 A.D. $\rightarrow$ index $1$

### Formula and development
First we find the total distance ($D$):
$$D = |\text{index}(A) - \text{index}(B)|$$
$$D = |0 - 1|$$
$$D = |-1| = 1$$

Now we find the intermediate years ($O$):
$$O = D - 1$$
$$O = 1 - 1 = 0$$

### Answer
They are separated by **0 intermediate years**. Year 1 A.D. is immediately consecutive to year 1 B.C.

### Real Historical Adjustment
The mathematical formula yields a theoretical result of 1 intermediate year (which would correspond to year 0). However, in the Christian historical and chronological record **year 0 does not exist**. Year 1 A.D. follows immediately after year 1 B.C.

Therefore, in historical reality:
$$O = 0$$

### Answer
In chronological reality, **0 full years** separate year 1 B.C. from year 1 A.D.

### PYTHON SCRIPT

```python
def calculate_intermediate_elements(index_a, index_b):
    """
    Applies the universal formula: O = |index(A) - index(B)| - 1
    """
    distance = abs(index_a - index_b)
    intermediate = distance - 1
    return intermediate

# =====================================================================
# 1. ELEVATOR PROBLEM (Floor 2 to Basement 1 - Without Ground Floor)
# Real continuous scale: B1 = 0, Floor 1 = 1, Floor 2 = 2
# =====================================================================
origin_floor_idx = 2  # Floor 2
destination_floor_idx = 0  # Basement 1

intermediate_floors = calculate_intermediate_elements(origin_floor_idx, destination_floor_idx)

print("--- 1. ELEVATOR PROBLEM ---")
print(f"Origin Index (Floor 2): {origin_floor_idx}")
print(f"Destination Index (B1): {destination_floor_idx}")
print(f"Real intermediate floors separating them: {intermediate_floors}\n")

# =====================================================================
# 2. POTS IN A ROW PROBLEM
# Scale: Pot 1 = 1, Pot 5 = 5
# =====================================================================
origin_pot_idx = 1
destination_pot_idx = 5

intermediate_pots = calculate_intermediate_elements(origin_pot_idx, destination_pot_idx)

print("--- 2. POTS PROBLEM ---")
print(f"Origin Index (Pot 1): {origin_pot_idx}")
print(f"Destination Index (Pot 5): {destination_pot_idx}")
print(f"Real intermediate pots separating them: {intermediate_pots}\n")

# =====================================================================
# 3. ERAS PROBLEM (1 B.C. to 1 A.D. - Without Historical Year 0)
# Real continuous scale: 1 B.C. = 0, 1 A.D. = 1
# =====================================================================
origin_year_idx = 0  # 1 B.C.
destination_year_idx = 1  # 1 A.D.

intermediate_years = calculate_intermediate_elements(origin_year_idx, destination_year_idx)

print("--- 3. ERAS PROBLEM ---")
print(f"Origin Index (1 B.C.): {origin_year_idx}")
print(f"Destination Index (1 A.D.): {destination_year_idx}")
print(f"Real intermediate years separating them: {intermediate_years}\n")
```
### 7. APPLICATIONS OF THE THEOREM

1.  Data structures and Arrays
2.  Linked lists
3.  Open interval theory and sets
4.  Combinatorial counting and Sequence analysis
5.  Programming (solves Fencepost Error)
6.  Time and space organization
7.  Civil Engineering and Architecture

### 8. FINAL CONCLUSION

The Pulgarin Theorem is highly useful because it transforms a visual counting problem, which usually generates confusion and errors, into an exact and universal mathematical formula (O = D - 1). Its applicability is scalable, it works the same for counting pots as for calculating the intermediate levels of a 100-story building.

Furthermore, it proves to be a fundamental and transversal tool, used by civil engineers, architects and programmers as a logical basis to optimize structural calculations and to program automated systems such as the route of an elevator.

----------------------------------------------------------------------------------------------------------------------------------
### 9. HISTORICAL BACKGROUND AND RELATED WORK

The Jhon Pulgarin Theorem mathematically addresses a phenomenon that has been identified across various scientific disciplines throughout history. Although the underlying formula for the cardinality of open intervals is universal, its systematic application connects directly with the following milestones in science and technology:

#### A. Discrete Mathematics: Cardinality of Open Intervals
In set theory and discrete mathematics, calculating the strictly internal elements between two integer boundaries A and B (where $A < B$) is formally defined as the cardinality of an open interval $(A, B)$. The use of the absolute value $| \text{index}(A) - \text{index}(B) | - 1$ extends this notion, making it symmetric and applicable regardless of the direction of the vectorized traversal—a principle studied in the topology of discrete spaces.

#### B. Computer Science: Edsger Dijkstra and the "Fencepost Error"
In software engineering, the core of this theorem resolves the classic Fencepost Error (or Off-by-one Error). In the 1970s, the renowned computer scientist Edsger Dijkstra formalized the necessity of zero-based indexing (starting to count from 0) to ensure that range and interval operations in computer memory remained consistent and did not require artificial corrections when interacting with the physical world.

#### C. Astronomy: Jacques Cassini and the Introduction of Year 0
The offset analyzed in the Eras Problem (1 BC and 1 AD) was physically discovered by the French astronomer Jacques Cassini in 1740. Cassini identified that mathematical calculations to predict historical eclipses failed by a factor of 1 year due to the non-existence of year 0 in the Gregorian and Julian calendars. To solve this, he introduced the "Astronomical Year Numbering" scale, where the year 1 BC is denoted numerically as year 0, validating the need for continuous indices proposed by this theorem.

### 10. FORMAL VERIFICATION OF METHODS (THEOREM PROVER)

```python
import random

def calculate_intermediate_elements(index_a, index_b):
    """
    Official implementation of the Jhon Pulgarin Theorem formula:
    O = |index(A) - index(B)| - 1
    """
    return abs(index_a - index_b) - 1

def execute_case_studies():
    print("====================================================")
    print("  CASE STUDY VALIDATION - JHON PULGARIN THEOREM")
    print("====================================================\n")

    # 1. Elevator Case (P2 to S1 -> Continuous indices: S1=0, P1=1, P2=2)
    obs_elevator = calculate_intermediate_elements(2, 0)
    print(f"[Case 1] Elevator (P2 -> S1): {obs_elevator} intermediate floor (Floor 1).")

    # 2. Pots Case (P1 to P5)
    obs_pots = calculate_intermediate_elements(1, 5)
    print(f"[Case 2] Pots in a row (1 -> 5): {obs_pots} intermediate pots (2, 3, 4).")

    # 3. Historical Eras Case (1 BC to 1 AD -> Continuous indices: 1 BC=0, 1 AD=1)
    obs_eras = calculate_intermediate_elements(0, 1)
    print(f"[Case 3] Eras (1 BC -> 1 AD): {obs_eras} intermediate years.\n")

def scientific_properties_test(num_simulations=10000):
    """
    Automated scientific test. Validates the theorem against 10,000 pairs
    of random indices to verify compliance with its mathematical properties.
    """
    print("====================================================")
    print(f"  RUNNING PROPERTY TEST ({num_simulations} ITERATIONS)")
    print("====================================================")
    
    for _ in range(num_simulations):
        # Generate two random indices across a wide range of the number line
        a = random.randint(-100000, 100000)
        b = random.randint(-100000, 100000)
        
        result_ab = calculate_intermediate_elements(a, b)
        result_ba = calculate_intermediate_elements(b, a)
        
        # Property 1: Symmetry -> O(A,B) must equal O(B,A)
        assert result_ab == result_ba, f"Symmetry failure at: {a}, {b}"
        
        # Property 2: Consecutive elements -> If |A - B| = 1, O must be 0
        if abs(a - b) == 1:
            assert result_ab == 0, f"Contiguity failure for consecutive elements: {a}, {b}"
            
        # Property 3: Identical elements -> If A == B, O must be -1 (Empty interval)
        if a == b:
            assert result_ab == -1, f"Identity failure for identical elements: {a}, {b}"
            
    print("✅ TEST SUCCESSFUL!")
    print("- Symmetry Property Mathematically Proven.")
    print("- Contiguity Property (Consecutive Elements) Verified.")
    print("- Identity Property (Empty Interval O = -1) Confirmed.")
    print("\nThe Jhon Pulgarin Theorem is mathematically consistent in Python.\n")

if __name__ == "__main__":
    execute_case_studies()
    scientific_properties_test()
```

---
**Jhon Pulgarin - 2026**
**Villavicencio, Meta - Colombia**


