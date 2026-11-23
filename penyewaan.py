from kamar_kos import KamarKos


class Penyewa:
    """Class relasi Association: Penyewa menempati satu KamarKos."""

    def __init__(self, id_penyewa: str, nama: str, no_hp: str, kamar_kos: KamarKos):
        # Atribut private
        self.__id_penyewa = id_penyewa
        self.__nama = nama
        self.__no_hp = no_hp
        self.__kamar_kos = kamar_kos  # Relasi association ke objek KamarKos

        # Menandai kamar kos yang ditempati sebagai Terisi
        if self.__kamar_kos is not None:
            self.__kamar_kos.set_status("Terisi")

    # --- Getter ---
    def get_id_penyewa(self) -> str:
        return self.__id_penyewa

    def get_nama(self) -> str:
        return self.__nama

    def get_no_hp(self) -> str:
        return self.__no_hp

    def get_kamar_kos(self) -> KamarKos:
        return self.__kamar_kos

    def set_no_hp(self, no_hp_baru: str) -> None:
        self.__no_hp = no_hp_baru

    # --- Method tambahan ---
    def pindah_kamar(self, kamar_baru: KamarKos) -> None:
        """Memindahkan penyewa ke KamarKos lain dan memperbarui status kedua kamar."""
        if self.__kamar_kos is not None:
            self.__kamar_kos.set_status("Tersedia")
        self.__kamar_kos = kamar_baru
        self.__kamar_kos.set_status("Terisi")

    def info_penempatan(self) -> str:
        """Menampilkan informasi penyewa beserta kamar kos yang ditempati."""
        kode_kamar = self.__kamar_kos.get_kode() if self.__kamar_kos else "-"
        no_kamar = self.__kamar_kos.get_nomor_kamar() if self.__kamar_kos else "-"
        return (
            f"ID: {self.__id_penyewa} | Nama: {self.__nama} | HP: {self.__no_hp} "
            f"--> Menempati Kos [{kode_kamar}] No. {no_kamar}"
        )