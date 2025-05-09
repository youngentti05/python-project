import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

def plot_total_revenue_bar(df):
    if df.empty:
        return None
    total = df['Thành tiền'].sum()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.text(0.5, 0.5, f"Tổng doanh thu: {total:,.0f} VNĐ", 
            ha='center', va='center', fontsize=12)
    ax.set_title("Tổng doanh thu")
    ax.axis('off')
    return fig

def plot_monthly_revenue(df):
    if df.empty:
        return None
    df['Tháng'] = pd.to_datetime(df['Ngày bán'], format='%Y-%m-%d %H:%M', errors='coerce').dt.to_period('M')
    if df['Tháng'].isna().any():
        df = df.dropna(subset=['Tháng'])
    monthly = df.groupby('Tháng')['Thành tiền'].sum().reset_index()
    if monthly.empty:
        return None
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(monthly['Tháng'].astype(str), monthly['Thành tiền'], marker='o')
    ax.set_ylabel("Doanh thu (VNĐ)")
    ax.set_title("Doanh thu theo tháng")
    ax.tick_params(axis='x', labelrotation=0)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
    return fig

def plot_predicted_revenue(df):
    if df.empty:
        return None
    df['Tháng'] = pd.to_datetime(df['Ngày bán'], format='%Y-%m-%d %H:%M', errors='coerce').dt.to_period('M')
    if df['Tháng'].isna().any():
        df = df.dropna(subset=['Tháng'])
    monthly = df.groupby('Tháng')['Thành tiền'].sum()
    if monthly.empty:
        return None
    predicted = monthly.mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    monthly.plot(kind='bar', ax=ax, color='skyblue', label='Thực tế')
    ax.axhline(predicted, color='red', linestyle='--', label='Dự đoán tháng tiếp theo (trung bình)')
    ax.set_title("Dự đoán doanh thu")
    ax.set_ylabel("Doanh thu (VNĐ)")
    ax.legend()
    ax.tick_params(axis='x', labelrotation=0)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
    return fig

def plot_top_5_products(df):
    if df.empty:
        return None
    top = df[['Tên mặt hàng', 'Số lượng']].groupby('Tên mặt hàng')['Số lượng'].sum().nlargest(5)
    fig, ax = plt.subplots(figsize=(10, 6))
    top.plot(kind='bar', ax=ax, color='green')
    ax.set_title("Top 5 sản phẩm bán chạy nhất")
    ax.set_ylabel("Số lượng bán")
    ax.tick_params(axis='x', labelrotation=0)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
    return fig

def plot_bottom_5_products(df):
    if df.empty:
        return None
    bottom = df[['Tên mặt hàng', 'Số lượng']].groupby('Tên mặt hàng')['Số lượng'].sum().nsmallest(5)
    fig, ax = plt.subplots(figsize=(10, 6))
    bottom.plot(kind='bar', ax=ax, color='orange')
    ax.set_title("5 sản phẩm bán chậm nhất")
    ax.set_ylabel("Số lượng bán")
    ax.tick_params(axis='x', labelrotation=0)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
    return fig

def plot_revenue_by_city(df):
    if df.empty or 'Thành phố' not in df.columns:
        return None
    revenue = df[['Thành phố', 'Thành tiền']].groupby('Thành phố')['Thành tiền'].sum().nlargest(5)
    fig, ax = plt.subplots(figsize=(10, 6))
    revenue.plot(kind='bar', ax=ax, color='purple')
    ax.set_title("Top 5 thành phố có doanh thu cao nhất")
    ax.set_ylabel("Doanh thu (VNĐ)")
    ax.tick_params(axis='x', labelrotation=0)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
    return fig

def plot_revenue_by_hour(df):
    if df.empty or 'Thời gian' not in df.columns:
        return None
    df['Giờ'] = pd.to_datetime(df['Thời gian'], format='%Y-%m-%d %H:%M', errors='coerce').dt.hour
    if df['Giờ'].isna().any():
        df = df.dropna(subset=['Giờ'])
    hourly = df.groupby('Giờ')['Thành tiền'].sum()
    if hourly.empty:
        return None
    fig, ax = plt.subplots(figsize=(10, 6))
    hourly.plot(kind='line', marker='o', ax=ax)
    ax.set_title("Doanh thu theo giờ")
    ax.set_xlabel("Giờ")
    ax.set_ylabel("Doanh thu (VNĐ)")
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
    return fig

def plot_top_revenue_days(df):
    if df.empty:
        return None
    df['Ngày bán'] = pd.to_datetime(df['Ngày bán'], format='%Y-%m-%d %H:%M', errors='coerce')
    if df['Ngày bán'].isna().any():
        df = df.dropna(subset=['Ngày bán'])
    daily = df.groupby(df['Ngày bán'].dt.date)['Thành tiền'].sum().sort_values(ascending=False).head(5)
    if daily.empty:
        return None
    fig, ax = plt.subplots(figsize=(10, 6))
    daily.plot(kind='bar', ax=ax, color='teal')
    ax.set_title("Top 5 ngày doanh thu cao nhất")
    ax.set_ylabel("Doanh thu (VNĐ)")
    ax.tick_params(axis='x', labelrotation=0)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
    return fig

def plot_top_revenue_products(df):
    if df.empty:
        return None
    revenue = df[['Tên mặt hàng', 'Thành tiền']].groupby('Tên mặt hàng')['Thành tiền'].sum().nlargest(5)
    fig, ax = plt.subplots(figsize=(10, 6))
    revenue.plot(kind='bar', ax=ax, color='navy')
    ax.set_title("Top 5 sản phẩm doanh thu cao nhất")
    ax.set_ylabel("Doanh thu (VNĐ)")
    ax.tick_params(axis='x', labelrotation=0)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
    return fig

def plot_bottom_revenue_products(df):
    if df.empty:
        return None
    revenue = df[['Tên mặt hàng', 'Thành tiền']].groupby('Tên mặt hàng')['Thành tiền'].sum().nsmallest(5)
    fig, ax = plt.subplots(figsize=(10, 6))
    revenue.plot(kind='bar', ax=ax, color='red')
    ax.set_title("5 sản phẩm doanh thu thấp nhất")
    ax.set_ylabel("Doanh thu (VNĐ)")
    ax.tick_params(axis='x', labelrotation=0)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
    return fig