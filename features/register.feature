Feature: Registro de Usuario
  Como nuevo usuario del sistema
  Quiero poder crear una cuenta
  Para acceder a las funcionalidades exclusivas

  @registro_csv
  Scenario Outline: Registro de usuario desde CSV
    Given estoy en la pagina de registro
    When ingreso datos de registro desde CSV con indice <indice>
    Then <resultado_esperado>

    Examples:
      | indice | resultado_esperado                                     |
      | 0      | deberia ver un mensaje de éxito "Usuario creado con éxito" |
      | 1      | deberia ver un mensaje de error que contiene "email"       |
      | 2      | deberia ver un mensaje de error que contiene "existe"      |
