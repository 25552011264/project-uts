from properti import Properti


class Kontrakan(Properti):
    """Subclass yang merepresentasikan rumah kontrakan."""

    def __init__(
        self,
        kode: str,
        alamat: str,
        harga_bulanan: int,
        jumlah_kamar_tidur: int,
        luas_tanah_m2: int,
        ada_garasi: bool,
        status: str = "Tersedia",
    ):
        # Memanggil constructor superclass
        super().__init__(kode, alamat, harga_bulanan, status)
        # Atribut private khusus Kontrakan
        self.__jumlah_kamar_tidur = jumlah_kamar_tidur
        self.__luas_tanah_m2 = luas_tanah_m2
        self.__ada_garasi = ada_garasi

    # --- Getter ---
    def get_jumlah_kamar_tidur(self) -> int:
        return self.__jumlah_kamar_tidur

    def get_luas_tanah_m2(self) -> int:
        return self.__luas_tanah_m2

    def get_ada_garasi(self) -> bool:
        return self.__ada_garasi

    def set_jumlah_kamar_tidur(self, jumlah: int) -> None:
        if jumlah > 0:
            self.__jumlah_kamar_tidur = jumlah

    # --- Method tambahan ---
    def hitung_estimasi_deposit(self, persentase: float = 0.2) -> int:
        """Menghitung uang deposit sewa kontrakan (default 20% dari harga bulanan)."""
        return int(self.get_harga_bulanan() * persentase)

    def info_ringkas(self) -> str:
        """Override method info_ringkas untuk menampilkan detail kontrakan."""
        garasi_str = "Ada Garasi" if self.__ada_garasi else "Tanpa Garasi"
        return (
            f"[KONTRAKAN | {self.get_kode()}] {self.get_alamat()} | "
            f"{self.__jumlah_kamar_tidur} KT, {self.__luas_tanah_m2} m2, {garasi_str} | "
            f"Rp{self.get_harga_bulanan():,}/bln | Status: {self.get_status()}"
        )