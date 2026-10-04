#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : ssh_modul.py
Tujuan    : Login SSH ke VM dengan Paramiko dan menjalankan perintah diagnostik.
Pembuat   : Sifwah Fatin Sofwani - 2409106072
"""

import getpass
import os

import paramiko

from identitas import kode_cabang

HOST = os.environ.get("SSH_HOST", "127.0.0.1")
PORT = int(os.environ.get("SSH_PORT", "2222"))
USERNAME = f"admin_{kode_cabang}"
PERINTAH = ["hostname", "uname -a", "uptime"]


def cek_ssh():
    hasil = {"status": "GAGAL", "output": {}, "error": None}
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        password = os.environ.get("SSH_PASSWORD") or getpass.getpass(
            f"Password SSH untuk {USERNAME}: "
        )
        client.connect(HOST, port=PORT, username=USERNAME,
                       password=password, timeout=10)
        print(f"[SSH] Terhubung ke {HOST} sebagai {USERNAME}")

        for perintah in PERINTAH:
            stdin, stdout, stderr = client.exec_command(perintah)
            keluaran = stdout.read().decode().strip()
            hasil["output"][perintah] = keluaran
            print(f"[SSH] $ {perintah}\n      {keluaran}")

        hasil["status"] = "BERHASIL"
    except Exception as e:
        hasil["error"] = str(e)
        print(f"[SSH] Koneksi gagal: {e}")
    finally:
        client.close()

    return hasil


if __name__ == "__main__":
    cek_ssh()
