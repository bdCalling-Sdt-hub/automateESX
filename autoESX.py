import json
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
        self.root.geometry("400x300")
        self.jsonData = None
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.root.eval("tk::PlaceWindow . center")

        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.upload_button = ctk.CTkButton(
            self.main_frame,
            text="Upload PDF",
            command=self.upload_pdf,
            height=40
        )
        self.upload_button.pack(pady=(20, 10))

        self.start_button = ctk.CTkButton(
            self.main_frame,
            text="Start Automation",
            command=self.start_automation,
            height=40
        )
        self.start_button.pack(pady=10)

        self.automation_checkbox = ctk.CTkCheckBox(
            self.main_frame,
            text="Export ESX",
            command=self.checkbox_event
        )
        self.automation_checkbox.pack(pady=10)

        self.status_label = ctk.CTkLabel(
            self.main_frame,
            text="Ready to start",
            wraplength=300
        )
        self.status_label.pack(pady=10)

        self.pdf_path = ""
        
        self.exportESX = False

    def checkbox_event(self):
        self.exportESX = self.automation_checkbox.get()

    def upload_pdf(self):
        self.pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.pdf_path:
            self.status_label.configure(
                text=f"PDF uploaded: {os.path.basename(self.pdf_path)}"
            )

    def start_automation(self):
        self.start_button.configure(state="disabled")
        self.status_label.configure(text="Automation in progress...")
        thread = threading.Thread(target=self.run_automation)
        thread.daemon = True
        thread.start()

    def run_automation(self):
        if not self.pdf_path:
            self.status_label.configure(text="No PDF uploaded")
            messagebox.showerror("Error", "No PDF uploaded")
       
        else:
            self.root.update_idletasks()
            self.status_label.configure(text="Getting data from PDF...")
            text = force_ocr_on_pdf(self.pdf_path)
            data = extract_text_from_pdf(text)
            open_xactimate()
            window = get_xactimate_window()
            if window:
                new_project()
                autoFill(data, text, self.exportESX)
                close_xactimate()
                self.status_label.configure(
                    text="Automation completed successfully!"
                )
            else:
                self.status_label.configure(text="Failed to find Xactimate window")
    
        self.start_button.configure(state="normal")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    speak("Welcome to Xactimate Automation")
    app = XactimateAutomationGUI()
    app.run()