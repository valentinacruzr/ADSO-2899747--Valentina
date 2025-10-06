#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Gráficas para Plantilla LaTeX - Gestión de Talento Humano
Genera gráficas de ejemplo relacionadas con métricas de RRHH, digitalización y tecnologías web
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams
import os

# Configuración global para mejorar la calidad de las gráficas
plt.style.use('default')
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 10
rcParams['axes.labelsize'] = 11
rcParams['axes.titlesize'] = 12
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9
rcParams['legend.fontsize'] = 9
rcParams['figure.titlesize'] = 13
rcParams['savefig.dpi'] = 300
rcParams['savefig.bbox'] = 'tight'
rcParams['savefig.pad_inches'] = 0.1

# Crear directorio de gráficas si no existe
graphics_dir = 'graphics'
os.makedirs(graphics_dir, exist_ok=True)

def generar_metricas_dora():
    """Genera gráfica de barras con métricas de RRHH por área"""

    # Datos de ejemplo: métricas de RRHH por área
    areas = ['Producción', 'Administración', 'Ventas', 'Logística']
    asistencia_promedio = [85.2, 92.7, 78.1, 88.4]  # porcentaje asistencia
    permisos_mes = [3.2, 1.8, 4.3, 2.1]  # permisos por mes

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Gráfica 1: Asistencia promedio
    bars1 = ax1.bar(areas, asistencia_promedio, color=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D'])
    ax1.set_title('Asistencia Promedio por Área (%)')
    ax1.set_ylabel('Porcentaje de asistencia')
    ax1.set_ylim(0, 100)

    # Añadir valores en las barras
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height:.1f}', ha='center', va='bottom')

    # Gráfica 2: Permisos por mes
    bars2 = ax2.bar(areas, permisos_mes, color=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D'])
    ax2.set_title('Permisos por Mes')
    ax2.set_ylabel('Número promedio de permisos')
    ax2.set_ylim(0, 6)

    # Añadir valores en las barras
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height:.1f}', ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/metricas_dora.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/metricas_dora.png', format='png')
    plt.close()
    print("✓ Generada: metricas_dora.pdf/png")

def generar_evolucion_temporal():
    """Genera gráfica de líneas mostrando evolución temporal de métricas de RRHH"""

    # Datos de ejemplo: evolución mensual de métricas RRHH
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec']
    asistencia_promedio = [82, 85, 87, 89, 91, 93, 94, 95, 96, 97, 98, 98]
    solicitudes_permisos = [25, 22, 20, 18, 15, 12, 10, 8, 7, 6, 5, 4]
    capacitaciones_completadas = [2, 4, 6, 8, 10, 12, 15, 18, 20, 22, 24, 26]

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Eje Y izquierdo: Asistencia y Capacitaciones
    color = '#2E86AB'
    ax1.set_xlabel('Mes')
    ax1.set_ylabel('Asistencia (%) / Capacitaciones Completadas', color=color)
    line1 = ax1.plot(meses, asistencia_promedio, color=color, marker='o', linewidth=2,
                     label='Asistencia Promedio (%)')
    line2 = ax1.plot(meses, capacitaciones_completadas, color='#F18F01', marker='s', linewidth=2,
                     label='Capacitaciones Completadas')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, 100)

    # Eje Y derecho: Solicitudes de permisos
    ax2 = ax1.twinx()
    color = '#C73E1D'
    ax2.set_ylabel('Solicitudes de Permisos', color=color)
    line3 = ax2.plot(meses, solicitudes_permisos, color=color, marker='^', linewidth=2,
                     label='Solicitudes de Permisos')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(0, 30)

    # Leyenda combinada
    lines = line1 + line2 + line3
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='center right')

    plt.title('Evolución de Métricas de Gestión de Talento Humano (2024)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/evolucion_metricas.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/evolucion_metricas.png', format='png')
    plt.close()
    print("✓ Generada: evolucion_metricas.pdf/png")

