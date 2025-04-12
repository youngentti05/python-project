import tkinter as tk
from tkinter import messagebox
import os
from GUI.sidebar import SidebarGUI
from GUI.maincontent import MainContentGUI
from data import data_loader

class TrangChuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Phân Tích Doanh Thu Cửa Hàng")
        self.root.geometry("1100x700")
        self.root.configure(bg='#f0f2f5')

        # Biến lưu trữ dữ liệu
        self.data = None

        # Thanh tiêu đề
        header_frame = tk.Frame(self.root, bg='#2c3e50')
        header_frame.pack(side="top", fill="x")
        tk.Label(
            header_frame, text="Phân Tích Doanh Thu Cửa Hàng Tiện Lợi",
            font=("Arial", 16, "bold"), fg="white", bg='#2c3e50'
        ).pack(pady=10)

        # Nút nạp file
        tk.Button(
            header_frame, text="Nạp File CSV", command=self.load_file,
            bg="#3498db", fg="white", font=("Arial", 10)
        ).pack(pady=5)

        # Sidebar frame
        self.sidebar_frame = tk.Frame(self.root, bg='#2c3e50')
        self.sidebar_frame.pack(side="left", fill="y")

        # Content frame
        self.content_frame = tk.Frame(self.root, bg='#e8f5e9')
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Khởi tạo main content và sidebar
        self.main_content = MainContentGUI(self.content_frame)
        self.main_content.pack(fill="both", expand=True)

        self.sidebar = SidebarGUI(self.sidebar_frame, self.handle_sidebar_select)
        self.sidebar.pack(fill="y", expand=True)

    def load_file(self):
        file_path = os.path.join("data", "sales_data", "sales_data.csv")
        if not os.path.exists(file_path):
            self.data = None
            self.sidebar.update_data(None)
            self.main_content.display_result(None, None)
            messagebox.showerror("Lỗi", f"File không tồn tại: {file_path}")
            return

        try:
            self.data = data_loader.load_sales_data(file_path)
            if self.data.empty or len(self.data) == 0:
                self.data = None
                raise ValueError("Dữ liệu rỗng hoặc không hợp lệ.")
            self.sidebar.update_data(self.data)
            self.main_content.display_result(None, self.data)
            messagebox.showinfo("Thành công", f"Đã nạp file: {os.path.basename(file_path)}")
        except Exception as e:
            self.data = None
            self.sidebar.update_data(None)
            self.main_content.display_result(None, None)
            messagebox.showerror("Lỗi", f"Không thể nạp file: {str(e)}")

    def handle_sidebar_select(self, key):
        self.main_content.display_result(key, self.data)