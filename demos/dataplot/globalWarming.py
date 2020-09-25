import pandas as pd
import matplotlib.pyplot as plt
t_shanghai = pd.read_csv("./t_shanghai_1_12.csv")


start = 1951
end = 1955
b = []
while end <= 2020 :
    b.append([start, end])
    start += 5
    end += 5

t_shanghai_year = []

for i in range(0, len(b)):
    print(b[i][0])
    t_shanghai_year.append(t_shanghai[(b[i][0]<=t_shanghai["year"])&(t_shanghai["year"]<=b[i][1])].rename(columns={"t":str(b[i][0])})[str(b[i][0])])


ts = pd.concat(t_shanghai_year,axis=1, sort=False)
ax = ts.boxplot(showfliers=False, showmeans=True)
plt.ylabel("In Fahrenheit (Shanghai)")
plt.xticks(rotation=45)
plt.savefig('globalwarming_sh.png', format='png')
#plt.show()

