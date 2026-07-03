# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['pandas', 'pandas.core', 'pandas.io', 'pandas.io.formats', 'pandas.io.formats.excel', 'pandas._libs', 'pandas._libs.tslibs', 'pandas._libs.tslibs.np_datetime', 'pandas._libs.tslibs.nattype', 'pandas._libs.hashtable', 'pandas._libs.index', 'pandas._libs.lib', 'pandas._libs.missing', 'pandas._libs.parsers', 'pandas._libs.join', 'pandas._libs.interval', 'pandas._libs.writers', 'openpyxl', 'openpyxl.styles', 'openpyxl.utils'],
    hookspath=['.'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='AmazonScraper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
