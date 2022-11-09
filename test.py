one_deep_dictionary = {'start here':1,'k1':[1,2,3,{'k2':[1,2,{'k3':['keep going',{'further':[1,2,3,4,[{'k4':'Python'}]]}]}]}]}

test = one_deep_dictionary['k1']
test = test[-1]
test = test['k2']
test = test[-1]
test = test['k3']
test = test[-1]
test = test['further']
test = test[-1]
test = test[0]
test = test['k4']

print(test)