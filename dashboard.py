import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def create_daily_use_df(df):
    daily_use_df = df.resample(rule='D', on='date').agg({
        'count': 'sum'
    })
    daily_use_df = daily_use_df.reset_index()
    
    return daily_use_df

def create_casual_users_df(df):
    casual_users_df = df.resample(rule='D', on='date').agg({
        'casual': 'sum'
    })
    casual_users_df = casual_users_df.reset_index()
    return casual_users_df

def create_registered_users_df(df):
    registered_users_df = df.resample(rule='D', on='date').agg({
        'registered': 'sum'
    })
    registered_users_df = registered_users_df.reset_index()
    return registered_users_df

all_df = pd.read_csv("all_data.csv")

datetime_columns = ["date", "date"]
all_df.sort_values(by="date", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])
    
min_date = all_df["date"].min()
max_date = all_df["date"].max()

with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
main_df = all_df[(all_df["date"] >= str(start_date)) & 
                (all_df["date"] <= str(end_date))]

daily_use_df = create_daily_use_df(main_df)

st.header('Bike Sharing Dashboard 🚲')
st.subheader('Daily Use')

total_use = daily_use_df['count'].sum()
st.metric("Total use", value=total_use)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    daily_use_df["date"],
    daily_use_df["count"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)

casual_users_df = create_casual_users_df(main_df)

casual_use = casual_users_df['casual'].sum()
st.metric("Casual users", value=casual_use)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    casual_users_df["date"],
    casual_users_df["casual"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)
registered_users_df = create_registered_users_df(main_df)

registered_use = registered_users_df['registered'].sum()
st.metric("Registered users", value=registered_use)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    registered_users_df["date"],
    registered_users_df["registered"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)

st.subheader('User Demographics')
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

def daily_stack_bar(data, col):
    fig, ax = plt.subplots(figsize=(20, 10))
    p1 = ax.bar(data[col].unique(), data.groupby([col])['casual'].sum())
    p2 = ax.bar(data[col].unique(), data.groupby([col])['registered'].sum(), bottom=data.groupby([col])['casual'].sum())

    ax.set_ylabel('Count')
    ax.legend((p1[0], p2[0]), ('Casual', 'Registered'))

    st.pyplot(fig)

def month_stack_bar(data, col):
    fig, ax = plt.subplots(figsize=(20, 10))
    p1 = ax.bar(data[col].unique(), data.groupby([col])['casual'].sum())
    p2 = ax.bar(data[col].unique(), data.groupby([col])['registered'].sum(), bottom=data.groupby([col])['casual'].sum())

    ax.set_ylabel('Count')
    ax.legend((p1[0], p2[0]), ('Casual', 'Registered'))

    st.pyplot(fig)

data = pd.DataFrame(all_df)

col1, col2 = st.columns(2)

with col1:
    daily_stack_bar(data, 'weekday')

with col2:
    month_stack_bar(data, 'month')
    
def season_stack_bar(data, col):
    fig, ax = plt.subplots(figsize=(16, 8))
    p1 = ax.bar(data[col].unique(), data.groupby([col])['casual'].sum())
    p2 = ax.bar(data[col].unique(), data.groupby([col])['registered'].sum(), bottom=data.groupby([col])['casual'].sum())

    ax.set_ylabel('Count')
    ax.legend((p1[0], p2[0]), ('Casual', 'Registered'))

    st.pyplot(fig)


def season_stack_bar(data, col):
    fig, ax = plt.subplots(figsize=(16, 8))
    p1 = ax.bar(data[col].unique(), data.groupby([col])['casual'].sum())
    p2 = ax.bar(data[col].unique(), data.groupby([col])['registered'].sum(), bottom=data.groupby([col])['casual'].sum())

    ax.set_ylabel('Count')
    ax.legend((p1[0], p2[0]), ('Casual', 'Registered'))

    st.pyplot(fig)

data = pd.DataFrame(all_df)

col1, col2 = st.columns(2)

with col1:
    daily_stack_bar(data, 'season')

with col2:
    month_stack_bar(data, 'workingday')