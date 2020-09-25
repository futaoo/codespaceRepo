import pandas as pd
import matplotlib.pyplot as plt
t_dublin = pd.read_csv("./t_dublin_1_12.csv")


start = 1951
end = 1955
b = []
while end <= 2020 :
    b.append([start, end])
    start += 5
    end += 5

t_dublin_year = []

for i in range(0, len(b)):
    t_dublin_year.append(t_dublin[(b[i][0]<=t_dublin["year"])&(t_dublin["year"]<=b[i][1])]["t"].rename(columns={"t":str(b[i][0])}))


ts = pd.concat(t_dublin_year,axis=1, sort=False)
ts.boxplot()
plt.show()

