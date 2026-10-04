# UTS Jaringan Komputer Lanjut - Integration Network with Python

Nama : Sifwah Fatin Sofwani
NIM  : 2409106072
Kelas: B 2024, Informatika, Universitas Mulawarman

## Tentang project

Ini project UTS Jaringan Komputer Lanjut. Isinya satu program Python yang dipecah jadi beberapa modul: identitas cabang, akses SSH, monitoring SNMP, pembuatan pesan NETCONF, dan klasifikasi data telemetry. Semuanya dijalankan dari `main.py`, lalu hasilnya dicetak jadi satu laporan akhir.

Untuk SSH dan SNMP, targetnya VM Ubuntu Server di VirtualBox. NETCONF dan telemetry tidak butuh perangkat asli. NETCONF cuma membuat pesan XML-nya, dan telemetry memakai data sampel.

## Struktur folder

```
2409106072_SifwahFatinSofwani_UTS_JKL/
├── .gitignore
├── README.md
├── main.py
├── identitas.py
├── ssh_modul.py
├── snmp_modul.py
├── netconf_modul.py
└── telemetry_modul.py
```

- `identitas.py` berisi nim, nama, kode cabang, dan function `buat_id_perangkat()`.
- `ssh_modul.py` berisi `cek_ssh()`. Function ini login ke VM pakai Paramiko lalu menjalankan `hostname`, `uname -a`, dan `uptime`.
- `snmp_modul.py` berisi `cek_snmp()`. Function ini mengambil `sysName` lewat SNMPv2c.
- `netconf_modul.py` berisi `buat_pesan_netconf()`. Function ini membuat XML `<rpc><edit-config>` untuk membuat VLAN, dan di kodenya ada komentar yang menandai bagian messages, operations, dan content layer.
- `telemetry_modul.py` berisi `klasifikasi_telemetry()`. Function ini memberi status tiap sampel cpuUsage: di atas 80 KRITIS, 50 sampai 80 WASPADA, di bawah 50 NORMAL.
- `main.py` memanggil semua function di atas, lalu mencetak laporan lewat class `LaporanCabang`.

## Persiapan

Yang dibutuhkan:
- Python 3.9 atau lebih baru
- VM Ubuntu dengan `openssh-server` dan `snmpd` yang sudah aktif
- Library: paramiko, pysnmp-lextudio, pyasn1

Di VM, saya membuat akun SSH `admin_072` dan mengatur community SNMP `comm_072` di `snmpd.conf`. Jaringan VM memakai NAT dengan port forwarding: TCP 2222 ke 22 untuk SSH dan UDP 1161 ke 161 untuk SNMP. Jadi dari Windows, VM diakses lewat `127.0.0.1`.

Kalau jaringan VM kamu beda, alamat dan portnya bisa diganti lewat environment variable `SSH_HOST`, `SSH_PORT`, `SNMP_HOST`, dan `SNMP_PORT`. Password SSH tidak disimpan di kode. Program akan memintanya saat dijalankan, atau bisa diisi lewat `SSH_PASSWORD`.

## Cara menjalankan

```
python -m venv venv
venv\Scripts\Activate.ps1
pip install paramiko pysnmp-lextudio==6.1.2 pyasn1==0.4.8
python main.py
```

Di Linux, aktivasi venv-nya `source venv/bin/activate`. Saat dijalankan, masukkan password akun SSH jika diminta. Setiap modul juga bisa dites sendiri-sendiri, misalnya `python ssh_modul.py`.

Catatan: PySNMP versi lama (`pysnmp==4.4.12`) error di Python 3.12 ke atas karena modul `imp` sudah dihapus, jadi saya pakai `pysnmp-lextudio`.

## Personalisasi

Semua nilai diturunkan dari NIM:
- kode cabang diambil dari 3 digit terakhir NIM
- username SSH `admin_072` dan community SNMP `comm_072`
- VLAN ID memakai angka kode cabang langsung
- sampel telemetry dihitung dari digit NIM supaya ketiga status muncul router-A dari 2 digit terakhir NIM mod 50 (NORMAL), router-B dari 50 + digit ke-3 dan ke-4 dari belakang mod 31 (WASPADA), dan router-C dari 81 + jumlah semua digit mod 19 (KRITIS)

Nilai kode cabang dan kredensial sengaja tidak ditulis di README ini.