def generar_correlacion_practicas():
    """Genera gráfica de dispersión mostrando correlación entre digitalización y eficiencia en RRHH"""

    np.random.seed(42)  # Para reproducibilidad

    # Datos simulados: correlación entre nivel de digitalización y eficiencia RRHH
    n_empresas = 25
    digitalizacion = np.random.normal(70, 15, n_empresas)
    digitalizacion = np.clip(digitalizacion, 20, 95)

    # Correlación positiva con algo de ruido
    eficiencia = 0.8 * digitalizacion + np.random.normal(0, 8, n_empresas) + 10
    eficiencia = np.clip(eficiencia, 30, 100)

    # Tamaños basados en el número de empleados
    num_empleados = np.random.randint(10, 200, n_empresas)

    plt.figure(figsize=(10, 7))
    scatter = plt.scatter(digitalizacion, eficiencia, s=num_empleados/5,
                         c=num_empleados, cmap='viridis', alpha=0.7, edgecolors='black', linewidth=0.5)

    # Línea de tendencia
    z = np.polyfit(digitalizacion, eficiencia, 1)
    p = np.poly1d(z)
    plt.plot(digitalizacion, p(digitalizacion), "--", color='red', linewidth=2, alpha=0.8)

    plt.xlabel('Nivel de Digitalización (%)')
    plt.ylabel('Eficiencia en Gestión de Talento Humano (índice)')
    plt.title('Correlación entre Digitalización y Eficiencia en RRHH')

    # Colorbar para número de empleados
    cbar = plt.colorbar(scatter)
    cbar.set_label('Número de Empleados')

    # Añadir estadísticas
    correlation = np.corrcoef(digitalizacion, eficiencia)[0,1]
    plt.text(0.05, 0.95, f'Correlación: r = {correlation:.3f}',
             transform=plt.gca().transAxes, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/correlacion_devops.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/correlacion_devops.png', format='png')
    plt.close()
    print("✓ Generada: correlacion_devops.pdf/png")

def generar_comparacion_metodologias():
    """Genera gráfica de radar comparando tecnologías frontend"""

    # Datos para comparación de tecnologías frontend
    categorias = ['Facilidad\nUso', 'Performance', 'Comunidad', 'Curva\nAprendizaje',
                  'Ecosistema', 'Mantenibilidad']

    # Puntuaciones (1-10) para cada tecnología
    react_scores = [9, 9, 10, 7, 9, 8]
    angular_scores = [7, 8, 9, 8, 8, 9]
    vue_scores = [9, 8, 7, 6, 6, 8]

    # Configurar gráfica de radar
    angles = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()
    angles += angles[:1]  # Cerrar el círculo

    react_scores += react_scores[:1]
    angular_scores += angular_scores[:1]
    vue_scores += vue_scores[:1]

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

    # Dibujar las líneas para cada tecnología
    ax.plot(angles, react_scores, 'o-', linewidth=2, label='React', color='#2E86AB')
    ax.fill(angles, react_scores, alpha=0.25, color='#2E86AB')

    ax.plot(angles, angular_scores, 's-', linewidth=2, label='Angular', color='#F18F01')
    ax.fill(angles, angular_scores, alpha=0.25, color='#F18F01')

    ax.plot(angles, vue_scores, '^-', linewidth=2, label='Vue.js', color='#C73E1D')
    ax.fill(angles, vue_scores, alpha=0.25, color='#C73E1D')

    # Configurar etiquetas y límites
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categorias)
    ax.set_ylim(0, 10)
    ax.set_yticks(range(0, 11, 2))
    ax.set_yticklabels(range(0, 11, 2))
    ax.grid(True)

    plt.title('Comparación de Tecnologías Frontend', size=14, y=1.08)
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/comparacion_metodologias.pdf', format='pdf', bbox_inches='tight')
    plt.savefig(f'{graphics_dir}/comparacion_metodologias.png', format='png', bbox_inches='tight')
    plt.close()
    print("✓ Generada: comparacion_metodologias.pdf/png")

def generar_tabla_frameworks():
    """Genera una tabla LaTeX con tecnologías utilizadas"""

    tabla_latex = r"""
\begin{table}[htbp]
\centering
\caption{Tecnologías utilizadas en el desarrollo del sistema}
\label{tab:frameworks}
\small
\begin{tabular}{lccc}
\toprule
\textbf{Tecnología} & \textbf{Lenguaje} & \textbf{Uso} & \textbf{Ventajas} \\
\midrule
React & JavaScript & Frontend & Componentes reutilizables \\
Spring Boot & Java & Backend & Productividad empresarial \\
MySQL & SQL & Base de datos & Integridad relacional \\
JWT & - & Autenticación & Seguridad stateless \\
\bottomrule
\end{tabular}
\end{table}
"""

    # Guardar tabla en archivo
    with open(f'tables/frameworks_comparison.tex', 'w', encoding='utf-8') as f:
        f.write(tabla_latex.strip())

    print("✓ Generada: frameworks_comparison.tex")

def main():
    """Función principal para generar todas las gráficas"""
    print("🎨 Generando gráficas para plantilla LaTeX...")
    print("=" * 50)
    
    try:
        generar_metricas_dora()
        generar_evolucion_temporal()
        generar_correlacion_practicas()
        generar_comparacion_metodologias()
        generar_tabla_frameworks()
        
        print("=" * 50)
        print("✅ ¡Todas las gráficas y tablas fueron generadas exitosamente!")
        print("\nArchivos generados:")
        print("📊 Gráficas PDF (para LaTeX): graphics/")
        print("🖼️  Gráficas PNG (para vista previa): graphics/")
        print("📋 Tabla LaTeX: tables/frameworks_comparison.tex")
        
    except Exception as e:
        print(f"❌ Error al generar gráficas: {e}")
        raise

if __name__ == "__main__":
    main()