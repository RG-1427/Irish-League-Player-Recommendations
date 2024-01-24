import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def createFile(pos, df):
    rowsToDrop = []
    for i in range(0, len(df)):
        test_string = df.iloc[i]["Position"].split(", ")
        flag = 0
        for j in test_string:
            for k in pos:
                if j == k:
                    flag = 1
                    break
        if flag == 0:
            rowsToDrop.append(i)
    df = df.drop(rowsToDrop)
    df.to_excel(pos[0] + ".xlsx")
    print("File for position", pos, "has been created")


df = pd.read_excel("Search results-2.xlsx")

pos = ["GK"]
#createFile(pos, df)

pos = ["CB", "LCB", "RCB"]
#createFile(pos, df)

pos = ["LB", "LWB", "RB", "RWB"]
#createFile(pos, df)

pos = ["DMF", "LDMF", "RDMF"]
#createFile(pos, df)

pos = ["CMF", "LCMF", "RCMF"]
#createFile(pos, df)

pos = ["AMF", "LAMF", "RAMF"]
#createFile(pos, df)

pos = ["LW", "RW"]
#createFile(pos, df)

pos = ["CF"]
#createFile(pos, df)

#GK
#Conceded Goals vs Shots Against per 90 both
#Save Rate % vs Clean Sheet
#Passes per 90 vs Accurate Passes
data = pd.read_excel("GK.xlsx")
sns.lmplot(x="Conceded goals per 90", y="Shots against per 90", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("GK Comparison 1")
plt.show()
sns.lmplot(x="Save rate, %", y="Clean sheets", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("GK Comparison 2")
plt.show()
sns.lmplot(x="Passes per 90", y="Accurate passes, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("GK Comparison 3")
plt.show()

#CB
#Duels per 90 vs Duels Won%
#Passes per 90 vs Accurate Passes
#Long Passes per 90 vs Accurate Long Passes
#Defensive Duels per 90 vs Defensive Duels won
#Ariel Duels per 90 vs Ariel Duels
data = pd.read_excel("CB.xlsx")
sns.lmplot(x="Duels per 90", y="Duels won, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("CB Comparison 1")
plt.show()
sns.lmplot(x="Passes per 90", y="Accurate passes, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("CB Comparison 2")
plt.show()
sns.lmplot(x="Long passes per 90", y="Accurate long passes, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("CB Comparison 3")
plt.show()
sns.lmplot(x="Defensive duels per 90", y="Defensive duels won, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("CB Comparison 4")
plt.show()
sns.lmplot(x="Aerial duels per 90", y="Aerial duels won, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("CB Comparison 5")
plt.show()

#LB/RB/LWB/RWB
#Assists vs Xa
#Defensive Duels per 90 vs Defensive Duels%
#Crosses per 90 vs Accurate Crosses
#Dribbles per 90 vs Successful Dribbles
#Progressive Runs vs Interceptions per 90
data = pd.read_excel("LB.xlsx")
sns.lmplot(x="Assists", y="xA", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Wingback Comparison 1")
plt.show()
sns.lmplot(x="Defensive duels per 90", y="Defensive duels won, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Wingback Comparison 2")
plt.show()
sns.lmplot(x="Crosses per 90", y="Accurate crosses, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Wingback Comparison 3")
plt.show()
sns.lmplot(x="Dribbles per 90", y="Successful dribbles, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Wingback Comparison 4")
plt.show()
sns.lmplot(x="Progressive runs per 90", y="Interceptions per 90", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Wingback Comparison 5")
plt.show()

#DMF
#Duels per 90 vs Duels Won
#Interceptions vs Fouls Suffered
#Passes per 90 vs Accurate Passes
#Forward passes per 90 vs Accurate forward passes
data = pd.read_excel("DMF.xlsx")
sns.lmplot(x="Duels per 90", y="Duels won, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Defensive Mid Comparison 1")
plt.show()
sns.lmplot(x="Interceptions per 90", y="Fouls suffered per 90", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Defensive Mid Comparison 2")
plt.show()
sns.lmplot(x="Passes per 90", y="Accurate passes, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Defensive Mid Comparison 3")
plt.show()
sns.lmplot(x="Forward passes per 90", y="Accurate forward passes, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Defensive Mid Comparison 4")
plt.show()

#CMF
#Duels per 90 vs Duels Won
#Interceptions vs Fouls Suffered
#Passes per 90 vs Succesful Passes
#Forward passes per 90 vs Succesful forward passes
#Progressive runs per 90 vs Key Passes per 90
data = pd.read_excel("CMF.xlsx")
sns.lmplot(x="Duels per 90", y="Duels won, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Centre Mid Comparison 1")
plt.show()
sns.lmplot(x="Interceptions per 90", y="Fouls suffered per 90", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Centre Mid Comparison 2")
plt.show()
sns.lmplot(x="Passes per 90", y="Accurate passes, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Centre Mid Comparison 3")
plt.show()
sns.lmplot(x="Forward passes per 90", y="Accurate forward passes, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Centre Mid Comparison 4")
plt.show()
sns.lmplot(x="Progressive runs per 90", y="Key passes per 90", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Centre Mid Comparison 5")
plt.show()

#AMF
#Assists vs Xa
#Goals vs Xg
#Shots per 90 vs Shots on target
#Dirbbles per 90 vs Succesful Dribbles
#Shot Assists vs Second Assists
data = pd.read_excel("AMF.xlsx")
sns.lmplot(x="Assists", y="xA", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Attacking Mid Comparison 1")
plt.show()
sns.lmplot(x="Goals", y="xG", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Attacking Mid Comparison 2")
plt.show()
sns.lmplot(x="Shots per 90", y="Shots on target, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Attacking Mid Comparison 3")
plt.show()
sns.lmplot(x="Dribbles per 90", y="Successful dribbles, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Attacking Mid Comparison 4")
plt.show()
sns.lmplot(x="Shot assists per 90", y="Second assists per 90", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Attacking Mid Comparison 5")
plt.show()

#LW/RW
#Assists vs Xa
#Goals vs Xg
#Shots per 90 vs Shots on target
#Crosses per 90 vs Successful Crosses
#Defensive Duels per 90 vs Succesful Defensive Duels
data = pd.read_excel("LW.xlsx")
sns.lmplot(x="Assists", y="xA", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Winger Comparison 1")
plt.show()
sns.lmplot(x="Goals", y="xG", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Winger Comparison 2")
plt.show()
sns.lmplot(x="Shots per 90", y="Shots on target, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Winger Comparison 3")
plt.show()
sns.lmplot(x="Defensive duels per 90", y="Defensive duels won, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Winger Comparison 4")
plt.show()
sns.lmplot(x="Crosses per 90", y="Accurate crosses, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Winger Comparison 5")
plt.show()

#CF
#Assists vs Xa
#Goals vs Xg
#Shots per 90 vs Shots on target
#non penalty goals vs assists
#shots vs goal conversion
data = pd.read_excel("CF.xlsx")
sns.lmplot(x="Assists", y="xA", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Striker Comparison 1")
plt.show()
sns.lmplot(x="Goals", y="xG", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Striker Comparison 2")
plt.show()
sns.lmplot(x="Shots per 90", y="Shots on target, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Striker Comparison 3")
plt.show()
sns.lmplot(x="Non-penalty goals", y="Assists", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Striker Comparison 4")
plt.show()
sns.lmplot(x="Shots per 90", y="Goal conversion, %", data=data, hue="Team", fit_reg=False)
ax = plt.gca()
ax.set_title("Striker Comparison 5")
plt.show()