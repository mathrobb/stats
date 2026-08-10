
# coding: utf-8

# In[ ]:

import numpy
import scipy.stats as stats
from datascience import *
import matplotlib.pyplot as plots
import matplotlib.pyplot as plt
plots.style.use('fivethirtyeight')
import numpy as np
import scipy.stats as stats
import scipy

import ipywidgets as widgets

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

import matplotlib.pyplot as plt

import numpy as np


def biasdemo1():    
    np.random.seed(15)
    Population = np.random.normal(15000,500,100000)
    PopSigma = np.round(np.std(Population),0)

    Biased = make_array()
    Unbiased=make_array()

    reps = 200000

    for i in np.arange(reps):
        Sample = np.random.choice(Population, 3)
        Biased = np.append(Biased, np.std(Sample))
        Unbiased = np.append(Unbiased, stats.tstd(Sample))

    biasedmean = np.round(np.mean(Biased),0)
    unbiasedmean = np.round(np.mean(Unbiased),0)
    
    plots.figure(figsize=(12,6))
    plots.suptitle("Biased = Bad, Unbiased = Good")

    plots.subplot(1,2,1)
    plots.hist(Biased)
    plots.scatter(PopSigma, -3, marker="^", zorder=5, s=80, color='green')
    plots.scatter(np.mean(Biased),-3, marker = "s", zorder=5, s=80, color='red')
    plots.title("Biased Estimator of Sigma")
    plots.text(710, 0.1*reps, f"Estimator = {biasedmean}", color='red')
    plots.text(710, 0.085*reps,f"True Value = {PopSigma}", color='green');

    plots.subplot(1,2,2)
    plots.hist(Unbiased)
    plots.scatter(PopSigma, -3, marker="^", zorder=5, s=80, color='green')
    plots.scatter(np.mean(Unbiased),-3, marker = "s", zorder=5, s=80, color='red')
    plots.title("Unbiased Estimator of Sigma")
    plots.text(710,  0.1*reps, f"Estimator = {unbiasedmean}", color='red')
    plots.text(710,  0.085*reps,f"True Value = {PopSigma}", color='green');
    
    
def biasdemo2():
    np.random.seed(15)
    Population = np.random.normal(15,5,100000)
    PopSigma = np.round(np.std(Population),3)

    Biased = make_array()
    Unbiased=make_array()

    reps = 100000

    for i in np.arange(reps):
        Sample = np.random.choice(Population, 8)
        Biased = np.append(Biased, np.std(Sample))
        Unbiased = np.append(Unbiased, stats.tstd(Sample))

    biasedmean = np.round(np.mean(Biased),3)
    unbiasedmean = np.round(np.mean(Unbiased),3)
    
    plots.figure(figsize=(12,6))
    plots.suptitle("Biased = Bad, Unbiased = Good")

    plots.subplot(1,2,1)
    plots.hist(Biased)
    plots.scatter(PopSigma, -3, marker="^", zorder=5, s=80, color='green')
    plots.scatter(biasedmean,-3, marker = "s", zorder=5, s=80, color='red')
    plots.title("Biased Estimator of Sigma")
    plots.text(7, 0.1*reps, f"Estimator = {biasedmean}", color='red')
    plots.text(7, 0.085*reps,f"True Value = {PopSigma}", color='green');

    plots.subplot(1,2,2)
    plots.hist(Unbiased)
    plots.scatter(PopSigma, -3, marker="^", zorder=5, s=80, color='green')
    plots.scatter(unbiasedmean,-3, marker = "s", zorder=5, s=80, color='red')
    plots.title("Unbiased Estimator of Sigma")
    plots.text(7, 0.1*reps, f"Estimator = {unbiasedmean}", color='red')
    plots.text(7, 0.085*reps,f"True Value = {PopSigma}", color='green');
    

