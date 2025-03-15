def get_prime_factors(number):
  factors=[]
  factor=2
  while factor<=number:
    if (number%factor==0):
      factors.append(factor)
      number=number/factor
    else:
      factor=factor+1
  return factors
      
      

print(get_prime_factors(21))
print(get_prime_factors(2300))  
print(get_prime_factors(347))
print(get_prime_factors(0))