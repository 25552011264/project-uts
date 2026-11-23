from kamar_kos import KamarKos
from kontrakan import Kontrakan
from penyewaan import Penyewa


class AplikasiPropertiKos:
    """Controller utama aplikasi CLI manajemen properti, kos, dan penyewa."""

    def __init__(self):
        # Menyimpan daftar objek properti (KamarKos & Kontrakan) dan penyewa
        self.daftar_properti: list = []
        self.daftar_penyewa: list[Penyewa] = []
        self._seed_data_awal()

    def _seed_data_awal(self) -> None:
        """Mengisi contoh data awal agar aplikasi langsung bisa diuji."""
        kos1 = KamarKos("KOS01", "Jl. Merdeka No. 10", 1200000, "A1", 1, "AC, WiFi, KM Dalam")
        kos2 = KamarKos("KOS02", "Jl. Merdeka No. 10", 950000, "A2", 1, "Kipas, WiFi, KM Luar")
        ktr1 = Kontrakan("KTR01", "Jl. Kenangan No. 25", 3500000, 3, 120, True)

        self.daftar_properti.extend([kos1, kos2, ktr1])

        # Relasi Association: Penyewa menempati satu KamarKos
        penyewa1 = Penyewa("P01", "Rina Wijaya", "081234567890", kos1)
        self.daftar_penyewa.append(penyewa1)

    def _cari_properti_by_kode(self, kode: str):
        """Helper mencari objek properti berdasarkan kode (case-insensitive)."""
        for item in self.daftar_properti:
            if item.get_kode().lower() == kode.lower():
                return item
        return None

    # 1. Tambah Data
    def tambah_data(self) -> None:
        print("\n--- TAMBAH DATA ---")
        print("1. Tambah Kamar Kos")
        print("2. Tambah Kontrakan")
        print("3. Tambah Penyewa (Menempati Kamar Kos)")
        pilihan = input("Pilih jenis data (1/2/3): ").strip()

        try:
            if pilihan == "1":
                kode = input("Kode Properti (cth: KOS03): ").strip()
                if self._cari_properti_by_kode(kode):
                    print("Kode properti sudah digunakan!")
                    return
                alamat = input("Alamat: ").strip()
                harga = int(input("Harga per bulan (angka): ").strip())
                no_kamar = input("Nomor Kamar: ").strip()
                lantai = int(input("Lantai: ").strip())
                fasilitas = input("Fasilitas: ").strip()

                kos_baru = KamarKos(kode, alamat, harga, no_kamar, lantai, fasilitas)
                self.daftar_properti.append(kos_baru)
                print("Data Kamar Kos berhasil ditambahkan.")

            elif pilihan == "2":
                kode = input("Kode Properti (cth: KTR02): ").strip()
                if self._cari_properti_by_kode(kode):
                    print("Kode properti sudah digunakan!")
                    return
                alamat = input("Alamat: ").strip()
                harga = int(input("Harga per bulan (angka): ").strip())
                kt = int(input("Jumlah Kamar Tidur: ").strip())
                luas = int(input("Luas Tanah (m2): ").strip())
                garasi_input = input("Ada garasi? (y/n): ").strip().lower()
                ada_garasi = garasi_input == "y"

                ktr_baru = Kontrakan(kode, alamat, harga, kt, luas, ada_garasi)
                self.daftar_properti.append(ktr_baru)
                print("Data Kontrakan berhasil ditambahkan.")

            elif pilihan == "3":
                # Menampilkan kamar kos yang masih tersedia
                kos_tersedia = [
                    p for p in self.daftar_properti
                    if isinstance(p, KamarKos) and p.get_status() == "Tersedia"
                ]
                if not kos_tersedia:
                    print("Tidak ada Kamar Kos yang tersedia saat ini.")
                    return

                print("Kamar Kos Tersedia:")
                for k in kos_tersedia:
                    print("  -", k.info_ringkas())

                kode_kos = input("Masukkan Kode Kamar Kos yang akan ditempati: ").strip()
                target_kos = self._cari_properti_by_kode(kode_kos)
                if not isinstance(target_kos, KamarKos) or target_kos.get_status() != "Tersedia":
                    print("Kode Kamar Kos tidak valid atau sudah terisi.")
                    return

                id_p = input("ID Penyewa (cth: P02): ").strip()
                nama_p = input("Nama Penyewa: ").strip()
                hp_p = input("No. HP: ").strip()

                penyewa_baru = Penyewa(id_p, nama_p, hp_p, target_kos)
                self.daftar_penyewa.append(penyewa_baru)
                print("Data Penyewa berhasil ditambahkan dan status Kamar Kos diperbarui menjadi Terisi.")

            else:
                print("Pilihan tidak valid.")
        except ValueError as e:
            print(f"Input tidak valid: {e}")

    # 2. Tampilkan Data
    def tampilkan_data(self) -> None:
        print("\n--- DAFTAR PROPERTI (KOS & KONTRAKAN) ---")
        if not self.daftar_properti:
            print("Belum ada data properti.")
        else:
            for idx, item in enumerate(self.daftar_properti, start=1):
                print(f"{idx}. {item.info_ringkas()}")

        print("\n--- DAFTAR PENYEWA & KAMAR KOS YANG DITEMPATI ---")
        if not self.daftar_penyewa:
            print("Belum ada data penyewa.")
        else:
            for idx, p in enumerate(self.daftar_penyewa, start=1):
                print(f"{idx}. {p.info_penempatan()}")

    # 3. Cari Data
    def cari_data(self) -> None:
        print("\n--- CARI DATA ---")
        keyword = input("Masukkan kode/alamat properti atau nama/ID penyewa: ").strip().lower()
        if not keyword:
            print("Kata kunci pencarian tidak boleh kosong.")
            return

        ditemukan = False
        for item in self.daftar_properti:
            if keyword in item.get_kode().lower() or keyword in item.get_alamat().lower():
                print("[Properti] ->", item.info_ringkas())
                ditemukan = True

        for p in self.daftar_penyewa:
            if keyword in p.get_id_penyewa().lower() or keyword in p.get_nama().lower():
                print("[Penyewa]  ->", p.info_penempatan())
                ditemukan = True

        if not ditemukan:
            print("Data tidak ditemukan.")

    # 4. Ubah Data
    def ubah_data(self) -> None:
        print("\n--- UBAH DATA ---")
        print("1. Ubah Harga Bulanan Properti")
        print("2. Ubah Status Properti (Tersedia / Terisi)")
        print("3. Ubah No. HP Penyewa")
        pilihan = input("Pilih opsi (1/2/3): ").strip()

        try:
            if pilihan in ("1", "2"):
                kode = input("Masukkan Kode Properti: ").strip()
                target = self._cari_properti_by_kode(kode)
                if not target:
                    print("Properti tidak ditemukan.")
                    return

                if pilihan == "1":
                    harga_baru = int(input("Harga bulanan baru: ").strip())
                    target.set_harga_bulanan(harga_baru)
                    print("Harga bulanan berhasil diperbarui.")
                else:
                    status_baru = input("Status baru (Tersedia / Terisi): ").strip()
                    target.set_status(status_baru)
                    print("Status properti berhasil diperbarui.")

            elif pilihan == "3":
                id_p = input("Masukkan ID Penyewa: ").strip()
                target_p = next(
                    (p for p in self.daftar_penyewa if p.get_id_penyewa().lower() == id_p.lower()),
                    None,
                )
                if not target_p:
                    print("Penyewa tidak ditemukan.")
                    return

                hp_baru = input("No. HP baru: ").strip()
                target_p.set_no_hp(hp_baru)
                print("No. HP penyewa berhasil diperbarui.")
            else:
                print("Pilihan tidak valid.")
        except ValueError as e:
            print(f"Gagal mengubah data: {e}")

    # 5. Cek Status Data
    def cek_status_data(self) -> None:
        print("\n--- CEK STATUS DATA ---")
        total_properti = len(self.daftar_properti)
        tersedia = sum(1 for p in self.daftar_properti if p.get_status().lower() == "tersedia")
        terisi = sum(1 for p in self.daftar_properti if p.get_status().lower() == "terisi")
        total_kos = sum(1 for p in self.daftar_properti if isinstance(p, KamarKos))
        total_kontrakan = sum(1 for p in self.daftar_properti if isinstance(p, Kontrakan))

        print(f"Total Properti      : {total_properti} (Kos: {total_kos}, Kontrakan: {total_kontrakan})")
        print(f"Status Tersedia     : {tersedia}")
        print(f"Status Terisi       : {terisi}")
        print(f"Total Penyewa Aktif : {len(self.daftar_penyewa)}")

        kode = input("\nIngin cek detail status kode properti tertentu? (Kosongkan jika tidak): ").strip()
        if kode:
            target = self._cari_properti_by_kode(kode)
            if target:
                print("Detail:", target.info_ringkas())
            else:
                print("Kode properti tidak ditemukan.")

    def jalankan(self) -> None:
        """Loop utama menu CLI."""
        while True:
            print("\n==========================================")
            print("   APLIKASI MANAJEMEN PROPERTI DAN KOS")
            print("==========================================")
            print("1. Tambah data")
            print("2. Tampilkan data")
            print("3. Cari data")
            print("4. Ubah data")
            print("5. Cek status data")
            print("6. Keluar dari program")
            print("==========================================")

            menu = input("Pilih menu (1-6): ").strip()
            if menu == "1":
                self.tambah_data()
            elif menu == "2":
                self.tampilkan_data()
            elif menu == "3":
                self.cari_data()
            elif menu == "4":
                self.ubah_data()
            elif menu == "5":
                self.cek_status_data()
            elif menu == "6":
                print("Terima kasih telah menggunakan aplikasi. Sampai jumpa!")
                break
            else:
                print("Pilihan menu tidak tersedia. Silakan pilih 1-6.")


if __name__ == "__main__":
    app = AplikasiPropertiKos()
    app.jalankan()