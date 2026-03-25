set PYTHONIOENCODING=utf-8

echo ========================================
echo  Ejecutando tests con reporte autonmtico...
echo ========================================
behave -f pretty
echo.
echo ========================================
echo  Reporte guardado en: reporte.csv
echo ========================================
