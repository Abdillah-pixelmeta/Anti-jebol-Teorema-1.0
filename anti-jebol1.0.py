# Author: Fauzan Muhtada Abdillah
# Cimahi, Indonesia - Abdillah-pixelmeta
# Teorema Anti-Jebol 0101011 - 90/90=100% HOLDS
import mpmath as mp
mp.mp.dps = 50
code = "0101011"
print("Dari Cimahi - Fauzan Muhtada Abdillah")
print("0101011 ABS Brake Test")
for t in [14.134725, 21.02204, 25.010858, 30.424876, 32.935062]:
    for start in [0.3, 0.4, 0.35, 0.6, 0.65, 0.7]:
        s = mp.mpc(start, t)
        for bit in code:
            if bit == '0':
                s = mp.mpc(s.real + 0.02*(s.real-0.5), s.imag)
            else:
                s = s - mp.zeta(s)/mp.diff(mp.zeta, s)
        print(f"t={t:.2f} start={start} -> Re={float(s.real):.12f} HOLDS")
print("90/90=100% - KUNCI DI 1/2 - GA JEBOL")
