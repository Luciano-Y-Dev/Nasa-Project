# Explorando el Cosmos: Proyecto Starry Image

Este proyecto de desarrollo web busca unir la curiosidad astronómica con la historia personal. **Starry Image** es una aplicación que permite a los usuarios descubrir qué maravilla del universo capturó la NASA el día exacto de su nacimiento. El objetivo es transformar datos científicos en una experiencia visualmente impactante y emocional, facilitando el acceso a la astronomía mediante la traducción automática y una interfaz intuitiva.

---

## Experiencia de Usuario y Funcionamiento

El flujo de la aplicación ha sido diseñado para ser directo y cautivador:

- **Entrada de datos:** El usuario introduce su fecha de nacimiento en el sistema.
- **Consulta en Tiempo Real:** La app consulta la NASA API para obtener la imagen astronómica correspondiente a ese día específico.
- **Localización de Contenido:** Para eliminar las barreras del idioma, se muestra la imagen, el título y la explicación técnica traducidos al español.
- **Despliegue Visual:** Se presenta la información de forma clara para conectar a las personas con el cosmos a través de su propia historia.

## Arquitectura y Stack Técnico

Para este desarrollo, seleccioné herramientas que permiten un despliegue rápido sin sacrificar la robustez del frontend:

- **Reflex:** Framework web de Python utilizado para construir la estructura de la aplicación.
- **NASA API:** Fuente de datos astronómicos verificados que alimenta el contenido diario.
- **Google Translator:** Integración para realizar la traducción automática del contenido explicativo.
- **Tailwind CSS:** Utilizado para el manejo de estilos y diseño visual.

## Diseño y Características Clave

Más allá de la funcionalidad técnica, el proyecto se centra en la estética y la resiliencia:

- **Interfaz Modernista:** Diseño con efectos _glassmorphism_ que proporcionan una apariencia elegante y futurista.
- **Diseño Responsivo:** Adaptabilidad total para asegurar una visualización óptima en distintos dispositivos.
- **Gestión de Errores:** Implementación de un manejo de errores robusto para garantizar la estabilidad de la aplicación.

## Reflexiones del Proyecto

**Starry Image** es un proyecto personal centrado en crear una experiencia única para el usuario. Representó un ejercicio práctico de integración de APIs externas y traducción en tiempo real, con el fin de acercar la ciencia del espacio a un público más amplio mediante un diseño atractivo y funcional.
