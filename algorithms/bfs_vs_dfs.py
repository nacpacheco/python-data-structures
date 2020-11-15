# # If you know a solution is not far from the root of the tree:
# BFS, it starts searching the closets nodes to the root first

# # If the tree is very deep and solutions are rare: 
# BFS, because DFS will take longer with this tree since its very deep,
# watch out for memory

# # If the tree is very wide:
# DFS, because BFS will use too much memory because it has to keep track
# of the nodes in the same leve, so wider the tree bigger the memory use

# # If solutions are frequent but located deep in the tree:
# DFS, because it goes deep first

# # Determining whether a path exists between two nodes:
# DFS

# # Finding the shortest path:
# BFS