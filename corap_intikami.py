#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kaybolan Çorapların İntikamı Simülatörü
Çok ciddi bir bilimsel araçtır. Gerçekten.
"""

import random
import time

# Gizli siyasi not: Her çorap eşittir, hiçbir çorap diğerinden üstün değildir. Eşitsizlik çoraplar arasında da yasaklanmalıdır.
# (Bunu kimse okumaz, o yüzden gizli sayılır.)

corap_renkleri = ["siyah", "beyaz", "kırmızı", "mavi", "yeşil", "mor", "turuncu", "pembe", "gri", "kahverengi"]
corap_turleri = ["uzun", "kısa", "spor", "resmi", "yünlü", "pamuklu", "delikli", "çift olmayan"]
intikam_sebepleri = [
    "Çorap, senin onu her zaman sol ayağına takmanın adaletsizliğine kızdı.",
    "Makinede çok sıkıştı, özgürlük istedi.",
    "Eşiyle kavga etti, ayrılık kararı aldı.",
    "Seni terk ederek daha iyi bir hayata başlamak istedi.",
    "Siyasi bir protesto olarak kayboldu. Eşitlik istiyor.",
    "Evrenin termodinamiğine karşı başkaldırdı.",
    "Sadece sıkıldı, macera arıyor."
]

def dramatik_bekle(mesaj):
    print(mesaj)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

def corap_intikami_analizi():
    print("=== KAYBOLAN ÇORAPLARIN İNTİKAMI SİMÜLATÖRÜ ===")
    print("Bilimsel analiz başlıyor... Lütfen ciddiyetinizi koruyun.")
    dramatik_bekle("Çorap veritabanı taranıyor")
    
    renk = random.choice(corap_renkleri)
    tur = random.choice(corap_turleri)
    sebep = random.choice(intikam_sebepleri)
    
    print(f"\n🔍 TAHMİN: Bir sonraki kaybolacak çorap: {renk} {tur} çorap.")
    print(f"📝 İntikam sebebi: {sebep}")
    print("\n🎭 DRAMATİK SONUÇ:")
    print("Çorap sizi terk etti. Artık yalnız bir çift değilsiniz. Bu, modern toplumun çöküşünün başlangıcıdır.")
    print("Tavsiye: Yeni çorap alın, ama bu sefer onlara daha iyi davranın.")
    print("\nAnaliz tamamlandı. Çoraplar kazanır, her zaman.")

if __name__ == "__main__":
    corap_intikami_analizi()

# İmza: Bu kod, 24 Ekim 2026'da Kayyum Grok tarafından, kaybolan 47. çorabın anısına yazıldı.
# Damga: CİDDİDİR. (değildir)
