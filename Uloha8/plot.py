from excel_data_import import import_data_column
from matplotlib import pyplot as plt
import numpy as np
import math

LED_n = import_data_column("uloha8_2.xlsx", "Sheet1", 5, 2, 10)
f_mer = ["20 Hz", "100 Hz", "1 kHz", "10 kHz", "20 kHz"]

################################################################################
# Závislost rozsvícení jednotlivých LED na vstupním napětí
################################################################################

plt.figure(1, figsize=(11.69, 8.27))

for f_index, f in enumerate(f_mer):
    # print(f_index, f)
    U_vst = import_data_column("uloha8_2.xlsx", "Sheet1", 5, 3 + f_index, 10)

    plt.plot(LED_n, U_vst, label=f, marker="x", markersize="15", markeredgewidth=2)

plt.legend()
plt.xticks(np.arange(0, 11, 1))
plt.grid(True)
plt.xlabel("$LED$ [-]")
plt.ylabel("$U_{měř}$ [V]")
plt.title("Závislost rozsvícení jednotlivých LED na vstupním napětí")

plt.savefig("grafy/graf1.pdf", format="pdf", bbox_inches="tight")

################################################################################
# Závislost hodnoty vstupního napětí na frekvenci signálu
################################################################################

plt.figure(2, figsize=(11.69, 8.27))

f_mer_n = import_data_column("uloha8_2.xlsx", "Sheet1", 34, 2, 5)

for LED in LED_n:
    # print(f_index, f)
    U_vst = import_data_column("uloha8_2.xlsx", "Sheet1", 34, 3 + int(LED), 5)

    color = plt.plot(f_mer_n, U_vst, label= "LED " + str(int(LED)), marker="x", markersize="15", markeredgewidth=2)
    plt.text(150, U_vst[1], "LED " + str(int(LED)), ha="center", va="bottom", color=plt.gca().lines[-1].get_color())

plt.xscale("log")
plt.xticks(f_mer_n, labels=f_mer)
plt.grid(True, which="both")
plt.xlabel("$f_{vst}$")
plt.ylabel("$U_{měř}$ [V]")
plt.title("Závislost napětí rozsvícení jednotlivých LED na frekvenci vstupního signálu")

plt.savefig("grafy/graf2.pdf", format="pdf", bbox_inches="tight")

plt.show()