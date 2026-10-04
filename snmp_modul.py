#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : snmp_modul.py
Tujuan    : Mengambil sysName (OID 1.3.6.1.2.1.1.5.0) lewat SNMPv2c.
Pembuat   : Sifwah Fatin Sofwani - 2409106072
"""

import asyncio
import os

from pysnmp.hlapi import (CommunityData, ContextData, ObjectIdentity,
                          ObjectType, SnmpEngine, UdpTransportTarget, getCmd)

from identitas import kode_cabang

HOST = os.environ.get("SNMP_HOST", "127.0.0.1")
PORT = int(os.environ.get("SNMP_PORT", "1161"))
COMMUNITY = f"comm_{kode_cabang}"
OID_SYSNAME = "1.3.6.1.2.1.1.5.0"


def cek_snmp():
    hasil = {"status": "GAGAL", "sysName": None, "error": None}

    # Python 3.12+ tidak membuat event loop otomatis, jadi dibuat manual
    asyncio.set_event_loop(asyncio.new_event_loop())
    engine = SnmpEngine()

    try:
        errorIndication, errorStatus, errorIndex, varBinds = getCmd(
            engine,
            CommunityData(COMMUNITY, mpModel=1),        # mpModel=1 -> SNMPv2c
            UdpTransportTarget((HOST, PORT), timeout=3, retries=1),
            ContextData(),
            ObjectType(ObjectIdentity(OID_SYSNAME)),
        )

        if errorIndication:
            raise RuntimeError(str(errorIndication))
        if errorStatus:
            raise RuntimeError(errorStatus.prettyPrint())

        for oid, nilai in varBinds:
            hasil["sysName"] = str(nilai)
            print(f"[SNMP] {oid.prettyPrint()} = {nilai.prettyPrint()}")
        hasil["status"] = "BERHASIL"
    except Exception as e:
        hasil["error"] = str(e)
        print(f"[SNMP] Gagal mengambil sysName: {e}")
    finally:
        # Tutup dispatcher agar tidak ada task yang tertinggal
        try:
            engine.transportDispatcher.closeDispatcher()
        except Exception:
            pass

    return hasil


if __name__ == "__main__":
    cek_snmp()