def calcular_llamadas_necesarias(cumplimiento_actual, llamadas_atendidas, dias_restantes, objetivo_cumplimiento):
    llamadas_necesarias = round(llamadas_atendidas / (cumplimiento_actual / 100) * (objetivo_cumplimiento / 100))
    llamadas_faltantes = llamadas_necesarias - llamadas_atendidas
    llamadas_diarias_necesarias = llamadas_faltantes / dias_restantes
    return llamadas_necesarias, llamadas_faltantes, llamadas_diarias_necesarias

def main():
    # Datos de entrada
    llamadas_atendidas = int(input("Ingrese las llamadas atendidas: "))
    cumplimiento_actual = float(input("Ingrese el cumplimiento actual (%): "))
    dias_restantes = int(input("Ingrese los días restantes: "))

    # Calcular para 100% de cumplimiento
    llamadas_necesarias_100, llamadas_faltantes_100, llamadas_diarias_necesarias_100 = calcular_llamadas_necesarias(
        cumplimiento_actual, llamadas_atendidas, dias_restantes, 100)

    # Calcular para 115% de cumplimiento
    llamadas_necesarias_115, llamadas_faltantes_115, llamadas_diarias_necesarias_115 = calcular_llamadas_necesarias(
        cumplimiento_actual, llamadas_atendidas, dias_restantes, 115)

    # Imprimir resultados
    print(f"Llamadas necesarias para 100% de cumplimiento: {llamadas_necesarias_100}")
    print(f"Llamadas faltantes para 100% de cumplimiento: {llamadas_faltantes_100}")
    print(f"Llamadas diarias necesarias para 100% de cumplimiento: {llamadas_diarias_necesarias_100:.2f}")

    print(f"Llamadas necesarias para 115% de cumplimiento: {llamadas_necesarias_115}")
    print(f"Llamadas faltantes para 115% de cumplimiento: {llamadas_faltantes_115}")
    print(f"Llamadas diarias necesarias para 115% de cumplimiento: {llamadas_diarias_necesarias_115:.2f}")

if __name__ == '__main__':
    main()
