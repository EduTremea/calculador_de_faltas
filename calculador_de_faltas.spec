# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['calculador_de_faltas.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\luiz.tremea\\Documents\\Anotações\\Códigos\\calculador_de_faltas\\numero_valido.jpg', '.'), ('C:\\Users\\luiz.tremea\\Documents\\Anotações\\Códigos\\calculador_de_faltas\\pode_faltar.jpg', '.'), ('C:\\Users\\luiz.tremea\\Documents\\Anotações\\Códigos\\calculador_de_faltas\\nao_pode_faltar.jpg', '.'), ('C:\\Users\\luiz.tremea\\Documents\\Anotações\\Códigos\\calculador_de_faltas\\reprovo.jpg', '.')],
    hiddenimports=[],
    hookspath=[],
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
    name='calculador_de_faltas',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
