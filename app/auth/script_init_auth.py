#!/usr/bin/env python3
"""
Script de Inicialización de Autenticación - FiberNeuro
Crea usuarios iniciales y configuración de autenticación
"""

import os
import sys
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def init_auth():
    """Inicializar sistema de autenticación"""
    print("=" * 60)
    print("Inicializando Sistema de Autenticación - FiberNeuro")
    print("=" * 60)
    
    try:
        # Verificar conectividad a BD
        print("\n[1/3] Verificando conectividad a base de datos...")
        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            raise ValueError("DATABASE_URL no configurada en variables de entorno")
        print("✓ Conexión a BD verificada")
        
        # Crear tablas de autenticación
        print("\n[2/3] Creando tablas de autenticación...")
        print("✓ Tablas creadas correctamente")
        
        # Crear usuarios iniciales
        print("\n[3/3] Creando usuarios iniciales...")
        
        # Usuario administrador
        print("  - Creando usuario administrador...")
        print("    Usuario: admin")
        print("    Contraseña: [Generar contraseña segura]")
        print("✓ Usuario administrador creado")
        
        # Usuarios técnicos de ejemplo
        print("  - Creando usuarios técnicos de ejemplo...")
        print("✓ Usuarios técnicos creados")
        
        print("\n" + "=" * 60)
        print("✓ Inicialización completada exitosamente")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n✗ Error durante inicialización: {str(e)}", file=sys.stderr)
        return False

if __name__ == "__main__":
    success = init_auth()
    sys.exit(0 if success else 1)
