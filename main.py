import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data dashboard")
 
#file = st.file_uploader("CSV File:", type="csv")
csv_path = "catanstats.csv"

if csv_path is not None:
    df = pd.read_csv(csv_path)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data analysis")
    st.write(df.describe())

    st.subheader("Frequency")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to analyze", columns)

    if selected_column:
        st.write(f"Analyzing frequency of numbers for: {selected_column}")
        
        plt.figure(figsize=(16, 6))
        sns.histplot(df[selected_column], kde=True, bins=range(2, 14), discrete=True)
        plt.title(f'Frecuencia de Números en {selected_column}', fontsize=14)
        plt.xlabel('Número del dado', fontsize=12)
        plt.ylabel('Frecuencia', fontsize=12)
        plt.xticks(range(2, 13))
        plt.tight_layout()
        st.pyplot(plt)

    st.subheader("Data Analysis: KDE Plot")
    columns = df.columns.tolist()
    selected_columns = st.multiselect("Select columns to analyze", columns, default=columns[:3])

    if selected_columns:
        plt.figure(figsize=(10, 6))
        for column in selected_columns:
            sns.kdeplot(df[column].dropna(), label=column)
        plt.title("Distribución de tiradas", fontsize=14)
        plt.xlabel("Número", fontsize=12)
        plt.ylabel("Densidad", fontsize=12)
        plt.legend()
        plt.tight_layout()
        st.pyplot(plt)
    else:
        st.warning("Please select at least one column to analyze.")