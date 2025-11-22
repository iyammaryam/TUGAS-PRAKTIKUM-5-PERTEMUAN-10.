# Menyiapkan dictionary sesuai soal dan menjalankan operasi yang diminta

def latihan1():
    # buat dictionary awal
    contacts = {
        "jk": "081267888",
        "RM": "087677776"
    }

    print("Kontak awal:", contacts)
    print()

    # Tampilkan kontak Ari
    print("Nomor JK:", contacts.get("JK"))
    print()

    # Tambah kontak Rio
    contacts["Rio"] = "087654544"
    print("Setelah tambah Rio:", contacts)
    print()

    # Ubah kontak RM
    contacts["RM"] = "088999776"
    print("Setelah ubah nomor RM:", contacts)
    print()

    # Tampilkan semua Nama
    print("Semua nama:", list(contacts.keys()))
    # Tampilkan semua Nomor
    print("Semua nomor:", list(contacts.values()))
    print()

    # Tampilkan daftar Nama dan nomornya (iterasi)
    print("Daftar nama dan nomor:")
    for name, number in contacts.items():
        print(f" - {name}: {number}")
    print()

    # Hapus kontak jk
    if "jk" in contacts:
        del contacts["jk"]
        print("Setelah hapus jk:", contacts)
    else:
        print("jk tidak ditemukan untuk dihapus.")

if __name__ == "__main__":
    latihan1()