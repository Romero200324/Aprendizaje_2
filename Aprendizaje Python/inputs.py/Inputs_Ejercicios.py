
# Seccion 1 
este_curso = 1.5 # Colocar los valors de trabajo
rapido = 2.5
promedio = 4
lento = 7

# Operaciones (Formula a usar)
# Variable = 100 - (primer_datos / segundo_dato * 100)

promedio_del_video_mas_rapido = 100 - este_curso / rapido * 100
promedio_del_video_intervalo = 100 - este_curso / promedio * 100
promedio_del_video_mas_lento = 100 - este_curso / lento * 100

ordenacion_de_todos_los_valores = ([promedio_del_video_mas_rapido, promedio_del_video_intervalo, int(promedio_del_video_mas_lento)])
ordenacion_de_todos_los_valores.sort()

# Sustión y resultado
print(f"Ver este video dura el {promedio_del_video_mas_rapido} % del video más rapido ")
print(f"Ver este video dura el {promedio_del_video_intervalo} % del video de intervalo")
print(f"Ver este video te ahorra el {int(promedio_del_video_mas_lento)} % de ver el video más lento")
print(f"De todos los cursos ansido ordenados de manera acedente para que tomes la mejor dección {ordenacion_de_todos_los_valores}")


# Seccion 2 

# La parte eliminada de un video (Crudo)

crudo_promedio = 5
crudo_de_este_video = 3.5

# Formula de operaciones 
tiempo_de_video_crudo_de_este_video = 100 - promedio / crudo_promedio * 100
tiempo_de_video_crudo_promedio = 100 - este_curso / crudo_de_este_video * 100

print(f"""
        El promedio de ver este video es de  %{tiempo_de_video_crudo_de_este_video} 
        A comparación de los videos promedio es de %{int(tiempo_de_video_crudo_promedio)}""")


#Sustitucion de los valores y resultado.



# C ( Problema )
# Ver dies horas de este curso a cuanto equievalen a otros cursos 

# Datos que tenemos 

# Formula de operaciones 
este_curso_de_10_horas_de_video = este_curso * 10
otros_cursos_de_10_horas_de_video = promedio * 10


# Sustitucion y resultado 
print(f"Esta es la cantidad de ver 10 horas de video {int(este_curso_de_10_horas_de_video)} horas")
print(f"En comparación de otros videos es la comparacion de video a {otros_cursos_de_10_horas_de_video} horas")
