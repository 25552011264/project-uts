from properti import Properti


class KamarKos(Properti):
    """Subclass yang merepresentasikan unit kamar kos."""

    def __init__(
        self,
        kode: str,
        alamat: str,
        harga_bulanan: int,
        nomor_kamar: str,
        lantai: int,
        fasilitas: str,
        status: str = "Tersedia",
    ):
        # Memanggil constructor superclass
        super().__init__(kode, alamat, harga_bulanan, status)
        # Atribut private khusus KamarKos
        self.__nomor_kamar = nomor_kamar
        self.__lantai = lantai
        self.__fasilitas = fasilitas

    # --- Getter ---
    def get_nomor_kamar(self) -> str:
        return self.__nomor_kamar

    def get_lantai(self) -> int:
        return self.__lantai

    def get_fasilitas(self) -> str:
        return self.__fasilitas

    def set_fasilitas(self, fasilitas_baru: str) -> None:
        self.__fasilitas = fasilitas_baru

    # --- Method tambahan ---
    def cek_fasilitas_lengkap(self) -> str:
        """Mengecek kelengkapan fasilitas kamar kos."""
        return f"Kamar {self.__nomor_kamar} (Lt. {self.__lantai}) - Fasilitas: {self.__fasilitas}"

    def info_ringkas(self) -> str:
        """Override method info_ringkas untuk menampilkan detail kamar kos."""
        return (
            f"[KOS | {self.get_kode()}] Kamar {self.__nomor_kamar} (Lt.{self.__lantai}) "
            f"@ {self.get_alamat()} | Fasilitas: {self.__fasilitas} | "
            f"Rp{self.get_harga_bulanan():,}/bln | Status: {self.get_status()}"
        )