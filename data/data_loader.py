import pandas as pd
import os
import logging

# Thiết lập logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def validate_csv(file_path):
    """
    Kiểm tra file CSV có đủ cột bắt buộc không.
    Trả về True nếu hợp lệ, False nếu không.
    """
    required_columns = ['Order ID', 'Product', 'Quantity Ordered', 'Price Each', 'Order Date', 'Purchase Address']
    try:
        df = pd.read_csv(file_path)
        missing_columns = set(required_columns) - set(df.columns)
        if missing_columns:
            logging.error(f"File {file_path} thiếu cột: {missing_columns}")
            return False
        return True
    except Exception as e:
        logging.error(f"Lỗi khi kiểm tra file {file_path}: {e}")
        return False

def load_single_file(file_path):
    """
    Tải và làm sạch một file CSV bán hàng.
    Trả về DataFrame hoặc DataFrame rỗng nếu lỗi.
    """
    if not os.path.exists(file_path):
        logging.warning(f"File không tồn tại: {file_path}")
        return pd.DataFrame()

    if not validate_csv(file_path):
        logging.warning(f"File không hợp lệ: {file_path}")
        return pd.DataFrame()

    try:
        df = pd.read_csv(file_path)
        df.columns = [col.strip() for col in df.columns]

        # Đổi tên cột (nếu cần)
        rename_map = {
            'Quantity O': 'Quantity Ordered',  # Sửa lỗi chính tả nếu có
        }
        df.rename(columns=rename_map, inplace=True)

        # Xóa hàng trống
        initial_rows = len(df)
        df.dropna(inplace=True)
        dropped_rows = initial_rows - len(df)
        if dropped_rows > 0:
            logging.info(f"Đã xóa {dropped_rows} hàng trống trong {file_path}")

        # Chuyển đổi kiểu dữ liệu
        df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'], errors='coerce')
        df['Price Each'] = pd.to_numeric(df['Price Each'], errors='coerce')
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

        # Xóa hàng lỗi
        initial_rows = len(df)
        df.dropna(subset=['Quantity Ordered', 'Price Each', 'Order Date', 'Product'], inplace=True)
        dropped_rows = initial_rows - len(df)
        if dropped_rows > 0:
            logging.info(f"Đã xóa {dropped_rows} hàng lỗi trong {file_path}")

        if df.empty:
            logging.warning(f"File {file_path} không có dữ liệu hợp lệ sau khi làm sạch")
            return pd.DataFrame()

        # Tạo cột mới để đồng bộ với analysis_functions
        df['Doanh thu'] = df['Quantity Ordered'] * df['Price Each']
        df['Ngày'] = df['Order Date'].dt.date
        df['Thời gian'] = df['Order Date']
        df['Thành phố'] = df['Purchase Address'].apply(
            lambda x: x.split(',')[-2].strip() if isinstance(x, str) and len(x.split(',')) >= 2 else 'Không xác định'
        )

        logging.info(f"Tải thành công: {file_path} ({len(df)} dòng)")
        return df

    except Exception as e:
        logging.error(f"Lỗi khi nạp file {file_path}: {e}")
        return pd.DataFrame()

def load_multiple_files(file_paths):
    """
    Tải nhiều file CSV, trả về DataFrame gộp lại toàn bộ.
    """
    all_dataframes = []

    for path in file_paths:
        df = load_single_file(path)
        if not df.empty:
            all_dataframes.append(df)

    if all_dataframes:
        combined_df = pd.concat(all_dataframes, ignore_index=True)
        logging.info(f"Gộp {len(all_dataframes)} file thành {len(combined_df)} dòng")
        return combined_df
    else:
        logging.warning("Không có dữ liệu nào được tải.")
        return pd.DataFrame()

def load_sales_data(file_or_files):
    """
    Hàm tổng quát để tải dữ liệu: có thể là một file hoặc nhiều file.
    """
    if isinstance(file_or_files, str):
        return load_single_file(file_or_files)
    elif isinstance(file_or_files, (list, tuple)):
        return load_multiple_files(file_or_files)
    else:
        logging.error("Đầu vào không hợp lệ cho load_sales_data.")
        return pd.DataFrame()