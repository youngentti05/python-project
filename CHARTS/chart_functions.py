import matplotlib.pyplot as plt
import pandas as pd

def plot_total_revenue_bar(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if df.empty:
        ax.text(0.5, 0.5, "Không có dữ liệu", ha='center', va='center', fontsize=12)
    else:
        total = df["Doanh thu"].sum()
        ax.bar(["Tổng Doanh Thu"], [total], color='#388e3c')
        ax.set_ylabel("Doanh Thu (VNĐ)")
    ax.set_title("Tổng Doanh Thu")
    return fig

def plot_monthly_revenue(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if df.empty:
        ax.text(0.5, 0.5, "Không có dữ liệu", ha='center', va='center', fontsize=12)
    else:
        monthly = df.groupby(df['Ngày'].apply(lambda x: pd.to_datetime(x).to_period('M')))["Doanh thu"].sum()
        monthly.plot(kind="bar", ax=ax, color='#388e3c')
        ax.set_xlabel("Tháng")
        ax.set_ylabel("Doanh Thu (VNĐ)")
    ax.set_title("Doanh Thu Theo Tháng")
    return fig

def plot_predicted_revenue(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.text(0.5, 0.5, "Biểu đồ dự đoán: Chưa hỗ trợ", ha='center', va='center', fontsize=12)
    ax.set_title("Dự Đoán Doanh Thu")
    return fig

def plot_top_5_products(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if df.empty:
        ax.text(0.5, 0.5, "Không có dữ liệu", ha='center', va='center', fontsize=12)
    else:
        top = df.groupby("Product")["Quantity Ordered"].sum().nlargest(5)
        top.plot(kind="bar", ax=ax, color='#388e3c')
        ax.set_xlabel("Sản Phẩm")
        ax.set_ylabel("Số Lượng")
    ax.set_title("Top 5 Sản Phẩm Bán Chạy")
    return fig

def plot_bottom_5_products(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if df.empty:
        ax.text(0.5, 0.5, "Không có dữ liệu", ha='center', va='center', fontsize=12)
    else:
        bottom = df.groupby("Product")["Quantity Ordered"].sum().nsmallest(5)
        bottom.plot(kind="bar", ax=ax, color='#388e3c')
        ax.set_xlabel("Sản Phẩm")
        ax.set_ylabel("Số Lượng")
    ax.set_title("Top 5 Sản Phẩm Kém Bán")
    return fig

def plot_revenue_by_city(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if df.empty:
        ax.text(0.5, 0.5, "Không có dữ liệu", ha='center', va='center', fontsize=12)
    else:
        city = df.groupby("Thành phố")["Doanh thu"].sum()
        city.plot(kind="bar", ax=ax, color='#388e3c')
        ax.set_xlabel("Thành Phố")
        ax.set_ylabel("Doanh Thu (VNĐ)")
    ax.set_title("Doanh Thu Theo Thành Phố")
    return fig

def plot_revenue_by_hour(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if df.empty:
        ax.text(0.5, 0.5, "Không có dữ liệu", ha='center', va='center', fontsize=12)
    else:
        hourly = df.groupby(df["Thời gian"].dt.hour)["Doanh thu"].sum()
        hourly.plot(kind="bar", ax=ax, color='#388e3c')
        ax.set_xlabel("Giờ")
        ax.set_ylabel("Doanh Thu (VNĐ)")
    ax.set_title("Doanh Thu Theo Giờ")
    return fig

def plot_top_revenue_days(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if df.empty:
        ax.text(0.5, 0.5, "Không có dữ liệu", ha='center', va='center', fontsize=12)
    else:
        top_days = df.groupby('Ngày')["Doanh thu"].sum().nlargest(5)
        top_days.plot(kind="bar", ax=ax, color='#388e3c')
        ax.set_xlabel("Ngày")
        ax.set_ylabel("Doanh Thu (VNĐ)")
    ax.set_title("Ngày Doanh Thu Cao Nhất")
    return fig

def plot_monthly_revenue_detail(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if df.empty:
        ax.text(0.5, 0.5, "Không có dữ liệu", ha='center', va='center', fontsize=12)
    else:
        monthly = df.groupby(df['Ngày'].apply(lambda x: pd.to_datetime(x).to_period('M')))["Doanh thu"].sum()
        monthly.plot(kind="bar", ax=ax, color='#388e3c')
        ax.set_xlabel("Tháng")
        ax.set_ylabel("Doanh Thu (VNĐ)")
    ax.set_title("Doanh Thu Từng Tháng")
    return fig

def plot_top_revenue_products(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if df.empty:
        ax.text(0.5, 0.5, "Không có dữ liệu", ha='center', va='center', fontsize=12)
    else:
        top = df.groupby("Product")["Doanh thu"].sum().nlargest(5)
        top.plot(kind="bar", ax=ax, color='#388e3c')
        ax.set_xlabel("Sản Phẩm")
        ax.set_ylabel("Doanh Thu (VNĐ)")
    ax.set_title("Top 5 Sản Phẩm Doanh Thu Cao")
    return fig

def plot_bottom_revenue_products(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if df.empty:
        ax.text(0.5, 0.5, "Không có dữ liệu", ha='center', va='center', fontsize=12)
    else:
        bottom = df.groupby("Product")["Doanh thu"].sum().nsmallest(5)
        bottom.plot(kind="bar", ax=ax, color='#388e3c')
        ax.set_xlabel("Sản Phẩm")
        ax.set_ylabel("Doanh Thu (VNĐ)")
    ax.set_title("Top 5 Sản Phẩm Doanh Thu Thấp")
    return fig