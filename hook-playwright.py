# hook-playwright.py
# ضعه في نفس مجلد main.py
# PyInstaller يستخدمه تلقائياً لتضمين ملفات Playwright

from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('playwright')
