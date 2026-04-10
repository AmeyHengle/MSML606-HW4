"""
report_input_types.py

measures how input type (random, sorted, reversed, repeated) affects
runtime and memory for both algorithms. run from the same directory as Homework4.py
paste the printed output into the report for the input type effects section.
"""

import random
import time
import tracemalloc
import sys
from Homework4 import Homework4

sys.setrecursionlimit(200000)

# note: quicksort degenerates badly on repeated values (approaches O(n^2))
# n=5000 keeps repeated-values runs from taking minutes on slower machines
N = 5_000
hw = Homework4()


def measure(sortFn, arr):
    arrCopy = arr.copy()
    tracemalloc.start()
    start = time.perf_counter()
    try:
        sortFn(arrCopy)
        elapsed = time.perf_counter() - start
        _, peakMem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return round(elapsed, 4), round(peakMem / 1e6, 3), None
    except RecursionError:
        elapsed = time.perf_counter() - start
        _, peakMem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return round(elapsed, 4), round(peakMem / 1e6, 3), "RecursionError"
    except Exception as e:
        tracemalloc.stop()
        return None, None, str(e)


def buildInputs(n):
    random.seed(0)
    base = [round(random.uniform(-1000, 1000), 2) for _ in range(n)]
    return {
        "random order":    base,
        "already sorted":  sorted(base),
        "reverse sorted":  sorted(base, reverse=True),
        "repeated values": [round(random.choice([-10.5, -3.3, 0.0, 3.3, 10.5]), 2) for _ in range(n)],
    }


inputs = buildInputs(N)

print("=" * 80)
print(f"INPUT TYPE EFFECT ON PERFORMANCE  (N = {N:,})")
print("=" * 80)
print(f"{'Input Type':<20}  {'QS Time(s)':>12}  {'QS Mem(MB)':>12}  {'HS Time(s)':>12}  {'HS Mem(MB)':>12}  Notes")
print("-" * 80)

for inputType, arr in inputs.items():
    qsTime, qsMem, qsErr = measure(hw.randomQuickSort, arr)
    hsTime, hsMem, hsErr = measure(hw.heapSort, arr)

    note = " | ".join(filter(None, [qsErr, hsErr])) or "ok"

    qsT = f"{qsTime:.4f}" if qsTime is not None else "n/a"
    hsT = f"{hsTime:.4f}" if hsTime is not None else "n/a"
    qsM = f"{qsMem:.3f}"  if qsMem  is not None else "n/a"
    hsM = f"{hsMem:.3f}"  if hsMem  is not None else "n/a"

    print(f"{inputType:<20}  {qsT:>12}  {qsM:>12}  {hsT:>12}  {hsM:>12}  {note}")

print("=" * 80)
print("\nKEY ANOMALY: quicksort is significantly slower on repeated values")
print("  this is because lomuto partition puts all equal elements on one side,")
print("  causing maximally unbalanced splits — degenerate O(n^2) behavior")
print("  heapsort is unaffected since it does not depend on pivot selection")
print("\nNOTE: paste this table into the report for the input type effects section")
