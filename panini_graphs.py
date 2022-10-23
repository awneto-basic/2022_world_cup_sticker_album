import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("stickers2_pdf.csv")
print(df.head())
packets = df["number of packets"]
pXk_A_n = df["P(Xk(A)=n)"]
pXk_Altn = df["P(Xk(A)<n)"]
EXkA = df["E(Xk(A))"]
pZnAk = df["P(Zn(A)=k)"]
pZnAltek = df["P(Zn(A)<=k)"]

fig, (ax1, ax2) = plt.subplots(2,figsize=(3, 9),sharex=True)


ax1.plot(packets, pXk_A_n)
ax2.plot(packets, EXkA)

plt.xticks(np.arange(0,2001,100))

ax1.set_title("Probability of completing the subset", loc="left")
ax1.set_ylabel("Probability")

ax2.set_title("Expected number of different stickers from the subset to obtain", loc="left")
ax2.set_ylabel("Number of different stickers")

plt.xlabel("number of packets bought")

plt.show()

fig = plt.plot(packets,pZnAk)
plt.title("Waiting time probability distribution", loc="left")
plt.xlabel("Number of packets bought")
plt.ylabel("Probability")
plt.xticks(np.arange(0,2001,100))
plt.show()
