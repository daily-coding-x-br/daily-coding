Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:
<<<<<<< HEAD

=======
```
>>>>>>> 8630924038efaea6a375698304d2c41474c1478a
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
<<<<<<< HEAD
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false
=======
```
`exists(board, "ABCCED")` returns `true`,
`exists(board, "SEE")` returns `true`,
`exists(board, "ABCB")` returns `false`.
>>>>>>> 8630924038efaea6a375698304d2c41474c1478a
