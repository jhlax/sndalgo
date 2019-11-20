import _xenakis as xenakis

# res_params = [(1, 7), (3, 1), (7, 3)]
# res_params = [(1, 3), (3, 7), (7, 1)]
res_params = [(3, 2), (4, 5), (9, 4)]
r1, r2, r3 = (xenakis.Residual(a, b) for a, b in res_params)

sieve = r1 & r2 & r3

print(sieve.modulus, sieve.shift)
