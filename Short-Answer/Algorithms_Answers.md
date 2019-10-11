#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) `while(a < n*n*n):` O(n^3)

   `a = a + n*n` O(n^2)

   Final Runtime: O(n) - O(n^3) is reduced by O(n^2) incrementing inside the loop

b) `for i in range(n):` O(n)

   `while j < n:` would be O(n) again but...

   `j *= 2` we have doubling so its O(log(n))

   Final Runtime: O(n log(n)) - since the loops are nested O(n) and O(log(n)) are multiplied together

c) `return 2 + bunnyEars(bunnies-1)` O(n)

   Final Runtime: O(n) - We only ever decrement bunnies at a rate of 1 per function call (effectively a basic for loop) 

## Exercise II

1) Drop an egg from the middle floor

2) If the egg didn't break, move up halfway between your current position and the top floor

   If it did break, move down halfway between your current position and the bottom floor

3) Repeat step 2 until you find the floor which is the break/non-break point

This is an implementation of binary search so the complexity is O(log(n))

In reality, this is an egg dropping which means it's going to break on the bottom floor and time is O(1), don't drop eggs.
