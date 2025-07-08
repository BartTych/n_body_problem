import pickle
from infinity import infinity_principle
from matplotlib import pyplot as plt

x, y, steps = pickle.load(open('fitting_test_0.pkl', 'rb'))
#x = x[::-1]

x_inf, y_inf = infinity_principle.cal_pos_with_infinity_principle(x, y, steps)


plt.scatter(x, y, s = 0.3)
plt.scatter(x_inf,y_inf,c='r',s = 0.3)
plt.show()