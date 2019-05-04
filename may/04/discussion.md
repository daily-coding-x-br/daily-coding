# Problem 1
 ## Solution using a Hash Set

 Simply go through the array checking if the complementary was already seen. This check can be made in O(1) amorized time using a hash table. The file `p1.py` implements this approach. 

 ## On Hash Sets and C++

 The C++ Hash Set (`unordered_set`) might display poor performance in competitions settings. Because of this, we may 'downgrade' to a O(n log(n)) runtime solution by using the STL's map, or sorting the array and using the 'squeeze' aproach. How to use Hash Tables effectively in C++:

 * Everything about unordered_map: https://codeforces.com/blog/entry/21853

 * C++ STL: Order of magnitude faster hash tables with Policy Based Data Structures: https://codeforces.com/blog/entry/60737
