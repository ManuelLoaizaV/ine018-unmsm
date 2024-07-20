gradosCelsius = int(15)
def De_celsius_a_farenheit(C):
    F = (9*C)/5 + 32
    return F
gradosFarenheit = De_celsius_a_farenheit(gradosCelsius)
print(gradosCelsius," grados celsius son ", gradosFarenheit, "grados farenheit")

De_celsius_a_farenheit(gradosCelsius)