def empirical_rule_demo():
    x = np.arange(-3.5, 3.5, 0.05)
    y = stats.norm.pdf(x, 0, 1)

    plots.figure(figsize = (13, 8.5))

    plots.suptitle("The Empirical Rule", weight = "bold", size = 'xx-large')
    
    plots.subplot(2, 3, 2)
    plots.plot(x, y)
    plots.fill_between(x,y, where =abs(x)<1, color="red")
    plots.text(-0.45, .15, "68%", color="white", weight="bold", size='large')
    plots.title("Within 1 Standard Deviation of mean")

    plots.subplot(2, 3, 4)
    plots.plot(x, y)
    plots.fill_between(x,y, where =abs(x)<=2, color="red")
    plots.text(-0.55, .15, "95%", color="white", weight="bold", size="large")
    plots.title("Within 2 Standard Deviations of mean")

    plots.subplot(2, 3, 6)
    plots.plot(x, y)
    plots.fill_between(x,y, where =abs(x)<3, color="red")
    plots.text(-0.85, .15, "99.7%", color="white", weight="bold", size="large")
    plots.title("Within 3 Standard Deviations of mean");
    

def sampling_distribution_demo1(): 
    
    x1 = np.linspace(0.0, 25.0, num=500)

    x2 = make_array()
    for i in np.arange(1000):
        x2 = np.append(x2, np.mean(x1[np.random.choice(len(x1), 5)]))

    x3 = make_array()
    for i in np.arange(1000):
        x3 = np.append(x3, np.mean(x1[np.random.choice(len(x1), 10)]))
    
    x4 = make_array()
    for i in np.arange(1000):
        x4 = np.append(x4, np.mean(x1[np.random.choice(len(x1), 15)]))
    
    x5 = make_array()
    for i in np.arange(1000):
        x5 = np.append(x5, np.mean(x1[np.random.choice(len(x1), 20)]))

    x6 = make_array()
    for i in np.arange(1000):
        x6 = np.append(x6, np.mean(x1[np.random.choice(len(x1), 30)]))

    
    plt.figure(figsize = (14, 8))

    plt.suptitle("Various Sampling Distributions", weight="bold", size='xx-large')

    plt.subplot(2, 3, 1)
    plt.hist(x1)
    plt.title('Uniform Original Population')


    plt.subplot(2, 3, 2)
    plt.hist(x2, density=True)
    mu, sigma = scipy.stats.norm.fit(x2)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x2),max(x2)), mu, sigma)
    plt.plot(np.linspace(min(x2),max(x2)), best_fit_line)
    plt.title("Samples of size 5")

    plt.subplot(2, 3, 3)
    plt.hist(x3, density=True)
    mu, sigma = scipy.stats.norm.fit(x3)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x3),max(x3)), mu, sigma)
    plt.plot(np.linspace(min(x3),max(x3)), best_fit_line)
    plt.title("Samples of size 10")

    plt.subplot(2, 3, 4)
    plt.hist(x4, density=True)
    mu, sigma = scipy.stats.norm.fit(x4)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x4),max(x4)), mu, sigma)
    plt.plot(np.linspace(min(x4),max(x4)), best_fit_line)
    plt.xlabel('Samples of size 15')

    plt.subplot(2, 3, 5)
    plt.hist(x5, density=True)
    mu, sigma = scipy.stats.norm.fit(x5)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x5),max(x5)), mu, sigma)
    plt.plot(np.linspace(min(x5),max(x5)), best_fit_line)

    plt.xlabel('Samples of size 20')

    plt.subplot(2, 3, 6)
    plt.hist(x6, density=True)
    mu, sigma = scipy.stats.norm.fit(x6)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x6),max(x6)), mu, sigma)
    plt.plot(np.linspace(min(x6),max(x6)), best_fit_line)

    plt.xlabel("Samples of size 30")

    plt.show()


    
    
    
