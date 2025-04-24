import matplotlib.pyplot as plt
import pandas as pd


def plot_total_revenue_bar(df):
    if df.empty:
        return None
    fig, ax = plt.subplots()
    ax.bar(["Tổng doanh thu"], [df['Thành tiền'].sum()])
    ax.set_ylabel("VNĐ")
    ax.set_title("Tổng doanh thu")
    return fig

def plot_monthly_revenue(df):
    if df.empty:
        return None
    df['Tháng'] = pd.to_datetime(df['Ngày bán']).dt.to_period('M')
    monthly = df.groupby('Tháng')['Thành tiền'].sum().reset_index()
    fig, ax = plt.subplots()
    ax.plot(monthly['Tháng'].astype(str), monthly['Thành tiền'], marker='o')
    ax.set_ylabel("Doanh thu (VNĐ)")
    ax.set_title("Doanh thu theo tháng")
    ax.tick_params(axis='x', labelrotation=0)
    return fig

def plot_predicted_revenue(df):
    if df.empty:
        return None
    df['Tháng'] = pd.to_datetime(df['Ngày bán']).dt.to_period('M')
    monthly = df.groupby('Tháng')['Thành tiền'].sum()
    predicted = monthly.mean()
    fig, ax = plt.subplots()
    monthly.plot(kind='bar', ax=ax, color='skyblue', label='Thực tế')
    ax.axhline(predicted, color='red', linestyle='--', label='Dự đoán tháng tiếp theo')
    ax.set_title("Dự đoán doanh thu")
    ax.legend()
    ax.tick_params(axis='x', labelrotation=0)
    return fig

def plot_top_5_products(df):
    if df.empty:
        return None
    top = df.groupby('Tên mặt hàng')['Số lượng'].sum().nlargest(5)
    fig, ax = plt.subplots()
    top.plot(kind='bar', ax=ax, color='green')
    ax.set_title("Top 5 sản phẩm bán chạy nhất")
    ax.tick_params(axis='x', labelrotation=0)
    return fig

def plot_bottom_5_products(df):
    if df.empty:
        return None
    bottom = df.groupby('Tên mặt hàng')['Số lượng'].sum().nsmallest(5)
    fig, ax = plt.subplots()
    bottom.plot(kind='bar', ax=ax, color='orange')
    ax.set_title("5 sản phẩm bán chậm nhất")
    ax.tick_params(axis='x', labelrotation=0)
    return fig

def plot_revenue_by_city(df):
    if df.empty or 'Thành phố' not in df.columns:
        return None
    revenue = df.groupby('Thành phố')['Thành tiền'].sum().nlargest(5)
    fig, ax = plt.subplots()
    revenue.plot(kind='bar', ax=ax, color='purple')
    ax.set_title("Top 5 thành phố có doanh thu cao nhất")
    ax.tick_params(axis='x', labelrotation=0)  # label nằm ngang
    return fig

def plot_revenue_by_hour(df):
    if df.empty or 'Thời gian' not in df.columns:
        return None
    df['Giờ'] = pd.to_datetime(df['Thời gian']).dt.hour
    hourly = df.groupby('Giờ')['Thành tiền'].sum()
    fig, ax = plt.subplots()
    hourly.plot(kind='line', marker='o', ax=ax)
    ax.set_title("Doanh thu theo giờ")
    ax.set_xlabel("Giờ")
    return fig

def plot_top_revenue_days(df):
    if df.empty:
        return None
    daily = df.groupby('Ngày bán')['Thành tiền'].sum().nlargest(5)
    fig, ax = plt.subplots()
    daily.plot(kind='bar', ax=ax, color='teal')
    ax.set_title("Top 5 ngày doanh thu cao nhất")
    ax.tick_params(axis='x', labelrotation=0)
    return fig

def plot_top_revenue_products(df):
    if df.empty:
        return None
    revenue = df.groupby('Tên mặt hàng')['Thành tiền'].sum().nlargest(5)
    fig, ax = plt.subplots()
    revenue.plot(kind='bar', ax=ax, color='navy')
    ax.set_title("Top 5 sản phẩm doanh thu cao nhất")
    ax.tick_params(axis='x', labelrotation=0)
    return fig

def plot_bottom_revenue_products(df):
    if df.empty:
        return None
    revenue = df.groupby('Tên mặt hàng')['Thành tiền'].sum().nsmallest(5)
    fig, ax = plt.subplots()
    revenue.plot(kind='bar', ax=ax, color='red')
    ax.set_title("5 sản phẩm doanh thu thấp nhất")
    ax.tick_params(axis='x', labelrotation=0)
    return fig
