#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : netconf_modul.py
Tujuan    : Membangun pesan XML <rpc><edit-config> untuk membuat VLAN.
Pembuat   : Sifwah Fatin Sofwani - 2409106072
"""

import xml.etree.ElementTree as ET

from identitas import kode_cabang

# TRANSPORT layer: NETCONF berjalan di atas SSH (port 830). Di UTS ini tidak
# dijalankan, kita hanya membangun isi pesannya.
NS_NETCONF = "urn:ietf:params:xml:ns:netconf:base:1.0"
NS_VLAN = "http://www.huawei.com/netconf/vrp"


def buat_pesan_netconf():
    # MESSAGES layer: elemen <rpc> pembungkus + message-id
    rpc = ET.Element("rpc", {"xmlns": NS_NETCONF, "message-id": "101"})

    # OPERATIONS layer: operasi <edit-config> pada datastore running
    edit = ET.SubElement(rpc, "edit-config")
    target = ET.SubElement(edit, "target")
    ET.SubElement(target, "running")

    # CONTENT layer: data konfigurasi (VLAN dengan ID = kode_cabang)
    config = ET.SubElement(edit, "config")
    vlan_root = ET.SubElement(config, "vlan", {"xmlns": NS_VLAN})
    vlans = ET.SubElement(vlan_root, "vlans")
    vlan = ET.SubElement(vlans, "vlan", {"operation": "create"})
    ET.SubElement(vlan, "vlanId").text = kode_cabang
    ET.SubElement(vlan, "vlanName").text = f"VLAN_{kode_cabang}"

    ET.indent(rpc)   # Python 3.9+
    return ET.tostring(rpc, encoding="unicode")


if __name__ == "__main__":
    print(buat_pesan_netconf())