# Proyecto final Programacion Orientada a Objetos
## Loteria Smart-Contract 💻 💲
Con el auge de las tecnologias de la 4ta revolucion industrial y las necesidades de los usuarios, han surgido diferentes corrientes de conectividad que aspiran a ser prometedoras y que le apuestan a la descentralizacion y democratizacion de lo que conocemos como la Web. Desde aplicaciones descentralizadas, criptomonedas, validacion de contratos y hasta criptosistemas es lo que contiene la tan emergente Web3, un paradigma donde el usuario es el veedor de su propia informacion y no se ve vulnerado. Tal como pueden ver en este video, los beneficios de esta corriente son incontables pero especificamente en este Read-me encontraras un uso del que decidimos disponer
> **❓ Motivacion del proyecto:** El fin primero de esta experiencia era lograr llevar a cabo una pequeña loteria local y remota haciendo uso de tecnologias descentralizadas y de todos los beneficios que nos brinda la implementacion de la programacion orientada a objetos. Aunque quizas sus aplicaciones sean reducidas, el factor aleatoridad en esta tecnologia apunta a la factibilidad y escabilidad de diversos tipos de negocios tales como casa de apuestas, bingo y fundraising, lo cual nos permite disfrutar de muchos mas beneficios en la Web3. 

A continuacion haremos mencion de varias de las tecnologias y recursos con la que se desarrollo el proyecto 
 * Brownie
 * Python3.
 * Solidity
 * ChainLink
 * Web3 Oracles
 * Infura
 * Metamask
 * Etherscan

Si gustas conocer un poco mas de las tecnologias puedes hacer uso de algunas referencias que dejaremos al final del documento

## **_Paso a paso acerca del uso_**
**Descarga Python3 🐍**

El primer paso para crear tu propia loteria es que cuentes con la version mas actual de Python. Para ello puedes acudir al sitio oficial de python.org y descargarlo para tu sistema, ya sea Windows, Linux o Mac.

* ✅ Como alternativa tambien puedes hacer uso de un entorno virtual mediante una VM, para ello accede a tu servidor de nube de preferencia, posteriormente usa el servicio de terminal y descargar Python. Con esta alternativa, los paquetes auxiliares y cualesquiera otros recursos que implementes se mantendran actualizados y listos para funcionar

**Descarga Brownie 🟫** 

Luego de que tengas Python instalado en tu VM o computador. Haras uso de los siguientes comandos para poder descargar Brownie

*Usando pipx*
```
python3 -m pip install --user pipx
python3 -m pipx ensurepath 
#Despues de ejecutar ensurepath, por favor reinicia tu terminal. Luego
pipx install eth-brownie
```
*Usando pip*

Para esta alternativa, sugerimos fuertemente que lo hagas en un entorno virtual. Esto con el fin de evitar sobreescribir datos y evitar problemas de directorio o archivos
```
pip install eth-brownie
#Ahora clonaras el siguiente repositorio y usaras un setup
git clone https://github.com/eth-brownie/brownie.git
cd brownie
python3 setup.py install
```

**Crea tu cuenta en Metamask, aplicacion y haz inmersion en la Web3 🐺**

Desde tu navegador de preferencia consulta metamask.io, descarga la aplicacion y sigue el instructivo sugerido para crear tu primera cartera de criptomonedas!

Luego por medio del menu de opciones, solicita acceder a las redes de prueba y selecciona **_Goerli Testnet_**. Luego de haber hecho este paso ya estaras listo para poder acceder a los beneficios de desarrollo que te ofrece la Web3. No te preocupes si ves tus fondos en _ETH 0_, haciendo uso de un Faucet podras recargar tu cuenta con _ETH 0.2_  (230 dolares aproximadamente)

> **🏦 Y como accedo a este "Faucet"?**.

Actualmente, para retribuir fondos a tu cartera por medio de _Goerli Faucet_ se te pedira tener una cuenta de _Alchemy_ (Sitio para almacenar tus aplicaciones de Web3). La misma pagina te dara el paso a paso necesario para crear tu cuenta y luego seras redirigido al menu de inicio del Faucet, en este momento, abre la extension de Metamask y copia la llave publica asociada a tu cartera (Esta aparece en la parte media de la pantalla, veras un logo de copiar al lado de este texto). Finalmente, obten tus _ETH_ y utilizalos de manera responsable

> **✋ Ahora como creo mi proyecto en Alchemy"?**.

Cuando ya dispongas de tu cuenta, el proceso para crear un proyecto es sencillo y gratuito!. En la barra del menu veras la opcion _New Project_. ,pincha encima de ella y luego solo queda esperar a que sea desplegada tu aplicacion. Para conocer mas informacion de tu proyecto tales como llaves o links, veras al lado del nombre de tu proyecto la opcion _Show info_, pinchala y ten esa informacion abierta porque la vamos a necesitar luego 


> **⏲ Como obtengo informacion actualizada para mi proyecto?**

Para esto haremos uso de la API de Infura, la cual podras encontrar en su pagina infura.io. Acceder es bastante sencillo y solo necesitaras de una cuenta, vincula tu correo o cualquier otro recursos para y de esta manera poder tener un Dashboard de tus proyectos.

Tal como hicimos en Alchemy, crearas un nuevo proyecto y vas a revelar la informacion del mismo. Conserva esta informacion porque sera relevante y asegurate de que la estes desplegando en la Testnet de Goerli

**Despliegue de loteria**

Ya estamos cada vez mas cerca para desplegar nuestra loteria en la Blockchain y poder compartirla con nuestros amigos. 

El paso a seguir es volver a tu terminal y ejecutar los siguientes comandos

*Clona nuestro repositorio, ejecutar los contratos y almacenamiento de cuentas*
Por medio del comando podras extraer todos los archivos de la loteria (Scripts, yaml, contratos, modulos de testing entre otros)

```
git clone _conexion https de este repositorio_
```
Con esto hecho, cambia tu posicion en el directorio (cd) a la nueva carpeta. Ahora cerciorate de crear cada una de las cuentas vinculadas a esta loteria por medio del siguiente comando

**✅ Nota**
> Si la creas en un entorno que no sea de prueba este paso no es necesario pero recuerda que se te tributara dinero real

```
#Para compilar contratos
 brownie compile
#Para crear cada cuenta 
 brownie accounts new account-name
#En este paso se te pedira la llave privada de la cuenta, asociala y encriptala
#Repite este proceso por cada cuenta expuesta en la loteria
#Para ver la lista de tus cuentas usa lo siguiente
 brownie accounts list
```

*Conexion a red de prueba (Infura) y aplicativo (Alchemy)*

En este paso haremos uso de 2 comandos algo extensos, pero con esto aseguramos que nuestro aplicativo tenga informacion actualizada y poder acceder a los contratos de aleatoridad brindados por ChainLink

```
#Eliminamos la red de desarrollo predeterminada 
brownie networks delete mainnet-fork
#Creamos nuestra red de desarrollo 
brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork= llave_app_alchemy accounts=10 mnemonic=brownie
```

Ya llegamos a nuestro final, lo ultimo que necesitaras es el siguiente comando y ver con tus amigos quien es el ganador. 

```
brownie run scripts/deploy_lottery.py --network goerli 
```

Por terminal veras el hash asociado al despliegue del contrato, buscalo en Etherscan y listo. Tu primera loteria Blockchain!

Gracias por tu atencion y agradecemos tu granito de arena en apoyar nuestro aprendizaje 👏


