def hitung_total_panen(hasil):
    return sum(hasil)

def hitung_diskon(total, persen):
    return total - (total * persen / 100)

if __name__ == "__main__":
    hasil = [120, 85, 150, 95]
    total = hitung_total_panen(hasil)
    print("Total panen:", total, "kg")
    print("Setelah diskon 10%:", hitung_diskon(total, 10), "kg")
