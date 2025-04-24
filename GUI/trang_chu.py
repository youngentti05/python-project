import tkinter as tk
from tkinter import messagebox
import os
from GUI.sidebar import SidebarGUI
from GUI.maincontent import MainContentGUI
from data import data_loader
from tkinter import filedialog

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

    from tkinter import filedialog, messagebox

    def load_file(self):
        # Cho phép người dùng chọn nhiều file CSV
        file_paths = filedialog.askopenfilenames(
            title="Chọn các file dữ liệu",
            filetypes=[("CSV Files", "*.csv")]
        )

        if not file_paths:
            messagebox.showinfo("Thông báo", "Chưa chọn file nào.")
            return

        try:
            self.data = data_loader.load_sales_data(file_paths)

            if self.data.empty:
                self.data = None
                raise ValueError("Không có dữ liệu hợp lệ trong các file đã chọn.")

            self.sidebar.update_data(self.data)
            self.main_content.display_result(None, self.data)

            file_names = ", ".join([os.path.basename(fp) for fp in file_paths])
            messagebox.showinfo("Thành công", f"Đã nạp {len(file_paths)} file: {file_names}")

        except Exception as e:
            self.data = None
            self.sidebar.update_data(None)
            self.main_content.display_result(None, None)
            messagebox.showerror("Lỗi", f"Không thể nạp dữ liệu: {str(e)}")


    def handle_sidebar_select(self, key):
        self.main_content.display_result(key, self.data)