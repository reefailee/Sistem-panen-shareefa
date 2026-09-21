def cetak_laporan(hasil, total):
    print("=== LAPORAN PANEN ===")
    for i, h in enumerate(hasil, 1):
        print(f"Panen ke-{i}: {h} kg")
    print("Total:", total, "kg")