def sampling_distribution_demo2():
    x0 = np.linspace(0.0, 25.0, num=500)

    x1 = np.cos(2 * np.pi * x0) 

    x2 = make_array()
    for i in np.arange(1000):
        x2 = np.append(x2, np.mean(x1[np.random.choice(len(x1), 3)]))

    x3 = make_array()
    for i in np.arange(1000):
        x3 = np.append(x3, np.mean(x1[np.random.choice(len(x1), 10)]))
    
    x4 = make_array()
    for i in np.arange(1000):
        x4 = np.append(x4, np.mean(x1[np.random.choice(len(x1), 15)]))
    
    x5 = make_array()
    for i in np.arange(1000):
        x5 = np.append(x5, np.mean(x1[np.random.choice(len(x1), 20)]))

    x6 = make_array()
    for i in np.arange(1000):
        x6 = np.append(x6, np.mean(x1[np.random.choice(len(x1), 30)]))
    

    plt.figure(figsize = (14, 8))

    plt.suptitle("Various Sampling Distributions", weight="bold", size='xx-large')

    plt.subplot(2, 3, 1)
    plt.hist(x1)
    plt.title('Non-Uniform Original Population')


    plt.subplot(2, 3, 2)
    plt.hist(x2, density=True)
    mu, sigma = scipy.stats.norm.fit(x2)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x2),max(x2)), mu, sigma)
    plt.plot(np.linspace(min(x2),max(x2)), best_fit_line)
    plt.title("Samples of size 3")

    plt.subplot(2, 3, 3)
    plt.hist(x3, density=True)
    mu, sigma = scipy.stats.norm.fit(x3)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x3),max(x3)), mu, sigma)
    plt.plot(np.linspace(min(x3),max(x3)), best_fit_line)
    plt.title("Samples of size 10")

    plt.subplot(2, 3, 4)
    plt.hist(x4, density=True)
    mu, sigma = scipy.stats.norm.fit(x4)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x4),max(x4)), mu, sigma)
    plt.plot(np.linspace(min(x4),max(x4)), best_fit_line)
    plt.xlabel('n = 15')

    plt.subplot(2, 3, 5)
    plt.hist(x5, density=True)
    mu, sigma = scipy.stats.norm.fit(x5)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x5),max(x5)), mu, sigma)
    plt.plot(np.linspace(min(x5),max(x5)), best_fit_line)

    plt.xlabel('Samples of size 20')

    plt.subplot(2, 3, 6)
    plt.hist(x6, density=True)
    mu, sigma = scipy.stats.norm.fit(x6)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x6),max(x6)), mu, sigma)
    plt.plot(np.linspace(min(x6),max(x6)), best_fit_line)

    plt.xlabel("Samples of size 30")


    plt.show()



def sampling_distribution_demo3():
    x1 = np.random.geometric(p=0.3, size=10000)

    x2 = make_array()
    for i in np.arange(1000):
        x2 = np.append(x2, np.mean(x1[np.random.choice(len(x1), 3)]))

    x3 = make_array()
    for i in np.arange(1000):
        x3 = np.append(x3, np.mean(x1[np.random.choice(len(x1), 10)]))
    
    x4 = make_array()
    for i in np.arange(1000):
        x4 = np.append(x4, np.mean(x1[np.random.choice(len(x1), 15)]))
    
    x5 = make_array()
    for i in np.arange(1000):
        x5 = np.append(x5, np.mean(x1[np.random.choice(len(x1), 35)]))

    x6 = make_array()
    for i in np.arange(1000):
        x6 = np.append(x6, np.mean(x1[np.random.choice(len(x1), 100)]))
    

    plt.figure(figsize = (14, 8))

    plt.suptitle("Various Sampling Distributions", weight="bold", size='xx-large')

    plt.subplot(2, 3, 1)
    plt.hist(x1)
    plt.title('Non-Symmetric Original Population')


    plt.subplot(2, 3, 2)
    plt.hist(x2, density=True)
    mu, sigma = scipy.stats.norm.fit(x2)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x2),max(x2)), mu, sigma)
    plt.plot(np.linspace(min(x2),max(x2)), best_fit_line)
    plt.title("Samples of size 3")

    plt.subplot(2, 3, 3)
    plt.hist(x3, density=True)
    mu, sigma = scipy.stats.norm.fit(x3)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x3),max(x3)), mu, sigma)
    plt.plot(np.linspace(min(x3),max(x3)), best_fit_line)
    plt.title("Samples of size 10")

    plt.subplot(2, 3, 4)
    plt.hist(x4, density=True)
    mu, sigma = scipy.stats.norm.fit(x4)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x4),max(x4)), mu, sigma)
    plt.plot(np.linspace(min(x4),max(x4)), best_fit_line)
    plt.xlabel('Samples of size 15')

    plt.subplot(2, 3, 5)
    plt.hist(x5, density=True)
    mu, sigma = scipy.stats.norm.fit(x5)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x5),max(x5)), mu, sigma)
    plt.plot(np.linspace(min(x5),max(x5)), best_fit_line)

    plt.xlabel('Samples of size 35')

    plt.subplot(2, 3, 6)
    plt.hist(x6, density=True)
    mu, sigma = scipy.stats.norm.fit(x6)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x6),max(x6)), mu, sigma)
    plt.plot(np.linspace(min(x6),max(x6)), best_fit_line)

    plt.xlabel("Samples of size 100")

    plt.show()

    
