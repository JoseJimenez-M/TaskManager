import pandas as pd
import os
from tkinter import messagebox
from Tasks.db_queries import get_tasks
def create_Report():
    tasks = get_tasks()
    if not tasks:
        messagebox.showinfo("No Data", "There are no tasks to export.")
        return

    df = pd.DataFrame(tasks)
    report_dir = os.path.join(os.path.dirname(__file__), "..", "Report")
    os.makedirs(report_dir, exist_ok=True)
    file_path = os.path.join(report_dir, "task_report.xlsx")

    try:
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Export Successful", f"Tasks exported to:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Export Error", f"Failed to export tasks:\n{str(e)}")