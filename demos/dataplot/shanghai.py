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

ts = pd.concat([t_shanghai_1,t_shanghai_2,t_shanghai_3,t_shanghai_4,t_shanghai_5,t_shanghai_6,t_shanghai_7,
t_shanghai_8,t_shanghai_9,t_shanghai_10,t_shanghai_11,t_shanghai_12],axis=1, sort=False)