-- ==============================================================================
-- crear_pestana_picores.applescript
-- Añade una nueva pestaña en 2ª posición (justo detrás de 'Alergia_medicamentos')
-- en el libro 'Seguimiento medicinas ÚLTIMO.xls'.
-- Extrae y sistematiza todos los medicamentos que han provocado picores,
-- sarpullidos o prurito, con fecha, medicamento, características y evolución.
-- ==============================================================================

set excelFilePath to "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/IA TEMAS VARIOS/SEGUMINENTO MEDICINAS JAVI/Seguimiento medicinas ÚLTIMO.xls"
set hfsPath to (POSIX file excelFilePath) as text

tell application "Microsoft Excel"
    activate
    -- Abrir libro de trabajo
    set wb to open workbook workbook file name hfsPath
    
    -- Si la pestaña ya existe de una ejecución previa, eliminarla para recrearla limpia
    set sheetExists to false
    try
        set oldSheet to worksheet "Picores_Medicamentos" of wb
        set sheetExists to true
    end try
    
    if sheetExists then
        set display alerts to false
        delete worksheet "Picores_Medicamentos" of wb
        set display alerts to true
    end if
    
    -- Crear la nueva pestaña en la 2ª posición (justo después de la hoja 1 'Alergia_medicamentos')
    set ws to make new worksheet at after worksheet 1 of wb
    set name of ws to "Picores_Medicamentos"
    
    -- 1. Encabezados
    set value of range "A1:G1" of ws to {"FECHA", "MEDICAMENTO", "FAMILIA / GRUPO", "MOTIVO PRESCRIPCIÓN", "CARACTERÍSTICAS DEL PICOR / REACCIÓN", "¿SE QUITÓ / SE PASÓ? (EVOLUCIÓN)", "MEDIDAS / TRATAMIENTO"}
    
    -- 2. Filas de Datos (Sistematizadas cronológicamente para el Alergólogo)
    set value of range "A2:G2" of ws to {"1997", "CLAMOXIL (Amoxicilina 500)", "Betalactámico (Penicilina)", "Amigdalitis aguda", "Sarpullido eritematoso difuso en el pecho.", "Se quitó al suspender el tratamiento. En 2017 tomó Amoxicilina 750 y volvieron a brotar algunos picores.", "Suspensión del fármaco. Sospecha firme de hipersensibilidad a aminopenicilinas."}
    
    set value of range "A3:G3" of ws to {"01/02/1999", "VELMONIT 500 (Ciprofloxacino)", "Fluorquinolona", "Amigdalitis aguda", "Sarpullido pruriginoso en el pecho acompañado de nerviosismo agudo.", "Se quitó tras la retirada del fármaco. (En 2022 tomó Ciprofloxacino y los picores cesaron al retirar Permixon).", "Suspendido a los 3 días de inicio."}
    
    set value of range "A4:G4" of ws to {"07/05/1999", "BRONGENIT (Cotrimoxazol)", "Sulfamida (Sulfametoxazol + Trimetoprima)", "Prostatitis", "Picores cutáneos a la 3ª pastilla. Agitación y nerviosismo a la 5ª y 6ª pastilla.", "Se resolvieron completamente los picores tras suspender el medicamento.", "Suspendido obligatoriamente a la 6ª pastilla por prurito creciente."}
    
    set value of range "A5:G5" of ws to {"11/05/1999", "VIBRACINA (Doxiciclina)", "Tetraciclina", "Prostatitis", "Tomado 7 días completos. El último día brotó sarpullido pruriginoso en el costado.", "El sarpullido remitió en los días posteriores a finalizar los 7 días de pauta.", "Fin de pauta; posterior disbiosis gastrointestinal transitoria tratada con dieta."}
    
    set value of range "A6:G6" of ws to {"08/10/2001", "SURNOX (Ofloxacino)", "Fluorquinolona", "Prostatitis", "A la 2ª pastilla picores intensos en la espalda + agitación nerviosa.", "Al 6º día se pasaron por completo los picores. Pudo completar 18 pastillas con Orfidal.", "Coadministración de ansiolítico (Orfidal); el prurito cedió espontáneamente al 6º día."}
    
    set value of range "A7:G7" of ws to {"01/12/2003", "BENERVA (Vitamina B1)", "Vitamina hidrosoluble (Tiamina)", "Suplemento vitamínico", "Prurito intenso desde la 1ª pastilla; granos en frente y pecho. En 2ª prueba (abril 2004) picadura roja en dedo pie.", "Se quitó por completo a los 5 días aproximadamente.", "Retirada de la vitamina B1; remisión espontánea de la lesión."}
    
    set value of range "A8:G8" of ws to {"01/06/2004", "MICOSPORT (Bifonazol)", "Antifúngico Imidazólico", "Micosis cutánea (hongos)", "Eficaz contra los hongos a los 7 días, pero el 7º día brotaron granos en frente y pecho.", "Erupción papulosa tardía que remitió al suspender tras curar la micosis.", "Suspensión al séptimo día tras erradicación del hongo."}
    
    set value of range "A9:G9" of ws to {"01/08/2004", "ALPRAZOLAM 0,25 mg", "Benzodiazepina", "Ansiedad / insomnio", "Picores sin granos visibles, descritos como pinchazos/pinchitos en antebrazos y cabeza.", "Duró 5 días y se pasó por completo.", "Autolimitado; remisión en 5 días."}
    
    set value of range "A10:G10" of ws to {"26/12/2006", "KLACID UNIDIA 500 (Claritromicina)", "Macrólido", "Infección respiratoria", "Picores crecientes e intensos en las piernas, taquicardia/palpitaciones y nerviosismo.", "Desapareció tras la interrupción inmediata del antibiótico.", "Suspendido a la 3ª pastilla de forma obligatoria."}
    
    set value of range "A11:G11" of ws to {"12/03/2015", "AZITROMICINA 500 mg", "Macrólido Azálido", "Recaída de gripe / Faringitis", "Con la 1ª pastilla picores en ambos brazos.", "Se pasaron solos y desaparecieron a las 3 horas. La 2ª y 3ª pastillas no dieron ningún picor.", "Ninguna; tolerancia adquirida en tomas sucesivas (en 2017 tolerado sin efectos)."}
    
    set value of range "A12:G12" of ws to {"20/04/2017", "AMOXICILINA 750 mg", "Betalactámico (Penicilina)", "Extracción muela juicio", "Tomó 11 pastillas; algunos picores cutáneos y palpitaciones la 4ª tarde.", "Picores leves transitorios que cedieron al concluir el ciclo.", "Completó la pauta con molestias leves; confirma reactividad a aminopenicilinas."}
    
    set value of range "A13:G13" of ws to {"27/10/2022", "PERMIXON 160 mg (Serenoa repens)", "Fitoterapia Urológica", "PSA elevado / Prostatitis", "Al 5º día picores aleatorios (tomaba también Cipro). En 19/12/2025 al 7º día picores en brazos y piernas.", "En 2022 se quitaron al dejar Permixon (al reanudar volvieron). En 2025 continuó tomándolo.", "En 2022 suspensión transitoria; en 2025 continuación bajo vigilancia clínica."}
    
    set value of range "A14:G14" of ws to {"17/03/2023", "PROCTOIAL RECTAL", "Ácido Hialurónico tópico", "Fisura anal", "Aplicación cada 12 horas. Escozor y picor perianal local con la segunda aplicación.", "Picor circunscrito a la zona de contacto mucoso.", "Uso continuado vigilado / ajuste de dosis tópica."}
    
    set value of range "A15:G15" of ws to {"08/02/2024", "NASONEX (Furoato Mometasona)", "Corticoide tópico nasal", "Catarro vías altas", "Pequeños picores aleatorios con la 1ª inhalación.", "Se pasó al poco rato. En la 2ª toma y tomas siguientes de 14 días no dio ningún picor.", "Ninguna; autolimitado en minutos. Tolerancia completa posterior."}
    
    set value of range "A16:G16" of ws to {"Mayo 2024", "INFILTRACIÓN CORTICOIDES", "Corticoide local parenteral", "Dolor cresta ilíaca izq.", "Picores corporales durante 5 días tras infiltración en cresta ilíaca izquierda.", "Duró 5 días y remitió por completo espontáneamente.", "Autolimitado en 5 días; aclaramiento natural del depósito corticoideo."}
    
    set value of range "A17:G17" of ws to {"15/01/2025", "LEVOFLOXACINO 500 mg", "Fluorquinolona", "Infección respiratoria La Moraleja", "Picores en brazos y axilas con las 3 primeras pastillas; en las 3 siguientes en las piernas.", "El último día ya no tuvo ningún picor.", "Aplicación de crema de Urea hidratante para calmar el prurito; no precisó Aerius."}
    
    set value of range "A18:G18" of ws to {"14/08/2026", "EZETIMIBA 10 mg", "Hipolipemiante (Inhibidor NPC1L1)", "Colesterol c-LDL", "Prurito cutáneo generalizado migratorio durante los primeros 15 días de tratamiento.", "No se quitó solo; requirió tratamiento farmacológico continuo.", "Toma diaria de antihistamínico (Aerius) y crema de urea. Suspendido por ineficacia y prurito."}
    
    set value of range "A19:G19" of ws to {"08/10/2026", "PITAVASTATINA (Livazo)", "Estatina hipolipemiante", "Colesterol c-LDL", "Picores corporales difusos a la 3ª semana de tratamiento continuo.", "Se quitó al suspender el tratamiento.", "Toma de antihistamínico Aerius (1 día) y suspensión definitiva; retorno a Atorvastatina."}
    
    set value of range "A20:G20" of ws to {"2022 - 2026", "ATORVASTATINA 20 mg (CONTROL)", "Estatina hipolipemiante", "Colesterol c-LDL", "CERO PICORES (Tolerancia cutánea óptima; dato clave de contraste para el Alergólogo).", "Tolerancia excelente continuada permanente (mantiene LDL en 64).", "Tratamiento de elección tolerado sin ningún prurito."}
    
    -- 3. Formateo Visual Profesional
    -- Encabezados
    set font size of font object of range "A1:G1" of ws to 11
    set bold of font object of range "A1:G1" of ws to true
    set color index of font object of range "A1:G1" of ws to 2 -- Blanco
    set color of interior object of range "A1:G1" of ws to {30, 58, 138} -- Azul Clínico Marino (#1E3A8A)
    set row height of row 1 of ws to 30
    
    -- Datos
    set font size of font object of range "A2:G20" of ws to 9.5
    set wrap text of range "A1:G20" of ws to true
    
    -- Colores alternos y fila de control de contraste
    repeat with r from 2 to 19
        if (r mod 2) is 0 then
            set color of interior object of range ("A" & r & ":G" & r) of ws to {248, 250, 252} -- Gris muy tenue
        else
            set color of interior object of range ("A" & r & ":G" & r) of ws to {255, 255, 255} -- Blanco
        end if
    end repeat
    
    -- Fila 20 (Control Atorvastatina) en verde suave de tolerancia
    set color of interior object of range "A20:G20" of ws to {240, 253, 244}
    set color of interior object of cell "B20" of ws to {220, 252, 231}
    
    -- Bordes
    try
        set line style of border object of range "A1:G20" of ws to continuous
        set weight of border object of range "A1:G20" of ws to thin
        set color of border object of range "A1:G20" of ws to {203, 213, 225}
    end try
    
    -- Anchos de Columna Calibrados
    set column width of column 1 of ws to 14
    set column width of column 2 of ws to 25
    set column width of column 3 of ws to 23
    set column width of column 4 of ws to 18
    set column width of column 5 of ws to 42
    set column width of column 6 of ws to 36
    set column width of column 7 of ws to 26
    
    -- Autoajuste de altura de filas para texto envuelto
    set autofit of entire row of range "A2:G20" of ws to true
    
    -- Guardar y cerrar
    save wb
    close wb saving no
end tell
