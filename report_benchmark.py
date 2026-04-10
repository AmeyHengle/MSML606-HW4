"""
report_benchmark.py

measures runtime and memory of both sorting algorithms across increasing input sizes.
paste the printed output into the report for the performance comparison section.
run this from the same directory as Homework4.py
"""

import random
import time
import tracemalloc
import sys
from Homework4 import Homework4

sys.setrecursionlimit(200000)

INPUT_SIZES = [10_000, 50_000, 100_000, 500_000, 1_000_000]
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
    except MemoryError:
        tracemalloc.stop()
        return None, None, "MemoryError"


print("=" * 85)
print("PERFORMANCE BENCHMARK — RANDOMIZED QUICKSORT VS HEAPSORT")
print("=" * 85)
print(f"{'N':>10}  {'QS Time(s)':>12}  {'QS Mem(MB)':>12}  {'HS Time(s)':>12}  {'HS Mem(MB)':>12}  {'Notes'}")
print("-" * 85)

for n in INPUT_SIZES:
    random.seed(42)
    arr = [random.uniform(-n, n) for _ in range(n)]

    qsTime, qsMem, qsErr = measure(hw.randomQuickSort, arr)
    hsTime, hsMem, hsErr = measure(hw.heapSort, arr)

    note = " | ".join(filter(None, [qsErr, hsErr])) or "ok"

    qsT = f"{qsTime:.4f}" if qsTime is not None else "n/a"
    hsT = f"{hsTime:.4f}" if hsTime is not None else "n/a"
    qsM = f"{qsMem:.3f}"  if qsMem  is not None else "n/a"
    hsM = f"{hsMem:.3f}"  if hsMem  is not None else "n/a"

    print(f"{n:>10}  {qsT:>12}  {qsM:>12}  {hsT:>12}  {hsM:>12}  {note}")

print("=" * 85)
print("\nNOTE: paste this table directly into the report performance section")
