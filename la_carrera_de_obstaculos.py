"""/*
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 */"""

run_jump = ["run", "jump", "run", "jump"]
valla_suelo = "_|_|"

def carrera(run_jump, valla_suelo):
    result = ""

    if not len(run_jump) == len(valla_suelo):
        return "The distance between both fields is not correct"
    
    for accion, field in zip(run_jump, valla_suelo):

        if not accion in ["jump", "run"] or not field in ["|", "_"]:
            return "Wrong characters."
        
        if field == "|" and accion == "run":
            result += "/"
        
        elif field == "_" and accion == "jump":
            result += "x"

        else:
            result += field
        
    if valla_suelo == result:
        return f"You've finished the field correctly."
    else:
        return f"You've missed some obstacles. {result}"
    


print(carrera(run_jump, valla_suelo))

         







