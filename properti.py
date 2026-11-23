class Properti:
    """Superclass induk untuk seluruh jenis properti (kos dan kontrakan)."""

    def __init__(self, kode: str, alamat: str, harga_bulanan: int, status: str = "Tersedia"):
        # Constructor berparameter dengan atribut private (__nama_atribut)
        self.__kode = kode
        self.__alamat = alamat
        self.__harga_bulanan = harga_bulanan
        self.__status = status  # Contoh: "Tersedia" atau "Terisi"

    # --- Getter (Encapsulation) ---
    def get_kode(self) -> str:
        return self.__kode

    def get_alamat(self) -> str:
        return self.__alamat

    def get_harga_bulanan(self) -> int:
        return self.__harga_bulanan

    def get_status(self) -> str:
        return self.__status

    # --- Setter / Method pengubah status (Encapsulation) ---
    def set_harga_bulanan(self, harga_baru: int) -> None:
        if harga_baru > 0:
            self.__harga_bulanan = harga_baru
        else:
            raise ValueError("Harga bulanan harus lebih dari 0.")

    def set_status(self, status_baru: str) -> None:
        self.__status = status_baru

    # --- Method tambahan ---
    def hitung_biaya_periode(self, jumlah_bulan: int) -> int:
        """Menghitung total biaya sewa berdasarkan jumlah bulan."""
        if jumlah_bulan <= 0:
            return 0
        return self.__harga_bulanan * jumlah_bulan

    def info_ringkas(self) -> str:
        """Mengembalikan ringkasan informasi properti."""
        return (
            f"[{self.__kode}] {self.__alamat} | "
            f"Rp{self.__harga_bulanan:,}/bln | Status: {self.__status}"
        )