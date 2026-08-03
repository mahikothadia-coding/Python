setx = {"green" , "blue"}
sety = {"blue" , "yellow"}
setz = setx.intersection(sety)
setu = setx.union(sety)
setv = setx.difference(sety)
setw = sety.difference(setx)
setz = setx.symmetric_difference(sety)
print(setz)
print(setu)
print(setv)
print(setw)
print(setz)
