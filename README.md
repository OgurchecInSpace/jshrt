Jshrt is url-shortener service. You can modify this code (buy domain and connect it to this project) and run this project in docker container.
This site doesn't work in docker container because it uses env IP for generate short URL.
  
Dockerfile and requirements in main directory. 

Api and website run on :8080 (mapping this port to 80 on hosting)
It uses nginx now, but you can don't use nginx if you will use it

