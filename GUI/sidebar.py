import tkinter as tk
from tkinter import ttk

class SidebarGUI(tk.Frame):
    def __init__(self, parent, on_menu_click):
        super().__init__(parent, bg='#2c3e50')  # Đồng bộ với trang_chuGUI
        self.on_menu_click = on_menu_click
        self.data = None

        # Tiêu đề
        tk.Label(
            self, text="CHỨC NĂNG",
            font=('Arial', 14, 'bold'), bg='#2c3e50', fg='white'
        ).pack(pady=10, fill='x')

        # Danh sách nút chức năng
        buttons = [
            ("Tổng Doanh Thu", "revenue"),
            ("Doanh Thu Theo Tháng", "monthly"),
            ("Dự Đoán Doanh Thu", "predict"),
            ("Top 5 SP Bán Chạy", "top_products"),
            ("Top 5 SP Kém Bán", "bottom_products"),
            ("Doanh Thu Theo TP", "by_city"),
            ("Doanh Thu Theo Giờ", "by_hour"),
            ("Ngày Doanh Thu Cao", "top_days"),
            ("Doanh Thu Từng Tháng", "monthly_revenue"),
            ("Top 5 SP Doanh Thu Cao", "top_revenue_products"),
            ("Top 5 SP Doanh Thu Thấp", "bottom_revenue_products")
        ]

        for text, key in buttons:
            self.create_button(text, key)

        # Phân cách
        separator = ttk.Separator(self, orient='horizontal')
        separator.pack(fill='x', pady=10, padx=10)

    def create_button(self, text, key):
        button = tk.Button(
            self,
            text=text,
            font=('Arial', 12),
            bg='#34495e', fg='white',
            activebackground='#388e3c', activeforeground='white',
            relief='flat',
            command=lambda: self.on_menu_click(key) if self.data else self.show_warning()
        )
        button.pack(fill='x', padx=10, pady=5)
        # Hiệu ứng hover
        button.bind("<Enter>", lambda e: button.config(bg='#3f5a7a'))
        button.bind("<Leave>", lambda e: button.config(bg='#34495e'))

    def update_data(self, data):
        """Cập nhật trạng thái dữ liệu."""
        self.data = data

    def show_warning(self):
        """Hiển thị cảnh báo nếu chưa có dữ liệu."""
        from tkinter import messagebox
        messagebox.showwarning("Chưa có dữ liệu", "Vui lòng chọn file CSV trước!")