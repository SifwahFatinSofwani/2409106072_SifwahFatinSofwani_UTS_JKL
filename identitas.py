#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : identitas.py
Tujuan    : Menyimpan identitas cabang virtual dan membuat ID perangkat.
Pembuat   : Sifwah Fatin Sofwani - 2409106072
"""

nim = "2409106072"
nama = "Sifwah Fatin Sofwani"
kode_cabang = nim[-3:]


def buat_id_perangkat(jenis, nomor):
    """Contoh hasil: buat_id_perangkat('router', 1) -> 'ROUTER-072-01'"""
    return f"{jenis.upper()}-{kode_cabang}-{int(nomor):02d}"


if __name__ == "__main__":
    print(f"Nama        : {nama}")
    print(f"NIM         : {nim}")
    print(f"Kode cabang : {kode_cabang}")
    print(f"ID perangkat: {buat_id_perangkat('router', 1)}")