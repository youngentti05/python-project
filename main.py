import sys
import os
# Thêm thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import tkinter as tk
from GUI.trang_chu import TrangChuGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = TrangChuGUI(root)
    root.mainloop()