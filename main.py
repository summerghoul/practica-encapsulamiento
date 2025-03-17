from clases.cuenta_bancaria import CuentaBancaria

# creamos instancia

cuenta = CuentaBancaria("Miguel", 1500)

# ---------------------------------------------------------------

# podemos intentar ver datos privados sin embargo nos saldra un error
# tambien podemos intentar modificar los datos privados, sin embargo no ocurrira nada

# ---------------------------------------------------------------

# Obtener saldo
print(cuenta.obtener_saldo())

# depositar 500 y obtener saldo
cuenta.depositar(-600)
print(cuenta.obtener_saldo())

# retirar 2000 y obtener saldo
cuenta.retirar(2000)
print(cuenta.obtener_saldo())
