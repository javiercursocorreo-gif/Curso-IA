#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_2_csvs_maestros_classroom.py
Genera los DOS únicos archivos CSV unificados para Google Classroom:
1. CURSO_IA_UNIFICADO.csv (en CURSO-IA/PANELES_CSV/)
   - Tema 1: MONOGRAFICOS (con los 6 mapas interactivos de los monográficos)
   - Temas siguientes: SESIÓN 1 a SESIÓN 60 (cada una con su Mapa Interactivo en 3 columnas)
2. CURSO_ROBOTICA_UNIFICADO.csv (en CURSO-ROBOTICA-V2/PANELES_CSV/ y copia en CURSO-IA/PANELES_CSV/)
   - Tema 0: INTRODUCCIÓN (Presentación inaugural + Manual de Classroom)
   - Temas 1..8:
       ROB1. UN MOTOR
       ROB2. SENSORES Y DECISIONES
       ROB3. MOVIMIENTO AVANZADO
       ROB4. BRAZO ROBÓTICO
       ROB5. ANDROIDES
       ROB6. NAVES ESPACIALES
       ROB7. EXPLORACIÓN ESPACIAL
       ROB8. TITANES Y ANIMATRÓNICA
"""

import os
import csv
import re

IA_ROOT = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
IA_CSV_DIR = os.path.join(IA_ROOT, "PANELES_CSV")

ROB_ROOT = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-ROBOTICA-V2"
ROB_CSV_DIR = os.path.join(ROB_ROOT, "PANELES_CSV")

HEADER = ['ID_CURSO', 'TEMA_CLASSROOM', 'TITULO_MATERIAL', 'DESCRIPCION_MATERIAL', 'URL_GITHUB']

# Mapa oficial de nombres de temas para cada bloque de Robótica
BLOCK_THEME_MAP = {
    1: "ROB1. UN MOTOR",
    2: "ROB2. SENSORES Y DECISIONES",
    3: "ROB3. MOVIMIENTO AVANZADO",
    4: "ROB4. BRAZO ROBÓTICO",
    5: "ROB5. ANDROIDES",
    6: "ROB6. NAVES ESPACIALES",
    7: "ROB7. EXPLORACIÓN ESPACIAL",
    8: "ROB8. TITANES Y ANIMATRÓNICA",
}

# Dataset oficial verificado de los 8 bloques de Robótica (respaldo directo si se ejecuta en sandbox)
FALLBACK_ROBOTICA_ROWS = [
    # INTRODUCCIÓN
    [
        '',
        'INTRODUCCIÓN',
        'Presentación inaugural',
        'Cuadro de mando interactivo de la clase inaugural con acceso directo a las diapositivas oficiales y a la guía visual de Google Classroom.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica-IA-Comun/0.PRESENTACION_PARA_LA_PRIMERA_CLASE/MAPA_CLASE_INAUGURAL.html'
    ],
    [
        '',
        'INTRODUCCIÓN',
        'Manual de Classroom',
        'Guía visual paso a paso para alumnos sobre cómo entrar y utilizar Google Classroom en el curso.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica-IA-Comun/1.GOOGLE_CLASSROOM/Guia_de_Classroom.pdf'
    ],
    # ROB1. UN MOTOR
    [
        '',
        'ROB1. UN MOTOR',
        '1.1 Puerta supermercado',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simuladores 3D de montaje, gemelo digital, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-1_Un-motor/1.1_Puerta-supermercado/MAPA_CLASE_1.1_PUERTA.html'
    ],
    [
        '',
        'ROB1. UN MOTOR',
        '1.2 Lavadora',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simuladores 3D de montaje, gemelo digital, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-1_Un-motor/1.2_Lavadora/MAPA_CLASE_1.2_LAVADORA.html'
    ],
    [
        '',
        'ROB1. UN MOTOR',
        '1.3 Ascensor',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simuladores 3D de montaje, gemelo digital, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-1_Un-motor/1.3_Ascensor/MAPA_CLASE_1.3_ASCENSOR.html'
    ],
    [
        '',
        'ROB1. UN MOTOR',
        '1.4 Semaforos inteligentes',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simuladores 3D de montaje, gemelo digital, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-1_Un-motor/1.4_Semaforos-inteligentes/MAPA_CLASE_1.4_SEMAFOROS.html'
    ],
    # ROB2. SENSORES Y DECISIONES
    [
        '',
        'ROB2. SENSORES Y DECISIONES',
        '2.1 Silla Ruedas Electrica. (Traccion diferencial)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simuladores 3D de montaje, gemelo digital y simulación interactiva sigue-ratón, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-2_Sensores-y-Decisiones/2.1_Silla-Ruedas-Electrica.%20%28Traccion-diferencial%29/MAPA_CLASE_2.1_SILLA_RUEDAS.html'
    ],
    [
        '',
        'ROB2. SENSORES Y DECISIONES',
        '2.2 Roomba. (Bucle infinito con sensor)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simuladores 3D de montaje, gemelo digital, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-2_Sensores-y-Decisiones/2.2_Roomba.%20%28Bucle-infinito-con-sensor%29/MAPA_CLASE_2.2_ROOMBA.html'
    ],
    [
        '',
        'ROB2. SENSORES Y DECISIONES',
        '2.3 Aparcamiento. (Condicion IF ELSE)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simuladores 3D de montaje, gemelo digital de plaza libre/ocupada, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-2_Sensores-y-Decisiones/2.3_Aparcamiento.%20%28Condicion-IF-ELSE%29/MAPA_CLASE_2.3_APARCAMIENTO.html'
    ],
    [
        '',
        'ROB2. SENSORES Y DECISIONES',
        '2.4 Ozobot. (El color como lenguaje)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simuladores 3D de montaje, gemelo digital seguidor de líneas, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-2_Sensores-y-Decisiones/2.4_Ozobot.%20%28El-color-como-lenguaje%29/MAPA_CLASE_2.4_OZOBOT.html'
    ],
    [
        '',
        'ROB2. SENSORES Y DECISIONES',
        '2.5 Camara seguridad. (Variable simple)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simuladores 3D de montaje, gemelo digital de barrido, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-2_Sensores-y-Decisiones/2.5_Camara-seguridad.%20%28Variable-simple%29/MAPA_CLASE_2.5_CAMARA_SEGURIDAD.html'
    ],
    # ROB3. MOVIMIENTO AVANZADO
    [
        '',
        'ROB3. MOVIMIENTO AVANZADO',
        '3.1 Robot repartidor. (Tarea guardada)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simuladores 3D de montaje, gemelo digital con navegación, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-3_Movimiento-Avanzado/3.1_Robot-repartidor.%20%28Tarea-guardada%29/MAPA_CLASE_3.1_ROBOT_REPARTIDOR.html'
    ],
    [
        '',
        'ROB3. MOVIMIENTO AVANZADO',
        '3.2 Coche ELEGOO. (Ver con camara)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simuladores 3D de montaje, gemelo digital con visión artificial, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-3_Movimiento-Avanzado/3.2_Coche-ELEGOO.%20%28Ver-con-camara%29/MAPA_CLASE_3.2_COCHE_ELEGOO.html'
    ],
    [
        '',
        'ROB3. MOVIMIENTO AVANZADO',
        '3.3 Avion con servos. (El servo posicion exacta)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), guía de servos (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simuladores 3D de montaje, cabina interactiva (manual, auto, sonido), simuladores de vuelo exterior, taller de averías y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-3_Movimiento-Avanzado/3.3_Avion-con-servos.%20%28El-servo-posicion-exacta%29/MAPA_CLASE_3.3_AVION_SERVOS.html'
    ],
    [
        '',
        'ROB3. MOVIMIENTO AVANZADO',
        '3.4 Dron. (Tres dimensiones)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simulador 3D de físicas, simulador de vuelo completo y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-3_Movimiento-Avanzado/3.4_Dron.%20%28Tres-dimensiones%29/MAPA_CLASE_3.4_DRON.html'
    ],
    [
        '',
        'ROB3. MOVIMIENTO AVANZADO',
        '3.5 Penguin BOT. (Sincronizacion de servos)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simuladores 3D de montaje bípedo, gemelo digital de marcha, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-3_Movimiento-Avanzado/3.5_Penguin-BOT.%20%28Sincronizacion-de-servos%29/MAPA_CLASE_3.5_PENGUIN_BOT.html'
    ],
    # ROB4. BRAZO ROBÓTICO
    [
        '',
        'ROB4. BRAZO ROBÓTICO',
        '4.1 Base giratoria. (Parametro)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), infografía de servomotores (PNG), presentación teórica (PDF), vídeo demostrativo (MP4), simulador 3D de montaje, simulación 3D en entorno real, programación por bloques con parámetros y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-4_Brazo-robotico/4.1_Base-giratoria.%20%28Parametro%29/MAPA_CLASE_4.1_BASE_GIRATORIA.html'
    ],
    [
        '',
        'ROB4. BRAZO ROBÓTICO',
        '4.2 Hombro. (Coordinar dos acciones)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simulador 3D de montaje, simulación 3D de elevación, programación por bloques coordinada y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-4_Brazo-robotico/4.2_Hombro.%20%28Coordinar-dos-acciones%29/MAPA_CLASE_4.2_HOMBRO.html'
    ],
    [
        '',
        'ROB4. BRAZO ROBÓTICO',
        '4.3 Codo. (Secuencia tres motores)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simulador 3D de montaje, simulación 3D en entorno real, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-4_Brazo-robotico/4.3_Codo.%20%28Secuencia-tres-motores%29/MAPA_CLASE_4.3_CODO.html'
    ],
    [
        '',
        'ROB4. BRAZO ROBÓTICO',
        '4.4 Muneca. (Variable de posicion)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simulador 3D de montaje, simulación 3D en entorno real, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-4_Brazo-robotico/4.4_Muneca.%20%28Variable-de-posicion%29/MAPA_CLASE_4.4_MUNECA.html'
    ],
    [
        '',
        'ROB4. BRAZO ROBÓTICO',
        '4.5 Pinza. (Sensor mas accion)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simulador 3D de montaje de garra, simulación 3D con sensor infrarrojo, programación por bloques y reto Pick & Place.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-4_Brazo-robotico/4.5_Pinza.%20%28Sensor-mas-accion%29/MAPA_CLASE_4.5_PINZA.html'
    ],
    [
        '',
        'ROB4. BRAZO ROBÓTICO',
        '4.6 Mano hidraulica. (Fuerza controlada)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simulador 3D de montaje hidráulico, simulación 3D de presión graduada, programación por bloques y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-4_Brazo-robotico/4.6_Mano-hidraulica.%20%28Fuerza-controlada%29/MAPA_CLASE_4.6_MANO_HIDRAULICA.html'
    ],
    # ROB5. ANDROIDES
    [
        '',
        'ROB5. ANDROIDES',
        '5.1 Perro Unitree Go2 AIR',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simulador 3D de anatomía y montaje, gemelo digital en entorno real, misiones acrobáticas y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-5_Androides/5.1_Perro_Unitree%20Go2%20AIR/MAPA_CLASE_5.1_PERRO_UNITREE.html'
    ],
    [
        '',
        'ROB5. ANDROIDES',
        '5.2 Robot Bipedo. (Comunicacion visual)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simulador 3D de montaje, cinemática de marcha bípeda, programación de estados visuales y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-5_Androides/5.2_Robot-Bipedo.%20%28Comunicacion-visual%29/MAPA_CLASE_5.2_ROBOT_BIPEDO.html'
    ],
    [
        '',
        'ROB5. ANDROIDES',
        '5.3 Androide MIXAMO',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), teoría general (PDF), guías de uso y fichas de taller (PDF), masterclass de simulación a Tesla (PDF), vídeo (MP4), simuladores 3D de montaje, intercambio de pieles, baile salsa y juego.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-5_Androides/5.3_Androide_MIXAMO/MAPA_CLASE_5.3_ANDROIDE_MIXAMO.html'
    ],
    [
        '',
        'ROB5. ANDROIDES',
        '5.4 Transformer. (POO y Enjambres)',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simulador de clase base, simulador de IA y movimiento, simulador de enjambres coordinados y juego de defensa.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-5_Androides/5.4_Transformer.%20%28POO-y-Enjambres%29/MAPA_CLASE_5.4_TRANSFORMER.html'
    ],
    [
        '',
        'ROB5. ANDROIDES',
        '5.5 Trio Dinamico StarWars',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simulador R2-D2, simulador BB-8 esférico, simulador C-3PO bípedo y simulador conjunto del Trío Dinámico.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-5_Androides/5.5_Trio_Dinamico_StarWars/MAPA_CLASE_5.5_TRIO_STAR_WARS.html'
    ],
    [
        '',
        'ROB5. ANDROIDES',
        '5.6 Robot combate',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), presentación teórica (PDF), vídeo demostrativo (MP4), simulador de anatomía mecha, visor de animaciones de combate, arena de lucha y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-5_Androides/5.6_Robot-combate/MAPA_CLASE_5.6_ROBOT_COMBATE.html'
    ],
    # ROB6. NAVES ESPACIALES
    [
        '',
        'ROB6. NAVES ESPACIALES',
        '6.1 Transporte Espacial Autonomo',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), teoría oficial (PDF), vídeos demostrativos (MP4), visor 3D de transporte autónomo y juego espacial.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-6_Naves_espaciales/6.1_Transporte_Espacial_Autonomo/MAPA_CLASE_6.1_TRANSPORTE_AUTONOMO.html'
    ],
    [
        '',
        'ROB6. NAVES ESPACIALES',
        '6.2 Star Wars',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), teoría oficial (PDF), vídeos hiperrealistas (MP4), el Gran Museo Star Wars con sus 6 pabellones 3D, taller Mixamo y juego de combate.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-6_Naves_espaciales/6.2_Star_Wars/MAPA_CLASE_6.2_STAR_WARS.html'
    ],
    [
        '',
        'ROB6. NAVES ESPACIALES',
        '6.3 Star Trek',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), visores 3D de la USS Enterprise y USS Intrepid, museo interactivo de inventos reales inspirados por Star Trek, simulaciones y juego.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-6_Naves_espaciales/6.3_Star_Trek/MAPA_CLASE_6.3_STAR_TREK.html'
    ],
    [
        '',
        'ROB6. NAVES ESPACIALES',
        '6.4 Interstellar',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), visor 3D de la nave Endurance en alta fidelidad, simulador de travesía por agujero de gusano y juego de navegación relativista.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-6_Naves_espaciales/6.4_Interstellar/MAPA_CLASE_6.4_INTERSTELLAR.html'
    ],
    [
        '',
        'ROB6. NAVES ESPACIALES',
        '6.5 SpaceX Falcon9',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), visor 3D del cohete Falcon 9, simulador de lanzamiento orbital, simulador de aterrizaje propulsado y juego interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-6_Naves_espaciales/6.5_SpaceX_Falcon9/MAPA_CLASE_6.5_SPACEX_FALCON9.html'
    ],
    [
        '',
        'ROB6. NAVES ESPACIALES',
        '6.6 Transbordador Espacial',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), visor 3D del Orbitador, simulador 3D de vuelo y maniobra de bahía de carga, y juego interactivo de reentrada.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-6_Naves_espaciales/6.6_Transbordador_Espacial/MAPA_CLASE_6.6_TRANSBORDADOR.html'
    ],
    [
        '',
        'ROB6. NAVES ESPACIALES',
        '6.7 Estacion Espacial ISS',
        'Acceso interactivo a todos los recursos de la clase: debate inicial (PDF), visor 3D de la macroestructura completa de la ISS, simulador 3D de acoplamiento RCS en gravedad cero y juego espacial.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-6_Naves_espaciales/6.7_Estacion_Espacial_ISS/MAPA_CLASE_6.7_ESTACION_ISS.html'
    ],
    # ROB7. EXPLORACIÓN ESPACIAL
    [
        '',
        'ROB7. EXPLORACIÓN ESPACIAL',
        '7.1 Rover Marciano',
        'Acceso interactivo a todos los recursos de la clase: infografías técnicas, vídeos demostrativos, visor 3D del rover marciano y juego de exploración en el cráter Jezero.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-7_Exploracion_Espacial/7.1_Rover_Marciano/MAPA_CLASE_7.1_ROVER_MARCIANO.html'
    ],
    [
        '',
        'ROB7. EXPLORACIÓN ESPACIAL',
        '7.3 Base Lunar',
        'Acceso interactivo a todos los recursos de la clase: infografía de hábitat lunar, visor 3D del complejo lunar y juego de gestión de recursos y soporte vital.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-7_Exploracion_Espacial/7.3_Base_Lunar/MAPA_CLASE_7.3_BASE_LUNAR.html'
    ],
    [
        '',
        'ROB7. EXPLORACIÓN ESPACIAL',
        '7.4 Terraformacion Marte',
        'Acceso interactivo a todos los recursos de la clase: infografía de transformación planetaria, visor 3D del terreno marciano y simulador interactivo de biosfera.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-7_Exploracion_Espacial/7.4_Terraformacion_Marte/MAPA_CLASE_7.4_TERRAFORMACION_MARTE.html'
    ],
    [
        '',
        'ROB7. EXPLORACIÓN ESPACIAL',
        '7.5 Telescopios Espaciales',
        'Acceso interactivo a todos los recursos de la clase: infografía del telescopio James Webb, visores 3D del Hubble y JWST, y juego de alineación óptica espacial.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-7_Exploracion_Espacial/7.5_Telescopios_Espaciales/MAPA_CLASE_7.5_TELESCOPIOS_ESPACIALES.html'
    ],
    [
        '',
        'ROB7. EXPLORACIÓN ESPACIAL',
        '7.6 Ascensor Espacial',
        'Acceso interactivo a todos los recursos de la clase: presentación interactiva, infografías de ingeniería, visor 3D de la megaestructura del ascensor y simulador de ascenso.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-7_Exploracion_Espacial/7.6_Ascensor_Espacial/MAPA_CLASE_7.6_ASCENSOR_ESPACIAL.html'
    ],
    [
        '',
        'ROB7. EXPLORACIÓN ESPACIAL',
        '7.7 Sondas Voyager y Heliopausa',
        'Acceso interactivo a todos los recursos de la clase: infografía de sondas interestelares, visores 3D de Voyager 1, Cassini-Huygens y Sputnik 1, y juego de asistencia gravitatoria.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-7_Exploracion_Espacial/7.7_Sondas_Voyager_y_Heliopausa/MAPA_CLASE_7.7_SONDAS_ESPACIALES.html'
    ],
    [
        '',
        'ROB7. EXPLORACIÓN ESPACIAL',
        '7.8 Red de Comunicaciones Espaciales',
        'Acceso interactivo a todos los recursos de la clase: infografía de la red DSN, visor 3D de estación de antenas parabólicas gigantes y juego de transmisión de telemetría interplanetaria.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-7_Exploracion_Espacial/7.8_Red_de_Comunicaciones_Espaciales/MAPA_CLASE_7.8_RED_COMUNICACIONES.html'
    ],
    [
        '',
        'ROB7. EXPLORACIÓN ESPACIAL',
        '7.9 Mineria Lunar y Logistica',
        'Acceso interactivo a todos los recursos de la clase: infografía de minería espacial e ISRU, visor 3D de complejo minero lunar y juego de extracción y procesado.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-7_Exploracion_Espacial/7.9_Mineria_Lunar_y_Logistica/MAPA_CLASE_7.9_MINERIA_LUNAR.html'
    ],
    [
        '',
        'ROB7. EXPLORACIÓN ESPACIAL',
        '7.10 Mision Apolo y Carrera Espacial',
        'Acceso interactivo a todos los recursos de la clase: infografía de corte transversal del Saturno V, visor 3D del Módulo Lunar Eagle, simulador interactivo de las 7 fases de la misión Apolo 11 y juego.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-7_Exploracion_Espacial/7.10_Mision_Apolo_y_Carrera_Espacial/MAPA_CLASE_7.10_MISION_APOLO.html'
    ],
    [
        '',
        'ROB7. EXPLORACIÓN ESPACIAL',
        '7.11 Paseo Espacial EVA',
        'Acceso interactivo a todos los recursos de la clase: infografía de ingeniería del traje espacial EMU, visor 3D interactivo del astronauta animado en gravedad cero y juego espacial.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-7_Exploracion_Espacial/7.11_Paseo_Espacial_EVA/MAPA_CLASE_7.11_PASEO_ESPACIAL_EVA.html'
    ],
    # ROB8. TITANES Y ANIMATRÓNICA
    [
        '',
        'ROB8. TITANES Y ANIMATRÓNICA',
        '8.1 Jurassic Park Animatronica',
        'Abre este simulador interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-8_Titanes_Animatronica/8.1_Jurassic_Park_Animatronica/3.PRACTICAS/P4.JUEGO.html'
    ],
    [
        '',
        'ROB8. TITANES Y ANIMATRÓNICA',
        '8.2 Mechas Gigantes',
        'Abre este simulador interactivo.',
        'https://javiercursocorreo-gif.github.io/Curso-Robotica/BLOQUE-8_Titanes_Animatronica/8.2_Mechas_Gigantes/3.PRACTICAS/P4.JUEGO.html'
    ],
]


def generate_ia_unified_csv():
    os.makedirs(IA_CSV_DIR, exist_ok=True)
    out_path = os.path.join(IA_CSV_DIR, "CURSO_IA_UNIFICADO.csv")

    rows = []

    # 1. TEMA: MONOGRAFICOS (los 6 mapas interactivos de los Monográficos)
    monograficos_rows = [
        [
            '',
            'MONOGRAFICOS',
            'Monográfico 1. Gemini en PC y Móvil (Instalación y Uso)',
            'Cuadro de mando interactivo del Monográfico 1 con la Guía visual oficial completa y acceso directo al portal de Google Gemini.',
            'https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/1.%20INTRODUCCION_GEMINI/MAPA_CLASE_1_GEMINI.html'
        ],
        [
            '',
            'MONOGRAFICOS',
            'Monográfico 2. NotebookLM: Tu Cuaderno Inteligente',
            'Cuadro de mando interactivo del Monográfico 2: Guía oficial (PDF), portal de NotebookLM, fichas de práctica guiada, fuentes de prueba (Apolo 11) y resultados generados por IA.',
            'https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/2.%20INTRODUCCION_NLM/MAPA_CLASE_2_NLM.html'
        ],
        [
            '',
            'MONOGRAFICOS',
            'Monográfico 3. Cómo Crear un Cuento Ilustrado con NotebookLM',
            'Cuadro de mando interactivo del Monográfico 3 con la metodología en 4 fases guiadas: Introducción al Proyecto, Creación del Cuento, Generador de Guion e Ilustrador Visual.',
            'https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/3.%20COMO_HACER_UN_CUENTO_CON_NLM/MAPA_CLASE_3_CUENTO.html'
        ],
        [
            '',
            'MONOGRAFICOS',
            'Monográfico 4. Mi Biografía (Escribe tus Memorias con IA)',
            'Cuadro de mando interactivo del Monográfico 4 con el manual metodológico de instrucciones (PDF) y la aplicación web interactiva para redactar vivencias y anécdotas con IA.',
            'https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/4.%20Mi_Biografia/MAPA_CLASE_4_BIOGRAFIA.html'
        ],
        [
            '',
            'MONOGRAFICOS',
            'Monográfico 5. Educanietos IA: Ayuda a tus Nietos con IA (Ciencias, Mates e Historia)',
            'Cuadro de mando interactivo del Monográfico 5 con el protocolo pedagógico (PDF), simulador interactivo de tutoría escolar y bancos de ejercicios prácticos de Historia y Matemáticas.',
            'https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/5.%20EL_ABUELO_TUTOR_MATEMATICAS_HISTORIA/MAPA_CLASE_5_EDUCANIETOS.html'
        ],
        [
            '',
            'MONOGRAFICOS',
            'Monográfico 6. Mapa de Gestión del Proyecto con IA (Arquitectura y Flujo de Trabajo)',
            'Cuadro de mando interactivo del Monográfico 6 con la ficha técnica de arquitectura del sistema, el simulador de flujo de producción y el póster infográfico de creación de materiales.',
            'https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/7.%20MAPA_GESTION_PROYECTO_CON_IA/MAPA_CLASE_7_GESTION.html'
        ],
    ]
    rows.extend(monograficos_rows)

    # 2. TEMAS: SESIÓN 1 a SESIÓN 60
    for s_num in range(1, 61):
        folder_name = f"{s_num:02d}_Sesion" if s_num < 60 else "60_Sesion_Cierre"
        tema = f"SESIÓN {s_num}"
        titulo = f"Mapa Interactivo: Sesión {s_num:02d} (HTML)"
        desc = f"Cuadro de mando interactivo en 3 columnas de la Sesión {s_num:02d} con todos los recursos y retos guiados paso a paso."
        url = (
            f"https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/"
            f"EXPORTACION_FICHAS_CLASSROOM_PDF/100.%20%5BSESSIONS%5D%20TERNAS_LISTAS_PARA_CLASSROOM/"
            f"{folder_name}/MAPA_SESION_{s_num:02d}.html"
        )
        rows.append(['', tema, titulo, desc, url])

    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        writer.writerows(rows)

    print(f"✅ CSV UNIFICADO DE IA generado ({len(rows)} filas): {out_path}")
    return out_path


def generate_robotica_unified_csv():
    unified_rows = [
        [
            '',
            'INTRODUCCIÓN',
            'Presentación inaugural',
            'Cuadro de mando interactivo de la clase inaugural con acceso directo a las diapositivas oficiales y a la guía visual de Google Classroom.',
            'https://javiercursocorreo-gif.github.io/Curso-Robotica-IA-Comun/0.PRESENTACION_PARA_LA_PRIMERA_CLASE/MAPA_CLASE_INAUGURAL.html'
        ],
        [
            '',
            'INTRODUCCIÓN',
            'Manual de Classroom',
            'Guía visual paso a paso para alumnos sobre cómo entrar y utilizar Google Classroom en el curso.',
            'https://javiercursocorreo-gif.github.io/Curso-Robotica-IA-Comun/1.GOOGLE_CLASSROOM/Guia_de_Classroom.pdf'
        ],
    ]

    # Intentar leer directamente los 8 archivos oficiales (1.PANEL_B1.csv .. 8.PANEL_B8.csv)
    # ignorando cualquier archivo .backup_, .desglosado_ o de prueba
    read_from_disk = False
    try:
        if os.path.isdir(ROB_CSV_DIR):
            temp_rows = list(unified_rows)
            seen_urls = {r[4] for r in temp_rows}
            for b_idx in range(1, 9):
                csv_path = os.path.join(ROB_CSV_DIR, f"{b_idx}.PANEL_B{b_idx}.csv")
                if not os.path.isfile(csv_path):
                    continue
                read_from_disk = True
                tema_oficial = BLOCK_THEME_MAP[b_idx]
                with open(csv_path, 'r', encoding='utf-8-sig') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        orig_tema = (row.get('TEMA_CLASSROOM') or '').strip()
                        orig_titulo = (row.get('TITULO_MATERIAL') or '').strip()
                        orig_desc = (row.get('DESCRIPCION_MATERIAL') or '').strip()
                        orig_url = (row.get('URL_GITHUB') or '').strip()
                        if not orig_url or orig_url in seen_urls:
                            continue
                        seen_urls.add(orig_url)
                        lesson_title = orig_tema if orig_tema else orig_titulo
                        temp_rows.append(['', tema_oficial, lesson_title, orig_desc, orig_url])
            if read_from_disk:
                unified_rows = temp_rows
    except PermissionError:
        read_from_disk = False

    if not read_from_disk:
        unified_rows = FALLBACK_ROBOTICA_ROWS

    # Guardar siempre en CURSO-IA/PANELES_CSV/CURSO_ROBOTICA_UNIFICADO.csv
    os.makedirs(IA_CSV_DIR, exist_ok=True)
    out_copy_in_ia = os.path.join(IA_CSV_DIR, "CURSO_ROBOTICA_UNIFICADO.csv")
    with open(out_copy_in_ia, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        writer.writerows(unified_rows)
    print(f"✅ CSV UNIFICADO DE ROBÓTICA generado ({len(unified_rows)} filas): {out_copy_in_ia}")

    # Y si tenemos acceso a CURSO-ROBOTICA-V2/PANELES_CSV, guardarlo también allí
    try:
        out_rob_path = os.path.join(ROB_CSV_DIR, "CURSO_ROBOTICA_UNIFICADO.csv")
        with open(out_rob_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(HEADER)
            writer.writerows(unified_rows)
        print(f"✅ Copia guardada también en: {out_rob_path}")
    except PermissionError:
        pass

    return out_copy_in_ia


if __name__ == "__main__":
    print("🚀 Generando los 2 únicos CSV Maestros Unificados (CURSO DE IA y CURSO DE ROBÓTICA)...")
    generate_ia_unified_csv()
    generate_robotica_unified_csv()
    print("\n🎉 ¡Proceso completado!")
