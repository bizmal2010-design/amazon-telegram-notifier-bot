# hook-pandas-fix.py
# يتجاوز hook-pandas.py المعطوب في PyInstaller

hiddenimports = [
    'pandas',
    'pandas._libs',
    'pandas._libs.tslibs',
    'pandas._libs.tslibs.np_datetime',
    'pandas._libs.tslibs.nattype',
    'pandas._libs.tslibs.timedeltas',
    'pandas._libs.tslibs.timestamps',
    'pandas._libs.tslibs.offsets',
    'pandas._libs.tslibs.parsing',
    'pandas._libs.tslibs.period',
    'pandas._libs.tslibs.strptime',
    'pandas._libs.tslibs.tzconversion',
    'pandas._libs.hashtable',
    'pandas._libs.index',
    'pandas._libs.lib',
    'pandas._libs.missing',
    'pandas._libs.reduction',
    'pandas._libs.ops',
    'pandas._libs.sparse',
    'pandas._libs.internals',
    'pandas._libs.interval',
    'pandas._libs.join',
    'pandas._libs.json',
    'pandas._libs.parsers',
    'pandas._libs.reshape',
    'pandas._libs.window',
    'pandas._libs.writers',
    'pandas.core',
    'pandas.core.arrays',
    'pandas.core.indexes',
    'pandas.io',
    'pandas.io.formats',
    'pandas.io.formats.excel',
]

datas = []
excludedimports = []