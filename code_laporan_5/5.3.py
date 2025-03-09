
# Fungsi lambda untuk konversi suhu
celciustofahrenheit = lambda C: (9/5) * C + 32
celciustoreamur = lambda C: 0.8 * C

print("Input C = 100. Output F =", celciustofahrenheit(100))  # 212
print("Input C = 80. Output R =", celciustoreamur(80))        # 64
print("Input C = 0. Output F =", celciustofahrenheit(0))      # 32

