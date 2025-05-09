import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import logging
from data import data_loader
from FUNCTION import analysis_functions
from CHARTS import chart_functions

# Thiết lập logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

class MainContentGUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#e8f5e9')
        self.chart_canvas = None

        # Tiêu đề
        self.label = tk.Label(
            self,
            text="Kết quả phân tích doanh thu",
            font=('Arial', 14, 'bold'),
            bg='#e8f5e9', fg='#388e3c'
        )
        self.label.pack(pady=10, fill='x')

        # Khu vực hiển thị văn bản với thanh cuộn
        text_frame = tk.Frame(self, bg='#e8f5e9')
        text_frame.pack(pady=10, fill='both', expand=True)

        self.result_text = tk.Text(
            text_frame, wrap=tk.WORD, width=60, height=10,
            bg='#f1f8e9', font=('Courier', 11), bd=1, relief='solid'
        )
        self.result_text.pack(side='left', fill='both', expand=True)

        scrollbar = tk.Scrollbar(text_frame, orient='vertical', command=self.result_text.yview)
        scrollbar.pack(side='right', fill='y')
        self.result_text.config(yscrollcommand=scrollbar.set)

        # Định nghĩa ánh xạ chức năng
        self.function_map = {
            "revenue": {
                "analysis": analysis_functions.calculate_total_revenue,
                "chart": chart_functions.plot_total_revenue_bar,
                "format": lambda x: f"Tổng doanh thu: {x:,.0f} VNĐ"
            },
            "monthly": {
                "analysis": analysis_functions.revenue_by_month,
                "chart": chart_functions.plot_monthly_revenue,
                "format": self.format_dataframe
            },
            "predict": {
                "analysis": analysis_functions.predict_revenue,
                "chart": chart_functions.plot_predicted_revenue,
                "format": lambda x: f"Doanh thu dự đoán: {x:,.0f} VNĐ"
            },
            "top_products": {
                "analysis": analysis_functions.top_5_best_selling,
                "chart": chart_functions.plot_top_5_products,
                "format": self.format_dataframe
            },
            "bottom_products": {
                "analysis": analysis_functions.bottom_5_worst_selling,
                "chart": chart_functions.plot_bottom_5_products,
                "format": self.format_dataframe
            },
            "by_city": {
                "analysis": analysis_functions.revenue_by_city,
                "chart": chart_functions.plot_revenue_by_city,
                "format": self.format_dataframe
            },
            "by_hour": {
                "analysis": analysis_functions.revenue_by_hour,
                "chart": chart_functions.plot_revenue_by_hour,
                "format": self.format_dataframe
            },
            "top_days": {
                "analysis": analysis_functions.top_revenue_day,
                "chart": chart_functions.plot_top_revenue_days,
                "format": self.format_dataframe
            },
            "top_revenue_products": {
                "analysis": analysis_functions.top_5_highest_revenue_products,
                "chart": chart_functions.plot_top_revenue_products,
                "format": self.format_dataframe
            },
            "bottom_revenue_products": {
                "analysis": analysis_functions.bottom_5_lowest_revenue_products,
                "chart": chart_functions.plot_bottom_revenue_products,
                "format": self.format_dataframe
            }
        }

    def format_dataframe(self, df):
        if df.empty:
            return "Không có dữ liệu"
        
        # Thêm định dạng số với dấu phẩy để ngăn cách
        formatted_df = df.copy()
        for col in formatted_df.columns:
            if formatted_df[col].dtype in ['int64', 'float64']:
                formatted_df[col] = formatted_df[col].apply(lambda x: f"{x:,.0f}")
        
        # Đổi tên cột
        if 'Product' in formatted_df.columns:
            formatted_df = formatted_df.rename(columns={'Product': 'Sản phẩm'})
        
        COLUMN_PADDING = 10  # Khoảng cách giữa các cột
        
        # Xác định độ rộng max cho từng cột
        col_widths = {}
        for col in formatted_df.columns:
            # Độ rộng là max dựa vào giá trị dài nhất trong cột 
            max_width = max(
                len(str(col)),
                max(len(str(val)) for val in formatted_df[col]) if not formatted_df.empty else 0
            )
            col_widths[col] = max_width
        
        # Tạo chuỗi header
        header = []
        for col in formatted_df.columns:
            header.append(str(col).ljust(col_widths[col] + COLUMN_PADDING))
        header_str = ''.join(header)
        
        # Tạo các dòng dữ liệu
        rows = []
        for _, row in formatted_df.iterrows():
            row_str = []
            for col in formatted_df.columns:
                cell_value = str(row[col])
                row_str.append(cell_value.ljust(col_widths[col] + COLUMN_PADDING))
            rows.append(''.join(row_str))
        
        # Kết hợp header và dữ liệu 
        result = header_str + '\n' + '\n'.join(rows)
        
        return result

    def display_result(self, key, data=None):
        """Hiển thị kết quả văn bản và biểu đồ dựa trên key."""
        logging.info(f"Gọi display_result với key: {key}, data: {'rỗng' if data is None else len(data)} dòng")
        self.result_text.delete(1.0, tk.END)
        if data is None or (hasattr(data, 'empty') and data.empty):
            self.result_text.insert(tk.END, "Vui lòng chọn file dữ liệu hợp lệ trước.")
            if key is not None:
                messagebox.showwarning("Chưa có dữ liệu", "Vui lòng chọn file dữ liệu hợp lệ trước.")
            return

        try:
            if key not in self.function_map:
                self.result_text.insert(tk.END, "Chức năng chưa được hỗ trợ.")
                return

            # Lấy hàm phân tích và định dạng
            func_info = self.function_map[key]
            result = func_info["analysis"](data)
            logging.info(f"Kết quả phân tích cho {key}: {result}")
            formatted_result = func_info["format"](result)

            # Hiển thị văn bản
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, formatted_result)

            # Hiển thị biểu đồ
            fig = func_info["chart"](data)
            if fig:
                self.display_chart(fig)
            else:
                logging.warning(f"Không tạo được biểu đồ cho key: {key}")

        except Exception as e:
            logging.error(f"Lỗi trong display_result: {str(e)}")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Đã xảy ra lỗi: {str(e)}")
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

    def display_chart(self, fig):
        """Hiển thị biểu đồ trong giao diện."""
        if  self.chart_canvas:
            self.chart_canvas.get_tk_widget().destroy()
        self.chart_canvas = FigureCanvasTkAgg(fig, master=self)
        self.chart_canvas.draw()
        self.chart_canvas.get_tk_widget().pack(pady=10, fill='both', expand=True)
