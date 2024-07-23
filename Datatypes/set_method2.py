company = {'Infosys','ICICI bank','TCS','Bajaj'}
add_company = {'SBI','TATA consultancy','Infosys','TCS'}

# Union method
union_method = company.union(add_company)
print('Union method will return all the element in both set:',union_method)
print()

union_method = company | add_company
print('Union Operator:',union_method)
print()

intersection_method = company.intersection(add_company)   # using operator for intersection &
print('Intersection method will return Common Element:',intersection_method)
print()

difference_method = company.difference(add_company)
print('Difference method:',difference_method)