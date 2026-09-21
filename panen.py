def hitung_total_panen(hasil):
    return sum(hasil)

if __name__ == "__main__":
    hasil = [120, 85, 150, 95]
    print("Total panen:", hitung_total_panen(hasil), "kg")
