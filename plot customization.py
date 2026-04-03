import matplotlib.pyplot as plt
year = [1950,1970,1990,2010]
population = [2.519, 3.692, 5.263, 6.972]
year = [1800, 1850, 1900] + year#adding more data
population = [1.0, 1.262, 1.650] + population#adding more data
plt.plot(year, population)
plt.xlabel("year")#labels x axis as year
plt.ylabel("population")#labels y axis as population
plt.title("world population")#labels the title as world population

plt.show()