import matplotlib.pyplot as plt#u have to download ts for it to work, pip install matplotlib
year = [1950,1970,1990,2010]#data in lists
population = [2.519, 3.692, 5.263, 6.972]#in billions
plt.plot(year, population)#year is horizontal, and population is vertical
plt.show()#displays the plot