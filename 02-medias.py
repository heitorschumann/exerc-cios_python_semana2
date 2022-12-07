from statistics import harmonic_mean
# liinha contendo 3 notas que são numeros reais positivos
n1, n2, n3 = map(int, input().split())
media = input().upper()

if media == 'A':
    # media aritmética
    resultado = n1+n2+n3/3
    print("Aritmética")
    print(f"{resultado:.2f}")
elif media == 'H':
    # media harmônica
    resultado = harmonic_mean([n1, n2, n3])
    print("Harmônica")
    print(f"{resultado:.2f}")
elif media == 'P':
    # media ponderada
    p1, p2, p3 = map(int, input().split())
    resultado = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3)
    print("Ponderada")
    print(f"{resultado:.2f}")
else:
    print("Operação inexistente")
