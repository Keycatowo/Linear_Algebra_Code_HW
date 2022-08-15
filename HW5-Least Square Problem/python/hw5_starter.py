#%% Prepare and Load data
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
#%% 
def hw():
    """
        For given points (1,6), (2,5), (3,7), (4,10)
        Please use least square method to find the cloest sol Ax=b, 
        and we name the sol beta. 
        It's ok to use inverse matrix operation in numpy.
        It not allow to use `np.linalg.lstsq`.
    """
    print("-------hw---------")
    from numpy.linalg import inv
    x = np.array([1,2,3,4])
    y = np.array([6,5,7,10])
    # >>>>> Start of todo
    A = ...
    beta = ...
    # <<<<< End of todo
    y_pred = A @ beta # @ is 2D matrix multipulation.
    print(f"y={beta[0]}x + {beta[1]}")
    print(f'MSE={mean_squared_error(y_pred, y)}')
    
    # Check answer
    np.testing.assert_almost_equal(beta, [1.4,3.5])
    plt.scatter(x, y)
    plt.plot(x, y_pred)
    plt.legend(["True Points", f"y={beta[0]:.2}x+{beta[1]:.2}"])
    plt.show()
    


def demo1():
    """
        It's a demo for realtion between bmi and diabetes target.
        We can plot it and see the equation.
    """
    print("-------demo1---------")
    import seaborn as sns
    from scipy import stats
    
    data = pd.read_csv("../diabetes.csv")
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['bmi'],data['target'])
    ax = sns.regplot(x="bmi", y="target", data=data, color='b', 
        line_kws={'label':"y={0:.1f}x+{1:.1f}".format(slope,intercept)})
    ax.legend()
    plt.title("Demo1")
    plt.show()

def demo2():
    print("-------demo2---------")
    from sklearn.linear_model import LinearRegression
    data = pd.read_csv("../diabetes.csv")
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    lm = LinearRegression().fit(X,y)
    y_pred = lm.predict(X)
    print(f"MSE = {mean_squared_error(y_pred, y)}")
    print("target = ")
    for coef, col in zip(lm.coef_, X.columns):
        if coef >= 0:
            print(f"\t+{coef:.3f} x {col}")
        else:
            print(f"\t {coef:.3f} x {col}")
    
#%%
if __name__ == "__main__":
    ######### HW: 2D points ###########
    hw()

    ######### Demo 1: LS in 1 feature problem ###########
    # It's a demo for realtion between bmi and diabetes target.
    # We can plot it and see the equation.
    demo1()

    ######### Demo 2: LS in n features problem ##########
    # It's a demo for 10 features, and 
    # we use linear regration to find the equation.
    demo2()


# %%
