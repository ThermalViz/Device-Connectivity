# Device-Connectivity

Startup Execute:
    - cd ./Documents/
    - sudo nano launcher.sh
      - cd
      - cd /home/neocircuits/Documents/
      - sudo python sensors.py
    - sudo chmod 755 launcher.sh
    - sudo crontab -e
      - @reboot sh /home/neocircuits/Documents/launcher.sh