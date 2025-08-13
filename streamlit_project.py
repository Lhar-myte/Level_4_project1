import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title("FINAL PROJECT")

with st.expander("Show dataset"):
    df = pd.read_csv("C:\\Level_4_project1\\mystery_books_final.csv")
    st.write(df.head(400))



total_books = len(df)
if st.button("Click for the total number of books scraped"):
    st.write(f"Total number of books scraped: {total_books}")


df["price_con"] = df["Price"].str.replace('£', '').astype(float)

average_price= df["price_con"].mean()
if st.button("Click for the average books"):
    st.write(f"The average books is: £{average_price:.2f}")




df["price_num"] = df["Price"].str.replace('£', '').astype(float)
minimum_price= df["price_num"].min()
maximum_price= df["price_num"].max()
if st.button("Click for the minimum price"):
    st.write(f"The minimum price is: £{minimum_price}")
if st.button("Click for the maximum price"):
    st.write(f"The maximum price is: £{maximum_price}")


books_per_rating = df['Rating'].value_counts()
if st.button("Click for books per rating"):
    st.write(f"{books_per_rating}")

df['Price_num'] = df['Price'].str.replace('£', '', regex=False).astype(float)

rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating_num'] = df['Rating'].map(rating_map)
correlation = df['Price_num'].corr(df['Rating_num'])
if st.button("Click for Correlation between price and rating"):
    st.write(f"Correlation between price and rating: {correlation:.2f}")


total_book_in_stock = (df['Availability'] == 'In stock').sum()
total_book_out_of_stock = (df['Availability'] != 'In stock').sum()

if st.button("Click to check for the total of books in stock"):
    st.write(f"Total of books in stock: {total_book_in_stock}")
if st.button("Click to check for the total of books out of stock"):
    st.write(f"Total of books out of stock: {total_book_out_of_stock}")

total_book_in_stock = (df['Availability'] == 'In stock').sum()
total_books = len(df)
total_percentage = (total_book_in_stock /  total_books) * 100

if st.button("Click to check for the Percentage of books in stock"):
    st.write(f" Percentage of books in stock: {total_percentage:.2f}%")




fig = px.histogram(df, x='Price_num', nbins=10, title='Histogram of Book Prices',
                   labels={'Price_num': 'Price (£)'},
                   color_discrete_sequence=['skyblue'])

st.plotly_chart(fig)



availability_counts = df['Availability'].value_counts()
availability_pie = px.pie(
    names=availability_counts.index,
    values=availability_counts.values,
    title='Availability Ratio'
)

st.plotly_chart(availability_pie)


avg_price_per_rating = df.groupby('Rating')['Price_num'].mean()
st.title("Average Price by Rating")
st.bar_chart(avg_price_per_rating)
