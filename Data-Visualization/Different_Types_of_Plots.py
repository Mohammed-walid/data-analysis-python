import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "sleep_hours": [5, 6, 7, 5, 8, 7, 6, 9, 8, 7],
    "attendance": [50, 60, 65, 70, 75, 80, 85, 90, 95, 100],
    "exam_score": [40, 45, 50, 55, 65, 68, 75, 82, 90, 96],
    "study_method": [
        "Reading", "Video", "Practice", "Reading", "Video",
        "Practice", "Reading", "Video", "Practice", "Reading"
    ],
    "section": ["A", "A", "B", "B", "A", "B", "A", "B", "A", "B"]
}

df = pd.DataFrame(data)
print(df)

#Scatter plot
#We want to discover whether studying more hours is associated with higher exam scores
plt.scatter(df["hours_studied"], df["exam_score"])
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Hours Studied vs Exam Score")

#we want to investigate whether sleep hours are related to exam scores.
plt.figure()
plt.scatter(df["sleep_hours"], df["exam_score"])
plt.xlabel("Sleep Hours")
plt.ylabel("Exam Score")
plt.title("Sleep Hours vs Exam Score")

#Does attending more classes relate to better exam scores?
plt.figure()
plt.scatter(df["attendance"], df["exam_score"])
plt.xlabel("Attendance (%)")
plt.ylabel("Exam Score")
plt.title("Attendance vs Exam Score")

#Standard line plot
plt.figure()
plt.plot(df["day"], df["exam_score"])
plt.xlabel("Day")
plt.ylabel("Exam Score")
plt.title("Exam Scores Over Time")

#Histogram
plt.figure()
plt.hist(df["exam_score"], bins=5)
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.title("Distribution of Exam Scores")

#Bar plot
avg_scores = df.groupby("study_method")["exam_score"].mean()

plt.figure()
plt.bar(avg_scores.index, avg_scores.values)
plt.xlabel("Study Method")
plt.ylabel("Average Exam Score")
plt.title("Average Score by Study Method")

#Pseudo color plot
pivot = df.pivot_table(
    values="exam_score",
    index="section",
    columns="study_method",
    aggfunc="mean"
)

plt.figure()
plt.pcolor(pivot, cmap="RdBu")
plt.colorbar(label="Average Exam Score")
plt.xticks(
    [i + 0.5 for i in range(len(pivot.columns))],
    pivot.columns
)
plt.yticks(
    [i + 0.5 for i in range(len(pivot.index))],
    pivot.index
)
plt.xlabel("Study Method")
plt.ylabel("Section")
plt.title("Average Scores Heatmap")

#Regression plot
plt.figure()
sns.regplot(
    x="hours_studied",
    y="exam_score",
    data=df
)
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Regression: Study Hours vs Exam Score")

#Box and whisker plot
plt.figure()
sns.boxplot(
    x="section",
    y="exam_score",
    data=df
)
plt.xlabel("Section")
plt.ylabel("Exam Score")
plt.title("Exam Score by Section")

#Residual plot
plt.figure()
sns.residplot(
    x="hours_studied",
    y="exam_score",
    data=df
)
plt.xlabel("Hours Studied")
plt.ylabel("Residuals")
plt.title("Residual Plot")

#Kde plot
plt.figure()
sns.kdeplot(
    x="exam_score",
    data=df,
    fill=True
)
plt.xlabel("Exam Score")
plt.ylabel("Density")
plt.title("KDE Plot of Exam Scores")

#Distribution plot
plt.figure()
sns.histplot(
    data=df,
    x="exam_score",
    hue="section",
    bins=5,
    kde=True,
    stat="density",
    common_norm=False
)
plt.xlabel("Exam Score")
plt.ylabel("Density")
plt.title("Score Distribution by Section")

plt.show()