def sampling_distribution_demo4():
    x1 = np.random.normal(100, 15, size=10000)

    x2 = make_array()
    for i in np.arange(1000):
        x2 = np.append(x2, np.mean(x1[np.random.choice(len(x1), 3)]))

    x3 = make_array()
    for i in np.arange(1000):
        x3 = np.append(x3, np.mean(x1[np.random.choice(len(x1), 5)]))
    
    x4 = make_array()
    for i in np.arange(1000):
        x4 = np.append(x4, np.mean(x1[np.random.choice(len(x1), 10)]))
    
    x5 = make_array()
    for i in np.arange(1000):
        x5 = np.append(x5, np.mean(x1[np.random.choice(len(x1), 25)]))

    x6 = make_array()
    for i in np.arange(1000):
        x6 = np.append(x6, np.mean(x1[np.random.choice(len(x1), 50)]))
    

    plt.figure(figsize = (14, 8))

    plt.suptitle("Various Sampling Distributions", weight="bold", size='xx-large')
    
    plt.subplot(2, 3, 1)
    plt.hist(x1, density=True)
    mu, sigma = scipy.stats.norm.fit(x1)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x1),max(x1)), mu, sigma)
    plt.plot(np.linspace(min(x1),max(x1)), best_fit_line)
    plt.title('Original Population')


    plt.subplot(2, 3, 2)
    plt.hist(x2, density=True)
    mu, sigma = scipy.stats.norm.fit(x2)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x2),max(x2)), mu, sigma)
    plt.plot(np.linspace(min(x2),max(x2)), best_fit_line)
    plt.title("Samples of size 3")

    plt.subplot(2, 3, 3)
    plt.hist(x3, density=True)
    mu, sigma = scipy.stats.norm.fit(x3)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x3),max(x3)), mu, sigma)
    plt.plot(np.linspace(min(x3),max(x3)), best_fit_line)
    plt.title("Samples of size 5")

    plt.subplot(2, 3, 4)
    plt.hist(x4, density=True)
    mu, sigma = scipy.stats.norm.fit(x4)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x4),max(x4)), mu, sigma)
    plt.plot(np.linspace(min(x4),max(x4)), best_fit_line)
    plt.xlabel('Samples of size 10', size="large")

    plt.subplot(2, 3, 5)
    plt.hist(x5, density=True)
    mu, sigma = scipy.stats.norm.fit(x5)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x5),max(x5)), mu, sigma)
    plt.plot(np.linspace(min(x5),max(x5)), best_fit_line)

    plt.xlabel('Samples of size 25', size="large")

    plt.subplot(2, 3, 6)
    plt.hist(x6, density=True)
    mu, sigma = scipy.stats.norm.fit(x6)
    best_fit_line = scipy.stats.norm.pdf(np.linspace(min(x6),max(x6)), mu, sigma)
    plt.plot(np.linspace(min(x6),max(x6)), best_fit_line)

    plt.xlabel("Samples of size 50", size="large")

    plt.show()
    

# Some functions for plotting. You don't have to understand how any
# of the functions in this cell work, since they use things we 
# haven't learned about in Data 8.


