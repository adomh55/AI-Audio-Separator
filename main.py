import os
import subprocess
import sys
import threading
from datetime import datetime
import customtkinter as ctk
from tkinter import filedialog, messagebox

class DemucsGui(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI Audio Separator - Dynamic Output")
        self.geometry("500x350")
        ctk.set_appearance_mode("dark")
        
        # UI Elements
        self.label = ctk.CTkLabel(self, text="AI Audio Separator (Unique Folders)", font=("Arial", 16))
        self.label.pack(pady=20)

        self.file_path_var = ctk.StringVar()
        self.entry = ctk.CTkEntry(self, textvariable=self.file_path_var, width=400)
        self.entry.pack(pady=10)

        self.btn_browse = ctk.CTkButton(self, text="Browse Audio", command=self.browse_file)
        self.btn_browse.pack(pady=5)

        self.btn_run = ctk.CTkButton(self, text="Start Separation", command=self.start_thread, fg_color="green")
        self.btn_run.pack(pady=20)

        self.progress_label = ctk.CTkLabel(self, text="", text_color="yellow")
        self.progress_label.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.flac *.m4a")])
        if file_path:
            self.file_path_var.set(file_path)

    def start_thread(self):
        input_path = self.file_path_var.get().strip()
        if not os.path.exists(input_path):
            messagebox.showerror("Error", "File not found!")
            return
        
        self.btn_run.configure(state="disabled")
        self.progress_label.configure(text="Processing... Check Terminal for details")
        threading.Thread(target=self.run_demucs, args=(input_path,), daemon=True).start()

    def run_demucs(self, input_path):
        # 1. إنشاء اسم مجلد فريد باستخدام الوقت الحالي
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = os.path.join("outputs", f"separated_{timestamp}")
        
        # التأكد من وجود مجلد outputs الرئيسي
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        # 2. بناء الأمر مع تحديد مخرج المجلد -o
        command = [
            sys.executable, "-m", "demucs.separate",
            "-d", "cpu",
            "-o", output_dir, # تحديد مجلد المخرجات الفريد
            input_path
        ]
        
        try:
            subprocess.run(command, check=True)
            self.after(0, lambda: self.finish_success(output_dir))
        except Exception as e:
            self.after(0, lambda: self.finish_error(str(e)))

    def finish_success(self, folder):
        self.btn_run.configure(state="normal")
        self.progress_label.configure(text=f"Saved in: {folder}")
        messagebox.showinfo("Success", f"Process Completed!\nFiles saved in:\n{os.path.abspath(folder)}")

    def finish_error(self, error_msg):
        self.btn_run.configure(state="normal")
        self.progress_label.configure(text="Error occurred.")
        messagebox.showerror("Error", error_msg)

if __name__ == "__main__":
    app = DemucsGui()
    app.mainloop()
