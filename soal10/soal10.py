import shapefile

# 1184097 mod 8 = 1, dua angka terakhir npm adalah 9.  akan membuat polygon segitiga

w = shapefile.Writer("soal10", shapeType=shapefile.POLYGON)
w.shapeType


w.field("kolom1", "C")
w.field("kolom2", "C")

w.record("kadal", "satu")
w.record("kodok", "dua")
w.record("kuro", "tiga")
w.record("kera", "empat")
w.record("kutilang", "lima")
w.record("kukang", "enam")
w.record("kuman", "tujuh")
w.record("kucing", "tujuh")
w.record("kijang", "tujuh")


w.poly([[[3, 1], [5, 3], [3, 5], [3, 1]]])
w.poly([[[9, 1], [11, 3], [9, 5], [9, 1]]])
w.poly([[[15, 1], [17, 3], [15, 5], [15, 1]]])
w.poly([[[20, 1], [22, 3], [20, 5], [20, 1]]])
w.poly([[[3, 6], [5, 8], [3, 10], [3, 6]]])
w.poly([[[9, 6], [11, 8], [9, 10], [9, 6]]])
w.poly([[[15, 6], [17, 8], [15, 10], [15, 6]]])
w.poly([[[25, 6], [27, 8], [25, 10], [25, 6]]])
w.poly([[[22, 6], [24, 8], [22, 10], [22, 6]]])


w.close()
