import tkinter as tk
import threading
import os
from tkinter import messagebox, filedialog
from pywinauto.application import Application
import time
import pygetwindow as gw
import pyautogui
from pynput.keyboard import Controller, Key
import customtkinter as ctk
from utils.startup import open_xactimate, get_xactimate_window
from config.keyboard import keyboard
from utils.end import close_xactimate
from utils.process import new_project
from data.autofill import autoFill
from pdf.pdftotext import extract_text_from_pdf, force_ocr_on_pdf
from utils.speak import speak


class XactimateAutomationGUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Xactimate Automation")
        self.root.geometry("500x400")
        self.jsonData = None

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root.eval("tk::PlaceWindow . center")

        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.upload_button = ctk.CTkButton(
            self.main_frame, text="Upload PDFs", command=self.upload_pdfs, height=40
        )
        self.upload_button.pack(pady=(20, 10))

        # Create a frame for the file list
        self.files_frame = ctk.CTkFrame(self.main_frame)
        self.files_frame.pack(pady=10, fill="both", expand=True)

        self.files_label = ctk.CTkLabel(
            self.files_frame, text="No files selected", wraplength=400
        )
        self.files_label.pack(pady=5)

        self.start_button = ctk.CTkButton(
            self.main_frame,
            text="Start Automation",
            command=self.start_automation,
            height=40,
        )
        self.start_button.pack(pady=10)

        self.automation_checkbox = ctk.CTkCheckBox(
            self.main_frame, text="Export ESX", command=self.checkbox_event
        )
        self.automation_checkbox.pack(pady=10)

        self.status_label = ctk.CTkLabel(
            self.main_frame, text="Ready to start", wraplength=400
        )
        self.status_label.pack(pady=10)

        self.pdf_paths = []
        self.exportESX = False

    def checkbox_event(self):
        self.exportESX = self.automation_checkbox.get()

    def upload_pdfs(self):
        new_pdf_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        if new_pdf_paths:
            self.pdf_paths = list(new_pdf_paths)
            if len(self.pdf_paths) > 1:
                # If multiple PDFs are selected, force enable Export ESX
                self.automation_checkbox.select()
                self.exportESX = False
                self.automation_checkbox.configure(state="disabled")
            else:
                self.automation_checkbox.configure(state="normal")

            # Update files list display
            files_text = "Selected files:\n" + "\n".join(
                [os.path.basename(path) for path in self.pdf_paths]
            )
            self.files_label.configure(text=files_text)
            self.status_label.configure(text=f"{len(self.pdf_paths)} PDF(s) uploaded")

    def start_automation(self):
        if not self.pdf_paths:
            self.status_label.configure(text="No PDFs uploaded")
            messagebox.showerror("Error", "No PDFs uploaded")
            return

        self.start_button.configure(state="disabled")
        self.status_label.configure(text="Automation in progress...")
        thread = threading.Thread(target=self.run_automation)
        thread.daemon = True
        thread.start()

    def run_automation(self):
        total_files = len(self.pdf_paths)

        for index, pdf_path in enumerate(self.pdf_paths):
            current_file = os.path.basename(pdf_path)
            self.status_label.configure(
                text=f"Processing {current_file} ({index + 1}/{total_files})..."
            )
            self.root.update_idletasks()

            # For multiple PDFs, always export ESX
            current_export_esx = True if len(self.pdf_paths) > 1 else self.exportESX

            # Get data from PDF
            self.status_label.configure(text=f"Getting data from {current_file}...")
            text = force_ocr_on_pdf(pdf_path)
            data = extract_text_from_pdf(text)
            # Open Xactimate once
            open_xactimate()
            window = get_xactimate_window()

            if not window:
                self.status_label.configure(text="Failed to find Xactimate window")
                self.start_button.configure(state="normal")
                return
            # Create a new project for each PDF
            new_project()

            # Process the PDF data
            self.status_label.configure(
                text=f"Processing {current_file} in Xactimate..."
            )
            autoFill(data, text, current_export_esx)

            # Don't close Xactimate between files, only after the last one
            if index < total_files - 1:
                self.status_label.configure(
                    text=f"Completed {current_file}. Moving to next file..."
                )
                time.sleep(2)  # Small delay between projects

        # Close Xactimate after processing all files
        close_xactimate()
        self.status_label.configure(
            text=f"Successfully processed {total_files} PDF(s)!"
        )
        self.start_button.configure(state="normal")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    speak("Welcome to Xactimate Automation")
    app = XactimateAutomationGUI()
    app.run()
