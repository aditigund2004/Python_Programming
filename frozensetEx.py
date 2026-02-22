'''
frozenset ->
is an unorder, hetergeneous immutable(no changeble) elements only, dupilcate are not allowed and indexing not alloed becuase unorderd
syntax
var = frozenset({v1,v2,v3,..})


imutable -> list, set, dict
immmuatble -> tuple, int, float, str, float, complex, fs, bool

order -> dict, list , tuple, str, range
unoederd -> set, fs

duploacte allowed -> list, tuple
not allowed ->set, fs, dictionary
'''


# fs = frozenset({1,2,3,4,5,6,7,8,9,10,'ram',(11,22),11,22,11,22})
# print(type(fs))

# print(fs)

fs1 = frozenset({1,2,3,4,5})
fs2 = frozenset({4,5,6,7,8,9,10})

# (method) def intersection(*s: Iterable[object]) -> frozenset[int]
print(fs1.intersection(fs2))  #frozenset({4, 5})

'''
(method) def difference(*s: Iterable[object]) -> frozenset[int]
Return a new set with elements in the set that are not in the others.
'''
print(fs1.difference(fs2))  #frozenset({1, 2, 3})

print(fs1.copy())
