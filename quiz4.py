#!/usr/bin/python3
"""

"""

from coopr.pyomo import *

xindx = [1, 2, 3]

# Concrete Model
model = ConcreteModel(name="Maximum Profit for Bed Construction")

# Decision Variable
model.x = Var(xindx, within=NonNegativeReals)

# Objective Function
model.obj = Objective(expr= 10 * model.x[1] + 60 * model.x[2] + 80 * model.x[3] <= 450 +
                            15 * model.x[1] + 20 * model.x[2] + 40 * model.x[3] <= 210 +
                             5 * model.x[1] + 15 * model.x[2] + 20 * model.x[3] <= 95 +
                                                   model.x[2] <= 45, sense=maximize)

# Constraints
model.MaterialConstraint = Constraint(expr=model.x[1] + model.x[2] + model.x[3] <= 450)
model.LaborConstraint = Constraint(expr=model.x[1] + model.x[2] + model.x[3] <= 210)
model.SpecLaborConstraint = Constraint(expr=model.x[1] + model.x[2] + model.x[3] <= 95)
model.MaxBedBUnits = Constraint(expr=model.x[2] <= 45)



