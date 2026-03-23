Feature: Login de Usuario
  Como usuario del sistema
  Quiero poder iniciar sesión
  Para acceder a mi cuenta

  @login
  Scenario: Login exitoso
    Given estoy en la página de login
    When ingreso credenciales válidas
    Then debería ver el mensaje de bienvenida

  @login
  Scenario: Login fallido con credenciales incorrectas
    Given estoy en la página de login
    When ingreso credenciales inválidas
    Then debería ver un mensaje de error