def show_menu():
    print("Menu:")
    print("1. Pilihan 1")
    print("2. Pilihan 2")
    print("3. Pilihan 3")
    print("4. Keluar")

def main():
    while True:
        show_menu()
        choice = input("Masukkan pilihan Anda: ")

        if choice == "1":
            rusuk = int(input("Rusuk  : "))
            print("Luas = ", 6*(rusuk**2))
            print("volume = ", rusuk*rusuk*rusuk)
        elif choice == "2":
            print("Anda memilih Pilihan 2")
        elif choice == "3":
            print("Anda memilih Pilihan 3")
        elif choice == "4":
            print("Terima kasih! Sampai jumpa lagi.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
