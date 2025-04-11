[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zLSmh4bI)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19022032)
# Práctica 3. Diseño modular



## Presentación del Problema

El objetivo de esta práctica fue desarrollar un sistema para evaluar automáticamente la legibilidad de textos en español utilizando el índice de Velázquez Gaytán. Este índice calcula la dificultad de comprensión de un texto basado en tres métricas fundamentales:

- Relación palabras/oraciones (complejidad estructural)
- Promedio de sílabas por palabra (complejidad léxica)
- Fórmula matemática que combina estos factores

El desafío principal consistió en implementar algoritmos eficientes para contar estos elementos lingüísticos (como vocales acentuadas y distintos signos de puntuación).

## Resultados Obtenidos

**PatitoFeo.txt**

Índice: 86.60 (Nivel: Fácil)

Estadísticas: 39 oraciones, 507 palabras, 904 sílabas

Análisis: Como era de esperarse en un cuento infantil, muestra la mayor legibilidad del conjunto, con oraciones cortas y vocabulario simple.

**AlanTuring.txt**

Índice: 49.41 (Nivel: Difícil)

Estadísticas: 20 oraciones, 540 palabras, 1169 sílabas

Análisis: Texto biográfico con contenido técnico que casi duplica la relación sílabas/palabra respecto al cuento infantil.

**ComputaciónEvolutiva.txt**

Índice: 23.58 (Nivel: Muy difícil)

Estadísticas: 9 oraciones, 199 palabras, 533 sílabas

Análisis: Documento académico especializado que presenta la mayor densidad lingüística (2.68 sílabas/palabra).

## Implementación Técnica

El sistema se desarrolló en dos módulos Python interconectados:

### Módulo de Análisis Textual (`analisis_texto.py`)

Implementa tres funciones clave mediante procesamiento de strings:

- `contar_oraciones()`: Identifica terminaciones con .?!:;
- `contar_palabras()`: Divide el texto por espacios
- `contar_silabas()`: Aproximación basada en conteo de vocales

Incluye:

- Manejo de casos extremos (mínimo 1 unidad)
- Procesamiento correcto de caracteres especiales y tildes

### Módulo de Cálculo (`legibilidad.py`)

- Aplica la fórmula de Velázquez Gaytán con precisión decimal
- Implementa lógica condicional para clasificación por niveles

Incluye validaciones para:

- Evitar divisiones por cero
- Acotar resultados al rango 0-100
- Uso de generadores para eficiencia en memoria

## Conclusión

Este proyecto logró cumplir con el objetivo de calcular el índice de legibilidad en textos escritos en español y clasificar su nivel de dificultad. Los resultados obtenidos coinciden con lo que se esperaba según el tipo de texto, lo que demuestra que el método utilizado es funcional y efectivo. Además, el sistema fue capaz de adaptarse a diferentes estilos de escritura y manejó bien las particularidades del idioma, como los acentos y signos de puntuación.
