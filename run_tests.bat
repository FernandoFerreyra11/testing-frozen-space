@echo off
echo ========================================
echo  Ejecutando tests con reporte HTML...
echo ========================================
behave -f html > reporte.html
behave -f pretty
echo.
echo ========================================
echo  Reporte guardado en: reporte.html
echo ========================================