def resize_window(lim=3.5):
    plots.xlim(-lim, lim)
    plots.ylim(-lim, lim)
    
def draw_line(slope=0, intercept=0, x=make_array(-4, 4), color='r'):
    y = x*slope + intercept
    plots.plot(x, y, color=color)
    
def draw_vertical_line(x_position, color='black'):
    x = make_array(x_position, x_position)
    y = make_array(-4, 4)
    plots.plot(x, y, color=color)
    
def make_correlated_data(r):
    x = np.random.normal(0, 1, 1000)
    z = np.random.normal(0, 1, 1000)
    y = r*x + (np.sqrt(1-r**2))*z
    return x, y

def r_scatter(r):
    """Generate a scatter plot with a correlation approximately r"""
    plots.figure(figsize=(5,5))
    x, y = make_correlated_data(r)
    plots.scatter(x, y, color='darkblue', s=20)
    plots.xlim(-4, 4)
    plots.ylim(-4, 4)
    
def r_table(r):
    """
    Generate a table of 1000 data points with a correlation approximately r
    """
    np.random.seed(8)
    x, y = make_correlated_data(r)
    return Table().with_columns('x', x, 'y', y)
    
    
def correlation_demo():

    table1 = r_table(-1)
    table2 = r_table(-0.8)
    table3 = r_table(-0.2)
    table4 = r_table(0)
    table5 = r_table(0.5)
    table6 = r_table(0.9)

    plots.figure(figsize = (14, 8))

    plots.suptitle("Various Correlations", weight="bold", size='xx-large')

    plots.subplot(2, 3, 1)
    plots.scatter(table1.column("x"),table1.column("y"), color="darkblue")
    plots.title('r near -1')

    plots.subplot(2, 3, 2)
    plots.scatter(table2.column("x"),table2.column("y"), color="darkblue")
    plots.title('r near -0.8')

    plots.subplot(2, 3, 3)
    plots.scatter(table3.column("x"),table3.column("y"), color="darkblue")
    plots.title('r near -0.2')

    plots.subplot(2, 3, 4)
    plots.scatter(table4.column("x"),table4.column("y"), color="darkblue")
    plots.title('r near 0')

    plots.subplot(2, 3, 5)
    plots.scatter(table5.column("x"),table5.column("y"), color="darkblue")
    plots.title('r near 0.5')

    plots.subplot(2, 3, 6)
    plots.scatter(table6.column("x"),table6.column("y"), color="darkblue")
    plots.title('r near 0.9')

    plots.show()


def residual_demo():
    x = make_array(1,2,3,4)
    y = make_array(1.5, 3, 2, 3)

    plots.figure(figsize = (16, 5))

    plots.subplot(1, 3, 1)
    plots.scatter(x, y,s=80, zorder=10)
    plots.title("The Scatterplot")
    plots.xticks(np.arange(1,5), np.arange(1,5))
    plots.xlim(.5,4.2);

    plots.subplot(1, 3, 2)
    plots.scatter(x, y,s=80, zorder=10)
    plots.plot([0,4],[1.5,1.5+0.35*4], color='black')
    plots.title("Adding in the Regression Line")
    plots.xticks(np.arange(1,5), np.arange(1,5))
    plots.xlim(.5,4.2);

    plots.subplot(1, 3, 3)
    plots.scatter(x, y,s=80, zorder=10)
    plots.plot([0,4],[1.5,1.5+0.35*4], color='black')
    plots.plot([1,1],[1.5,1.85], color='red')
    plots.plot([2,2],[1.5+.7,3], color='red')
    plots.plot([3,3],[2,1.5+3*0.35], color='red')
    plots.plot([4,4],[2.9,3], color='red')
    plots.text(1.1, 1.65,"$e_1 = -0.35$")
    plots.text(1, 2.6, "$e_2 = 0.80$")
    plots.text(3.15, 2.25,"$e_3 = -0.55$")
    plots.text(3,2.9, "$e_4 = 0.10$")
    plots.title("Showing the Residuals")
    plots.xticks(np.arange(1,5), np.arange(1,5))
    plots.xlim(.5,4.2);

    
    
