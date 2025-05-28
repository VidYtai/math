import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

# Title and Intro
st.title("📊 Change Starts with Me: A Statistical Journey")
st.subheader("Survey on Social Habit: Exercising")
st.write("""
**Name:** Navdeesh  
**Class:** 9D

This interactive project explores the habit of **exercising** among 20 people.
Let's see what the data reveals!
""")

# Simulated Survey Data (Fake but realistic)
people = [
    "Aarav", "Meera", "Rohan", "Kavya", "Aditya", "Isha", "Arjun", "Nandini", "Siddharth", "Anaya",
    "Vivaan", "Priya", "Kunal", "Tanya", "Harsh", "Sanya", "Rajat", "Sneha", "Dhruv", "Ayesha"
]
exercise_hours = [0.5, 1, 2, 1.5, 3, 2.5, 0, 1, 2, 1.5, 2, 3.5, 1, 0.5, 2.5, 1.5, 3, 2, 0, 1.5]
data = pd.DataFrame({"Person": people, "Exercise Hours/Day": exercise_hours})
st.dataframe(data)

# Grouping Data into Class Intervals
bins = [0, 1, 2, 3, 4]
labels = ["0-1", "1-2", "2-3", "3-4"]
data['Interval'] = pd.cut(data['Exercise Hours/Day'], bins=bins, labels=labels, include_lowest=True)
frequency = data['Interval'].value_counts().sort_index()

# Display Frequency Table
st.subheader("📈 Frequency Distribution")
freq_df = pd.DataFrame({"Interval": frequency.index, "Frequency": frequency.values})
st.dataframe(freq_df)

# Interactive Frequency Polygon using Plotly
st.subheader("📉 Frequency Polygon (Interactive)")
mid_points = [0.5, 1.5, 2.5, 3.5]
fig = go.Figure()
fig.add_trace(go.Scatter(x=mid_points, y=frequency.values, mode='lines+markers', name='Frequency',
                         line=dict(color='royalblue'), fill='tozeroy'))
fig.update_layout(title='Interactive Frequency Polygon of Exercise Habits',
                  xaxis_title='Exercise Time Intervals (hrs)',
                  yaxis_title='Number of People',
                  template='plotly_white')
st.plotly_chart(fig)

# Interpretation Write-up
st.subheader("🧠 Interpretation")

st.markdown("""
**Q1: What did the data show?**  
The data collected from 20 individuals shows a wide range of exercise habits, ranging from 0 to 3.5 hours per day. The most noticeable observation is that a significant portion of the participants tend to exercise between 1–2 hours daily, which appears to be the most balanced and commonly followed routine. This indicates a general awareness about health and fitness among people. The frequency of individuals exercising for more than 2 hours is also encouraging, reflecting dedication. However, it’s equally important to note that a few individuals reported little to no exercise at all. This shows a lack of consistency or motivation in some cases, which may lead to long-term health issues. The data paints a mixed picture but leans positively towards health consciousness. Ultimately, while there is room for improvement, the habit of exercising is present in most people’s lives, which is a promising takeaway from this survey.

**Q2: What habit is most common? What’s concerning?**  
From the frequency distribution, it’s clear that the most common exercise habit is spending 1 to 2 hours daily on physical activity. This is a healthy amount and falls in line with many fitness guidelines that recommend moderate daily exercise. This consistency among participants is encouraging and shows a developing routine among the youth and adults alike. What’s concerning, however, is the presence of individuals who either don’t exercise at all or exercise for less than an hour daily. A total of three people fall in this bracket, and while that may seem small, it’s still a warning sign. Inactivity can contribute to various physical and mental health problems, especially in a digital age where sedentary habits are the norm. If this pattern grows unchecked, it could lead to a larger health concern in the future. Promoting regular exercise and making it accessible and enjoyable is crucial for these individuals.

**Q3: How are you compared to the average?**  
When I compared my own habit of exercising for approximately 1.5 hours a day to the survey results, I noticed that I fall just slightly below the calculated average, which comes out to around 1.63 hours per day. This comparison is helpful because it gives me a real sense of where I stand in terms of fitness commitment compared to my peers. Although the difference is minor, it does highlight that there’s always room for improvement. Staying just below average can be a motivating factor to increase my consistency or maybe add another short session during the day. It also makes me reflect on whether the quality of my workout is matching the quantity. Am I being efficient with my time or just going through the motions? So while I’m doing fairly well, the average has given me a small nudge to push myself a bit further and aim higher.

**Q4: What ONE change will you adopt personally?**  
Based on this reflection and comparison with the group data, the one change I’m committing to is waking up 15 minutes earlier each morning to start my day with a short but focused workout. I’ve realized that the hardest part of building a habit is consistency, and adding just 15 minutes in the morning feels manageable yet impactful. It’s a small change that won’t disrupt my schedule but will definitely contribute to improving my energy, mood, and overall physical health. Starting the day with movement can set a positive tone for everything that follows. I believe this extra time will also help me build discipline, which spills over into other areas like studies, screen time, and even my eating habits. Eventually, that extra 15 minutes could grow into something bigger—but for now, it’s the most realistic and personal change I can lead, and I’m excited to stick to it.
""")
