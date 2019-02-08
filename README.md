# Minecraft LEVERAGE-Web
    Pagina web encargada de Administrar Cuentas de Usuarios y brindar informacion a los mismos. Asegurar el perfecto funcionamiento del Sistema AntiParche acoplado al Launcher LEVERAGE
    La API brinda todo tipo de informacion, tanto para el AntiParches como para la web en si.
    Incorpora diversas funcionalidades complejas con RCON y Query al Servidor LEVERAGE, e incluso modificacion de archivos internos de dicho server

# Funcionalidades Servidor LEVERAGE:
    * Web:
        - Cambiar Plantilla (Mas Moderna y usable)
        - Autenticacion y Registro
        - Perfil de Usuario (Skins, Cambiar Informacion, Cambiar Password, Recuperar Cuenta)
        - Sistema AntiTrampas (Whitelist en el Server, RCON y Comprabar Datos reales)
        - Informacion del Servidor (Informacion Estatica [Descarga, Instalacion, Empezar, Reglamento y Enlaces] y Dinamica [Noticias, Lanzamientos, Eventos recreativos])
        - Lista de Baneados (Usuarios y Objetos)
        - Sistema de Donacion Mejorada (Spam, kitar dicho spam si dona nauta cada mes [Separar Usuario y Premium])
        - Informacion Testing y Oficial Server (Situacion Actual de Cada uno)
        - Informacion del Grupo de Trabajo (Privilegios y Manejo del Servidor - De forma externa e interna)
        - Zona admin:
            . RCON (Ver consola y enviar comandos)
            . Accion con los Usuarios (Kickear, Banear, Mensajes Privados y Cambiar datos)
            . Ajuste de Datos en el Sistema AntiParche (Mods, Versiones y Paquetes de Recursos permitidos y datos del mimso antiparches [Version y URL Update]) - Lleado JSON y Eliminacion individual
            . Ajuste de Privilegios
            . Busqueda, Edicion y Eliminacion de Usuarios
        - API (AntiParches, Datos internos Web y RCON)		-> Cuanto mas API menos pincha (Modulos Genericos)
        - Reportes de Bugs
        - Donacion de Tarjeta Nauta (Dar algo a cambio en el juego)

        * Launcher:
        - Organizacion de Datos (Mods, Version y ResourcePack)
        - Donacion Tarjeta Nauta API (Mejorar Sistema de Donacion)
        - Sistema de Cache (Descargar Noticias, Anuncios y otras cosas y comprabar nadamas si cambio algo [API que diga fecha de algun cambio para actualizar cache])
        - Añadir Compatibilidad para la 1.13
        - AntiTramps (Chequear Mods, Version, Paquete de Recursos y antes de entrar [Monitoriar cuando entras al Servidor])
        - Lista de Usuario (Detallado con Cabeza del Skins)
        - Organizar Modo Offline y Online (Mensajes, Funcionalidades, )
        - Mensaje de OFFLINE activar para registrarse directamente
    
    * Server:
        - Kitar Gorgona Spawn
        - Aumentar Spawn de Dungeon Tactic y Toro Quest
        - Disminuir Spawn de Dragones
        - Kitar Spawn de Dragones Muertos
        - Aumentar Spawn de plantas Carnivoras
        - Ajustar Generacion de Minerales
        - Kitar Plata del Ice and Fire, Cobre Industrial, Tin industrial, Plomo Industrial
    - 
    
    * Extra:
        - Crear Trailer
        - Crear Tutoriales (Instalar Minecraft y Trabajar con el AntiTrampas)
        - Crear Instalador Profeccional
        
        
# Dependencias:
    - Django
    - pillow
    - django-ckeditor
    - django-jet