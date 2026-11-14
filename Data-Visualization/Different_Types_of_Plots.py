import pandas as pd
import matplotlib.pyplot as plt

data = {
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    "sleep_hours": [5, 6, 7, 5, 8, 7, 6, 9, 8, 7],

    "attendance": [50, 60, 65, 70, 75, 80, 85, 90, 95, 100],

    "exam_score": [40, 45, 50, 55, 65, 68, 75, 82, 90, 96]
}

df = pd.DataFrame(data)

print(df)