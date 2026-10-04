#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : telemetry_modul.py
Tujuan    : Menyimpan sampel data cpuUsage (hasil decode GPB) dan
            mengklasifikasikannya menjadi KRITIS / WASPADA / NORMAL.
Pembuat   : Sifwah Fatin Sofwani - 2409106072
"""

from identitas import nim

# Nilai diturunkan dari digit NIM (dibuat bervariasi agar ketiga kelas muncul):
#   router-A: 2 digit terakhir NIM mod 50                 -> 0..49  (NORMAL)
#   router-B: 50 + (digit ke-3 & 4 dari belakang) mod 31  -> 50..80 (WASPADA)
#   router-C: 81 + (jumlah seluruh digit NIM) mod 19      -> 81..99 (KRITIS)
data_telemetry = {
    "router-A": {"cpuUsage": int(nim[-2:]) % 50},
    "router-B": {"cpuUsage": 50 + int(nim[-4:-2]) % 31},
    "router-C": {"cpuUsage": 81 + sum(int(d) for d in nim) % 19},
}


def klasifikasi_telemetry():
    hasil = []
    for perangkat, isi in data_telemetry.items():
        cpu = isi["cpuUsage"]
        if cpu > 80:
            status = "KRITIS"
        elif cpu >= 50:
            status = "WASPADA"
        else:
            status = "NORMAL"
        hasil.append({"perangkat": perangkat, "cpuUsage": cpu, "status": status})
        print(f"[TELEMETRY] {perangkat}: cpuUsage={cpu}% -> {status}")
    return hasil


if __name__ == "__main__":
    klasifikasi_telemetry()