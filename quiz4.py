#!/usr/bin/python3
"""
Question 1 from quiz4.  This program will find the appropriate number of beds
of type A, B, C to make to maximize the profit of the bed manufacture.
"""

from pyomo.environ import *


N = 3  # Number of products
products = range(1, N+1)  # list of indices for decision var
IndxProd = 2  # index of Bed with limit (B)
ProdLimit = 45  # limit of Bed B
numprod = range(N)

Prices = [250, 320, 625]
MPrice = {"Products"[i] : Prices[i] for i in numprod}

M = 2  # Number of requirements to make bed
Material = range(1, M+1)
nummat = range(M)

# Avaliable Material and Labor
Cap = [450, 210, 95]
AvailMat = {"Material"[i] : Cap[i] for i in nummat}

# Requirements to make beds
Req = [[10, 15, 5],
       [60, 20, 15],
       [80, 40, 20]]
ReqMat = {("Products"[i], "Material"[i]) : Req[i][j] for j in nummat for i in numprod}

# Concrete Model
model = ConcreteModel(name="Maximum Profit for Bed Construction")

# Decision Variables
model.Prod = Var(products, within=NonNegativeReals)

# Capacity Constraints
def CapacityRule(model, p):
    """
    This function has the Pyomo model as the first positional
    parameter,
    and a material requirement index as a second positional
    parameter
    """
    return sum(ReqMat[i,p] * model.Prod[i] for i in products) <= AvailMat[p]

# Generate one constraint for each material type
model.Capacity = Constraint(Material, rule=CapacityRule)

# Production Constraint since we can only build so many 'B' Beds
model.ProdRestriction = Constraint(expr=model.Prod[IndxProd] <= ProdLimit)


#!/usr/bin/python3
"""
Question 2 from quiz4. This program will model the unbalanced problem.
"""

from coopr.pyomo import *

supply_points = 2
demand_points = 4  # Really 3, but with 1 dummy point to address Supply exceeding demand

a = range(1, supply_points+1)
a1 = range(supply_points)
b = range(1, demand_points+1)
b1 = range(demand_points)

# Index list for decision variables x
xindx = [(a[i], b[j]) for j in b1 for i in a1]

# Concrete Model
model = ConcreteModel(name="Quiz Question 2, Unbalanced Problem")

# Decision Variables
model.x = Var(xindx, winthin=NonNegativeReals)

# The objective function
model.obj = Objective(expr=25*model.x[1, 1] + 45*model.x[1, 2] + 42*model.x[1, 3] +
                           20*model.x[2, 1] + 60*model.x[2, 2] + 50*model.x[2, 3],
                          sense=minimize)

# Supply Constraints
model.SConstraint1 = Constraint(expr=model.x[1, 1] + model.x[1, 2] + model.x[1, 3] + model.x[1, 4] <= 85)
model.SConstraint2 = Constraint(expr=model.x[2, 1] + model.x[2, 2] + model.x[2, 3] + model.x[2, 4] <= 65)

# Demand Constraings
model.DConstraint1 = Constraint(expr=model.x[1, 1] + model.x[2, 1] + model.x[3, 1] <= 35)
model.DConstraint2 = Constraint(expr=model.x[1, 2] + model.x[2, 2] + model.x[3, 2] <= 42)
model.DConstraint3 = Constraint(expr=model.x[1, 3] + model.x[2, 3] + model.x[3, 3] <= 50)
model.DConstraint4 = Constraint(expr=model.x[1, 4] + model.x[2, 4] + model.x[3, 4] <= 50)


#!/usr/bin/python3
"""
Question 3 from quiz4. This program will model the now balanced problem.
"""

from coopr.pyomo import *

supply_points = 2
demand_points = 3

a = range(1, supply_points+1)
a1 = range(supply_points)
b = range(1, demand_points+1)
b1 = range(demand_points)

# Index list for decision variables x
xindx = [(a[i], b[j]) for j in b1 for i in a1]

# Concrete Model
model = ConcreteModel(name="Quiz Question 3, Unbalanced Problem")

# Decision Variables
model.x = Var(xindx, winthin=NonNegativeReals)

# The objective function
model.obj = Objective(expr=48*model.x[1, 1] + 68*model.x[1, 2] + 64*model.x[1, 3] +
                           44*model.x[2, 1] + 83*model.x[2, 2] + 74*model.x[2, 3],
                          sense=minimize)

# Supply Constraints
model.SConstraint1 = Constraint(expr=model.x[1, 1] + model.x[1, 2] + model.x[1, 3] <= 85)
model.SConstraint2 = Constraint(expr=model.x[2, 1] + model.x[2, 2] + model.x[2, 3] <= 65)

# Demand Constraings
model.DConstraint1 = Constraint(expr=model.x[1, 1] + model.x[2, 1] + model.x[3, 1] <= 42)
model.DConstraint2 = Constraint(expr=model.x[1, 2] + model.x[2, 2] + model.x[3, 2] <= 50)
model.DConstraint3 = Constraint(expr=model.x[1, 3] + model.x[2, 3] + model.x[3, 3] <= 58)
