import pandas as pd

def calculate_total_revenue(df):
    if df.empty:
        return 0
    return df['Thành tiền'].sum()

def revenue_by_month(df):
    if df.empty:
        return pd.DataFrame(columns=['Tháng', 'Doanh thu'])
    df['Ngày bán'] = pd.to_datetime(df['Ngày bán'], format='%Y-%m-%d %H:%M', errors='coerce')
    df['Tháng'] = df['Ngày bán'].dt.strftime('%m-%Y') 
    result = df.groupby('Tháng')['Thành tiền'].sum().reset_index()
    result.columns = ['Tháng', 'Doanh thu']
    return result

def predict_revenue(df):
    if df.empty:
        return "Không có dữ liệu để dự đoán"
    df['Ngày bán'] = pd.to_datetime(df['Ngày bán'], format='%Y-%m-%d %H:%M', errors='coerce')
    df['Tháng'] = df['Ngày bán'].dt.to_period('M')
    monthly_avg = df.groupby('Tháng')['Thành tiền'].sum().mean()
    return monthly_avg 

def top_5_best_selling(df):
    if df.empty:
        return pd.DataFrame(columns=['Product', 'Số lượng'])
    result = df.groupby('Tên mặt hàng')['Số lượng'].sum().nlargest(5).reset_index()
    result.columns = ['Product', 'Số lượng']
    return result

def bottom_5_worst_selling(df):
    if df.empty:
        return pd.DataFrame(columns=['Product', 'Số lượng'])
    result = df.groupby('Tên mặt hàng')['Số lượng'].sum().nsmallest(5).reset_index()
    result.columns = ['Product', 'Số lượng']
    return result

def revenue_by_city(df):
    if df.empty:
        return pd.DataFrame(columns=['Thành phố', 'Doanh thu'])
    result = df.groupby('Thành phố')['Thành tiền'].sum().sort_values(ascending=False).reset_index()
    result.columns = ['Thành phố', 'Doanh thu']
    return result

def revenue_by_hour(df):
    if df.empty:
        return pd.DataFrame(columns=['Giờ', 'Doanh thu'])
    df['Ngày bán'] = pd.to_datetime(df['Ngày bán'], format='%Y-%m-%d %H:%M', errors='coerce')
    df['Giờ'] = df['Ngày bán'].dt.hour
    result = df.groupby('Giờ')['Thành tiền'].sum().reset_index()
    result.columns = ['Giờ', 'Doanh thu']
    return result

def top_revenue_day(df):
    if df.empty:
        return pd.DataFrame(columns=['Ngày', 'Doanh thu'])
    df['Ngày bán'] = pd.to_datetime(df['Ngày bán'], format='%Y-%m-%d %H:%M', errors='coerce')
    result = df.groupby(df['Ngày bán'].dt.date)['Thành tiền'].sum().sort_values(ascending=False).head(5).reset_index()
    result.columns = ['Ngày', 'Doanh thu']
    return result

def detailed_monthly_revenue(df):
    if df.empty:
        return pd.DataFrame(columns=['Tháng', 'Doanh thu'])
    df['Ngày bán'] = pd.to_datetime(df['Ngày bán'], format='%Y-%m-%d %H:%M', errors='coerce')
    df['Tháng'] = df['Ngày bán'].dt.strftime('%m-%Y')
    result = df.groupby('Tháng')['Thành tiền'].sum().reset_index()
    result.columns = ['Tháng', 'Doanh thu']
    return result

def top_5_highest_revenue_products(df):
    if df.empty:
        return pd.DataFrame(columns=['Product', 'Doanh thu'])
    result = df.groupby('Tên mặt hàng')['Thành tiền'].sum().nlargest(5).reset_index()
    result.columns = ['Product', 'Doanh thu']
    return result

def bottom_5_lowest_revenue_products(df):
    if df.empty:
        return pd.DataFrame(columns=['Product', 'Doanh thu'])
    result = df.groupby('Tên mặt hàng')['Thành tiền'].sum().nsmallest(5).reset_index()
    result.columns = ['Product', 'Doanh thu']
    return result

def most_used_payment_method(df):
    if df.empty:
        return pd.DataFrame(columns=['Phương thức thanh toán', 'Số lần sử dụng'])
    result = df['Phương thức thanh toán'].value_counts().reset_index()
    result.columns = ['Phương thức thanh toán', 'Số lần sử dụng']
    return result
