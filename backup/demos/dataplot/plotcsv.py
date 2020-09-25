import pandas as pd
import matplotlib.pyplot as plt
t_dublin = pd.read_csv("./t_dublin_1_12.csv")
t_dublin_1 = t_dublin[t_dublin["mon"]==1].rename(columns={"t":"Jan"})["Jan"]
t_dublin_2 = t_dublin[t_dublin["mon"]==2].rename(columns={"t":"Feb"})["Feb"]
t_dublin_3 = t_dublin[t_dublin["mon"]==3].rename(columns={"t":"Mar"})["Mar"]
t_dublin_4 = t_dublin[t_dublin["mon"]==4].rename(columns={"t":"Apr"})["Apr"]
t_dublin_5 = t_dublin[t_dublin["mon"]==5].rename(columns={"t":"May"})["May"]
t_dublin_6 = t_dublin[t_dublin["mon"]==6].rename(columns={"t":"Jun"})["Jun"]
t_dublin_7 = t_dublin[t_dublin["mon"]==7].rename(columns={"t":"Jul"})["Jul"]
t_dublin_8 = t_dublin[t_dublin["mon"]==8].rename(columns={"t":"Aug"})["Aug"]
t_dublin_9 = t_dublin[t_dublin["mon"]==9].rename(columns={"t":"Sep"})["Sep"]
t_dublin_10 = t_dublin[t_dublin["mon"]==10].rename(columns={"t":"Oct"})["Oct"]
t_dublin_11 = t_dublin[t_dublin["mon"]==11].rename(columns={"t":"Nov"})["Nov"]
t_dublin_12 = t_dublin[t_dublin["mon"]==12].rename(columns={"t":"Dec"})["Dec"]

ts1 = pd.concat([t_dublin_1,t_dublin_2,t_dublin_3,t_dublin_4,t_dublin_5,t_dublin_6,t_dublin_7,
t_dublin_8,t_dublin_9,t_dublin_10,t_dublin_11,t_dublin_12],axis=1, sort=False)


t_shanghai = pd.read_csv("./t_shanghai_1_12.csv")
t_shanghai_1 = t_shanghai[t_shanghai["mon"]==1].rename(columns={"t":"Jan"})["Jan"]
t_shanghai_2 = t_shanghai[t_shanghai["mon"]==2].rename(columns={"t":"Feb"})["Feb"]
t_shanghai_3 = t_shanghai[t_shanghai["mon"]==3].rename(columns={"t":"Mar"})["Mar"]
t_shanghai_4 = t_shanghai[t_shanghai["mon"]==4].rename(columns={"t":"Apr"})["Apr"]
t_shanghai_5 = t_shanghai[t_shanghai["mon"]==5].rename(columns={"t":"May"})["May"]
t_shanghai_6 = t_shanghai[t_shanghai["mon"]==6].rename(columns={"t":"Jun"})["Jun"]
t_shanghai_7 = t_shanghai[t_shanghai["mon"]==7].rename(columns={"t":"Jul"})["Jul"]
t_shanghai_8 = t_shanghai[t_shanghai["mon"]==8].rename(columns={"t":"Aug"})["Aug"]
t_shanghai_9 = t_shanghai[t_shanghai["mon"]==9].rename(columns={"t":"Sep"})["Sep"]
t_shanghai_10 = t_shanghai[t_shanghai["mon"]==10].rename(columns={"t":"Oct"})["Oct"]
t_shanghai_11 = t_shanghai[t_shanghai["mon"]==11].rename(columns={"t":"Nov"})["Nov"]
t_shanghai_12 = t_shanghai[t_shanghai["mon"]==12].rename(columns={"t":"Dec"})["Dec"]

ts2 = pd.concat([t_shanghai_1,t_shanghai_2,t_shanghai_3,t_shanghai_4,t_shanghai_5,t_shanghai_6,t_shanghai_7,
t_shanghai_8,t_shanghai_9,t_shanghai_10,t_shanghai_11,t_shanghai_12],axis=1, sort=False)




ax1 = plt.subplot(211)
ax1.get_xaxis().set_visible(True)
a = ts1.boxplot(showfliers=False, showmeans=True)
plt.ylabel("In Fahrenheit (Dublin)")

ax2 = plt.subplot(212, sharex=ax1, sharey=ax1)
ts2.boxplot(showfliers=False, showmeans=True)
plt.ylabel("In Fahrenheit (Shanghai)")

plt.subplots_adjust(hspace=0.5)

plt.savefig('temperature.png', format='png')


# plt.show()





