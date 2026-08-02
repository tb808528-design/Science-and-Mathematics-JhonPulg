# Science-and-Mathematics-JhonPulg / Rule of 3
#Calculating rule of 3 with inputs in 4-step, The example I’ll give will be with popsicles.
# 3 popsicles (A), cost 45 pesos (B), 7 popsicles (C) ¿how much do they cost? (D) = 105$3




# Step 1; Define the variables
def Rule_of_3():
    print("Rule of 3: A / B = C / D")
    print("Leave empty the one you want to calculate and press enter.") #No pongas para calcular.



# Step 2; Ask for input
A = input("A = ")
B = input("B = ")
C = input("C = ")
D = input("D = ")

# Step 3; Convert to Float if it's not empty, if = Nome
A = float(A) if A else None
B = float(B) if B else None
C = float(C) if C else None
D = float(D) if D else None

# Step 4; Calculate the missing one
if A is None:
    A = (B * C) / D
    print(f"The number of popsicles is = {A}")
    
elif B is None:
    B = (A * D) / C
    print(f"The cost of popsicles is = {B} pesos")
elif C is None:
    C = (A * D) // B 
    print(f"The number of popsicles is = {C}")
elif D is None:
    D = (B * C) / A
    print(f"The cost of popsicles is = {D} pesos")
else:
    print("No need to calculate, you have all the variables")
    
    
    
Rule_of_3()
