import sqlite3
import pandas as pd

with sqlite3.connect("sales.db") as conn:
    print('\na) Wyświetl tylko sprzedaż produktu „Laptop”')
    sql_query = ("""
    SELECT * FROM sales
    WHERE product == "Laptop"
    """)
    df = pd.read_sql(sql_query, conn)
    print(df)

    print('\nb) Wyświetl dane tylko z dni 2025-05-07 i 2025-05-08')
    sql_query = ("""
    SELECT * FROM sales
    WHERE date = "2025-05-07" OR date = "2025-05-08"
    """)
    df = pd.read_sql(sql_query, conn)
    print(df)

    print('\nc) Wyświetl tylko transakcje, w których cena jednostkowa przekracza 200 zł')
    sql_query = ("""
    SELECT * FROM sales
    WHERE price > 200
    """)
    df = pd.read_sql(sql_query, conn)
    print(df)
    
    print('\nd) Oblicz łączną wartość sprzedaży dla każdego produkt')
    sql_query = ("""
    SELECT product, SUM(price*quantity) as "total value" FROM sales
    GROUP BY product
    """)
    df = pd.read_sql(sql_query, conn)
    print(df)

    print('\ne) Znajdź dzień z największą liczbą sprzedanych sztuk')
    sql_query = ("""
    SELECT SUM(quantity) as "total quantity", date FROM sales
    GROUP BY date
    """)
    df = pd.read_sql(sql_query, conn)
    print(df)
    print("Maximum:")
    print(df.loc[df["total quantity"].idxmax()])