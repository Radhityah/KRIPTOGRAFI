import hashlib

def buat_md5(nama, email, nomor_hp):
    """Membuat hash MD5 dari data profil user."""
    data = f"{nama}|{email}|{nomor_hp}"
    return hashlib.md5(data.encode()).hexdigest()

def main():
    print("=" * 55)
    print("   SISTEM CEK INTEGRITAS DATA PROFIL USER (MD5)")
    print("=" * 55)

    # Input data awal
    print("\n[INPUT DATA PROFIL AWAL]")
    nama_awal  = input("Nama     : ")
    email_awal = input("Email    : ")
    hp_awal    = input("Nomor HP : ")

    # Buat hash awal
    hash_awal = buat_md5(nama_awal, email_awal, hp_awal)
    print("\n[HASH MD5 DATA AWAL]")
    print(f"Hash MD5 : {hash_awal}")

    # Input data baru
    print("\n[INPUT DATA PROFIL BARU]")
    nama_baru  = input("Nama     : ")
    email_baru = input("Email    : ")
    hp_baru    = input("Nomor HP : ")

    # Buat hash baru
    hash_baru = buat_md5(nama_baru, email_baru, hp_baru)

    # Tampilkan perbandingan
    print("\n" + "=" * 55)
    print("   HASIL PERBANDINGAN")
    print("=" * 55)
    print(f"Hash MD5 Lama : {hash_awal}")
    print(f"Hash MD5 Baru : {hash_baru}")
    print("-" * 55)

    if hash_awal == hash_baru:
        print("STATUS : DATA TIDAK BERUBAH (Integritas terjaga)")
    else:
        print("STATUS : DATA TELAH DIMODIFIKASI!")
        print("\nDetail perubahan:")
        if nama_awal != nama_baru:
            print(f"  - Nama    : '{nama_awal}' -> '{nama_baru}'")
        if email_awal != email_baru:
            print(f"  - Email   : '{email_awal}' -> '{email_baru}'")
        if hp_awal != hp_baru:
            print(f"  - Nomor HP: '{hp_awal}' -> '{hp_baru}'")
    print("=" * 55)

if __name__ == "__main__":
    main()