#!/bin/bash
echo "0 8 1 * * python3  /home/aaron/Documentos/Data_Enginner_Program/Proyecto Data Engineering con Python/pipe/pipe.py" | crontab
echo "data update"