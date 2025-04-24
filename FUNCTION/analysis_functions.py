import pandas as pd

def calculate_total_revenue(df):
    if df.empty:
        return 0
    return df['Thành tiền'].sum()

def revenue_by_month(df):
    if df.empty:
        return pd.DataFrame(columns=['Tháng', 'Doanh thu'])
    df['Tháng'] = pd.to_datetime(df['Ngày bán']).dt.to_period('M')
    return df.groupby('Tháng')['Thành tiền'].sum().reset_index(name='Doanh thu')

def predict_revenue(df):
    if df.empty:
        return "Không có dữ liệu để dự đoán"
    df['Tháng'] = pd.to_datetime(df['Ngày bán']).dt.to_period('M')
    monthly_avg = df.groupby('Tháng')['Thành tiền'].sum().mean()
    return f"Dự đoán doanh thu tháng tiếp theo: {monthly_avg:,.0f} VNĐ"

def top_5_best_selling(df):
    if df.empty:
        return pd.DataFrame(columns=['Tên mặt hàng', 'Số lượng'])
    return df.groupby('Tên mặt hàng')['Số lượng'].sum().nlargest(5).reset_index()

def bottom_5_worst_selling(df):
    if df.empty:
        return pd.DataFrame(columns=['Tên mặt hàng', 'Số lượng'])
    return df.groupby('Tên mặt hàng')['Số lượng'].sum().nsmallest(5).reset_index()

def revenue_by_city(df):
    # Không có cột thành phố, nên trả về DataFrame trống
    return pd.DataFrame(columns=['Thành phố', 'Doanh thu'])

def revenue_by_hour(df):
    if df.empty:
        return pd.DataFrame(columns=['Giờ', 'Doanh thu'])
    df['Giờ'] = pd.to_datetime(df['Ngày bán']).dt.hour
    return df.groupby('Giờ')['Thành tiền'].sum().reset_index(name='Doanh thu')

def top_revenue_day(df):
    if df.empty:
        return pd.DataFrame(columns=['Ngày', 'Doanh thu'])
    return df.groupby('Ngày bán')['Thành tiền'].sum().sort_values(ascending=False).head(5).reset_index(name='Doanh thu')

def detailed_monthly_revenue(df):
    if df.empty:
        return pd.DataFrame(columns=['Tháng', 'Doanh thu'])
    df['Tháng'] = pd.to_datetime(df['Ngày bán']).dt.to_period('M')
    return df.groupby('Tháng')['Thành tiền'].sum().reset_index(name='Doanh thu')

def top_5_highest_revenue_products(df):
    if df.empty:
        return pd.DataFrame(columns=['Tên mặt hàng', 'Doanh thu'])
    return df.groupby('Tên mặt hàng')['Thành tiền'].sum().nlargest(5).reset_index()

def bottom_5_lowest_revenue_products(df):
    if df.empty:
        return pd.DataFrame(columns=['Tên mặt hàng', 'Doanh thu'])
    return df.groupby('Tên mặt hàng')['Thành tiền'].sum().nsmallest(5).reset_index()
