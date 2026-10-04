#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : main.py
Tujuan    : Menjalankan semua modul dan mencetak satu laporan cabang gabungan.
Pembuat   : Sifwah Fatin Sofwani - 2409106072
"""

import identitas
import netconf_modul
import snmp_modul
import ssh_modul
import telemetry_modul


class LaporanCabang:
    def __init__(self, nama, nim, kode_cabang):
        self.nama = nama
        self.nim = nim
        self.kode_cabang = kode_cabang

    def tampilkan_laporan(self, hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry):
        garis = "=" * 60
        print(f"\n{garis}")
        print("LAPORAN AKHIR CABANG")
        print(garis)
        print(f"Nama        : {self.nama}")
        print(f"NIM         : {self.nim}")
        print(f"ID perangkat: {identitas.buat_id_perangkat('router', 1)}")

        print("\n[1] Hasil SSH")
        print(f"    Status : {hasil_ssh['status']}")
        for perintah, keluaran in hasil_ssh["output"].items():
            print(f"    $ {perintah} -> {keluaran}")
        if hasil_ssh["error"]:
            print(f"    Error  : {hasil_ssh['error']}")

        print("\n[2] Hasil SNMP")
        print(f"    Status  : {hasil_snmp['status']}")
        print(f"    sysName : {hasil_snmp['sysName']}")
        if hasil_snmp["error"]:
            print(f"    Error   : {hasil_snmp['error']}")

        print("\n[3] Pesan NETCONF yang dibuat")
        print(pesan_netconf)

        print("\n[4] Klasifikasi Telemetry")
        for item in hasil_telemetry:
            print(f"    {item['perangkat']}: {item['cpuUsage']}% -> {item['status']}")
        print(garis)


def main():
    hasil_ssh = ssh_modul.cek_ssh()
    hasil_snmp = snmp_modul.cek_snmp()
    pesan_netconf = netconf_modul.buat_pesan_netconf()
    hasil_telemetry = telemetry_modul.klasifikasi_telemetry()

    laporan = LaporanCabang(identitas.nama, identitas.nim, identitas.kode_cabang)
    laporan.tampilkan_laporan(hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry)


if __name__ == "__main__":
    main()