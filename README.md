# FiberNeuro - Paquete Final

Sistema integrado de gestión para FiberNeuro con backend API, aplicación móvil Flutter y módulo de autenticación.

## Estructura del Proyecto

```
paquete-final/
├── 03_CODIGO_FUENTE/
│   ├── fiberneuro-api/          # Backend API (Docker)
│   └── fiberneuro-campo/        # App Flutter para técnicos
├── docs/                         # Documentación
└── scripts/                      # Scripts de utilidad
```

## Guía de Configuración Rápida

### 1. Clonar repositorio
```bash
git clone https://github.com/fiberneuro/paquete-final.git
cd paquete-final
```

### 2. Backend (Docker)
```bash
cd 03_CODIGO_FUENTE/fiberneuro-api
cp .env.example .env  # Editar variables de entorno
docker-compose up -d
```

### 3. Aplicación Móvil (Flutter)
```bash
cd ../fiberneuro-campo
flutter pub get
flutter build apk --release
# Instalar APK en dispositivos de técnicos
```

### 4. Inicializar usuarios
```bash
python app/auth/script_init_auth.py
```

## Requisitos Previos

- **Backend**: Docker y Docker Compose
- **Móvil**: Flutter SDK (v3.0 o superior)
- **Autenticación**: Python 3.8+

## Variables de Entorno

Copia `.env.example` a `.env` en la carpeta `fiberneuro-api` y configura:

```
DATABASE_URL=
API_PORT=8000
DEBUG=false
```

## Documentación

Ver la carpeta `docs/` para documentación detallada.

## Licencia

[Por definir]
