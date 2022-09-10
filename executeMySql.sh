#!/bin/bash
echo 'Creando y cargando la base de datos...'
mysql -u $user -p $password -e "source $path_sql"
echo 'Carga finalizada'