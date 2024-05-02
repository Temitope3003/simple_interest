def calculate_simple_interest(principal,rate,time):
  interest = (principal * rate * time)/100
  return interest


print(calculate_simple_interest(1000,5,2))