def line_demo():
    xx = make_array(1,2,3,4)
    yy = make_array(1.5, 3, 2, 3)


    def plot_func(slope, intercept):
        x = np.linspace(0, 5)
        y = x*slope + intercept
        plt.scatter(xx,yy, s=50)
        plt.ylim(-1,6)
        plt.xlim(0,5)
        plt.plot([1,1],[1.5,slope+intercept], color="red")
        plt.plot([2,2],[3, 2*slope+intercept], color ='red')
        plt.plot([3,3],[2, 3*slope+intercept], color ='red')
        plt.plot([4,4],[3, 4*slope+intercept], color="red")
        rmse = np.round(((1.5-slope-intercept)**2 + 
                         (3-2*slope-intercept)**2 + 
                         (2-3*slope-intercept)**2 + 
                         (3-4*slope-intercept)**2)**0.5, 3)
        plt.plot(x, y)
        plt.text(1,5, f"RMSE = {rmse}", color="red", size='large')

    interact(plot_func, slope = widgets.FloatSlider(value=.35, min=-1, max=1.0, step=0.15), 
             intercept=widgets.FloatSlider(value=1.5, min=-1, max=2.5, step=0.1));
    
    
def anscombe1():
    anscombe = Table.read_table("anscombe.csv")
    plots.figure(figsize = (12, 11))

    plots.suptitle("Anscombe's Quartet", weight="bold", size="xx-large")

    plots.subplot(2,2,1)
    plots.scatter(anscombe.column('x1'),anscombe.column('y1'))
    #plots.text(10, 6, "$\hat{y}= 0.5x+3$\n$r = 0.816$")
    #plots.plot([4,14],[5,12])
    plots.title("I");


    plots.subplot(2,2,2)
    plots.scatter(anscombe.column('x2'),anscombe.column('y2'))
    #plots.text(10, 6, "$\hat{y}= 0.5x+3$\n$r = 0.816$")
    #plots.plot([4,14],[5,12])
    plots.title("II");

    plots.subplot(2,2,3)
    plots.scatter(anscombe.column('x3'),anscombe.column('y3'))
    #plots.text(10, 6, "$\hat{y}= 0.5x+3$\n$r = 0.816$")
    #plots.plot([4,14],[5,12])
    plots.title("III");

    plots.subplot(2,2,4)
    plots.scatter(anscombe.column('x4'),anscombe.column('y4'))
    #plots.text(10, 6, "$\hat{y}= 0.5x+3$\n$r = 0.816$")
    #plots.plot([8,19],[7,12.5])
    plots.title("IV");

    plots.show();

def anscombe2():
    plots.figure(figsize = (12, 11))
    anscombe = Table.read_table("anscombe.csv")

    plots.suptitle("Anscombe's Quartet\nwith Regression Lines", weight="bold", size="xx-large")

    plots.subplot(2,2,1)
    plots.scatter(anscombe.column('x1'),anscombe.column('y1'))
    plots.text(10, 6, "$\hat{y}= 0.5x+3$\n$r = 0.816$")
    plots.plot([4,14],[5,12])
    plots.title("I");


    plots.subplot(2,2,2)
    plots.scatter(anscombe.column('x2'),anscombe.column('y2'))
    plots.text(10, 6, "$\hat{y}= 0.5x+3$\n$r = 0.816$")
    plots.plot([4,14],[5,12])
    plots.title("II");

    plots.subplot(2,2,3)
    plots.scatter(anscombe.column('x3'),anscombe.column('y3'))
    plots.text(10, 6, "$\hat{y}= 0.5x+3$\n$r = 0.816$")
    plots.plot([4,14],[5,12])
    plots.title("III");

    plots.subplot(2,2,4)
    plots.scatter(anscombe.column('x4'),anscombe.column('y4'))
    plots.text(10, 6, "$\hat{y}= 0.5x+3$\n$r = 0.816$")
    plots.plot([8,19],[7,12.5])
    plots.title("IV");

    plots.show();



