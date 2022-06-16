import pandas as pd
import matplotlib.pyplot as plt

df0 = pd.read_csv("network_samples_faculty_0.csv")
df1 = pd.read_csv("network_samples_faculty_1.csv")
df2 = pd.read_csv("network_samples_faculty_2.csv")
df3 = pd.read_csv("network_samples_faculty_3.csv")
df4 = pd.read_csv("network_samples_faculty_4.csv")

ps0 = df0["posteriorSigma"]
ps1 = df1["posteriorSigma"]
ps2 = df2["posteriorSigma"]
ps3 = df3["posteriorSigma"]
ps4 = df4["posteriorSigma"]

pm0 = df0["posteriorMu"]
pm1 = df1["posteriorMu"]
pm2 = df2["posteriorMu"]
pm3 = df3["posteriorMu"]
pm4 = df4["posteriorMu"]

plt.plot(ps0, label="0")
plt.plot(ps1, label="1")
plt.plot(ps2, label="2")
plt.plot(ps3, label="3")
plt.plot(ps4, label="4")
plt.ylabel("sigma")
plt.xlabel("sample number")
plt.title("Estimated Sigma")
plt.legend()
plt.show()

plt.plot(pm0, label="0")
plt.plot(pm1, label="1")
plt.plot(pm2, label="2")
plt.plot(pm3, label="3")
plt.plot(pm4, label="4")
plt.title("Estimated Mu")
plt.ylabel("mu")
plt.xlabel("sample number")
plt.legend()
plt.show()