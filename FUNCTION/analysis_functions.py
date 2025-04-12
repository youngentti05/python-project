import pandas as pd

def calculate_total_revenue(df):
    if df.empty:
        return 0
    return df['Doanh thu'].sum()

def revenue_by_month(df):
    if df.empty:
        return pd.DataFrame(columns=['Tháng', 'Doanh thu'])
    df['Tháng'] = pd.to_datetime(df['Ngày']).dt.to_period('M')
    return df.groupby('Tháng')['Doanh thu'].sum().reset_index()

def predict_revenue(df):
    if df.empty:
        return "Không có dữ liệu để dự đoán"
    df['Tháng'] = pd.to_datetime(df['Ngày']).dt.to_period('M')
    monthly_avg = df.groupby('Tháng')['Doanh thu'].sum().mean()
    return f"Dự đoán doanh thu tháng tiếp theo: {monthly_avg:,.0f} VNĐ"

def top_5_best_selling(df):
    if df.empty:
        return pd.DataFrame(columns=['Product', 'Số lượng'])
    return df.groupby('Product')['Quantity Ordered'].sum().nlargest(5).reset_index()

def bottom_5_worst_selling(df):
    if df.empty:
        return pd.DataFrame(columns=['Product', 'Số lượng'])
    return df.groupby('Product')['Quantity Ordered'].sum().nsmallest(5).reset_index()

def revenue_by_city(df):
    if df.empty:
        return pd.DataFrame(columns=['Thành phố', 'Doanh thu'])
    return df.groupby('Thành phố')['Doanh thu'].sum().sort_values(ascending=False).reset_index()

def revenue_by_hour(df):
    if df.empty:
        return pd.DataFrame(columns=['Giờ', 'Doanh thu'])
    df['Giờ'] = pd.to_datetime(df['Thời gian']).dt.hour
    return df.groupby('Giờ')['Doanh thu'].sum().reset_index()

def top_revenue_day(df):
    if df.empty:
        return pd.DataFrame(columns=['Ngày', 'Doanh thu'])
    return df.groupby('Ngày')['Doanh thu'].sum().sort_values(ascending=False).head(5).reset_index()

def detailed_monthly_revenue(df):
    if df.empty:
        return pd.DataFrame(columns=['Tháng', 'Doanh thu'])
    df['Tháng'] = pd.to_datetime(df['Ngày']).dt.to_period('M')
    return df.groupby('Tháng')['Doanh thu'].sum().reset_index()

def top_5_highest_revenue_products(df):
    if df.empty:
        return pd.DataFrame(columns=['Product', 'Doanh thu'])
    return df.groupby('Product')['Doanh thu'].sum().nlargest(5).reset_index()

def bottom_5_lowest_revenue_products(df):
    if df.empty:
        return pd.DataFrame(columns=['Product', 'Doanh thu'])
    return df.groupby('Product')['Doanh thu'].sum().nsmallest(5).reset_index()