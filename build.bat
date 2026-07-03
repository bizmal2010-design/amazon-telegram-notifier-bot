@echo off
echo ================================================
echo     بناء البرنامج فقط (البيئة جاهزة)
echo ================================================

call myenv\Scripts\activate.bat

echo جاري البناء...
pyinstaller --onefile --windowed ^
  --additional-hooks-dir=. ^
  --hidden-import=pandas ^
  --hidden-import=pandas.core ^
  --hidden-import=pandas.io ^
  --hidden-import=pandas.io.formats ^
  --hidden-import=pandas.io.formats.excel ^
  --hidden-import=pandas._libs ^
  --hidden-import=pandas._libs.tslibs ^
  --hidden-import=pandas._libs.tslibs.np_datetime ^
  --hidden-import=pandas._libs.tslibs.nattype ^
  --hidden-import=pandas._libs.hashtable ^
  --hidden-import=pandas._libs.index ^
  --hidden-import=pandas._libs.lib ^
  --hidden-import=pandas._libs.missing ^
  --hidden-import=pandas._libs.parsers ^
  --hidden-import=pandas._libs.join ^
  --hidden-import=pandas._libs.interval ^
  --hidden-import=pandas._libs.writers ^
  --hidden-import=openpyxl ^
  --hidden-import=openpyxl.styles ^
  --hidden-import=openpyxl.utils ^
  --name "AmazonScraper" main.py

echo.
echo [نسخ المتصفحات...]
xcopy /E /I /Y "%USERPROFILE%\AppData\Local\ms-playwright\chromium-1223" "dist\browsers\chromium-1223"
xcopy /E /I /Y "%USERPROFILE%\AppData\Local\ms-playwright\chromium_headless_shell-1223" "dist\browsers\chromium_headless_shell-1223"

echo.
echo ================================================
echo  انتهى! شغّل البرنامج من: dist\AmazonScraper.exe
echo ================================================
pause