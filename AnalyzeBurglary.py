import pandas as pd

df = pd.read_csv("network_samples_burglary.csv")

ldf = df[df["Burglary"] == 1]
ldf = ldf[ldf["Earthquake"] == 1]
pAlarmGivenNoEvents = len(ldf[ldf["Alarm"] == 1]) / len(ldf["Alarm"])
print(pAlarmGivenNoEvents)
#print(df.mean())