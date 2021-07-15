#Pizza Slice Helper
#by Alan Tran 
num_pizza=input('How many pies of pizza are there?')
slices_per_pizza=input('How many slices does each pie have?')
total_slice=int(num_pizza)*int(slices_per_pizza)
people=input('How many people are there?')
slice_per_person=int(total_slice)//int(people)
leftover=int(total_slice)%int(people)
print(f'Each person can have {slice_per_person} slices.')
print(f'There will be {leftover} slices left over')
