nohup gunicorn -c gunicorn_config.py app:app --certfile=/etc/pki/tls/certs/nftprofilebuilder_com.crt --keyfile=/etc/pki/tls/private/nftprofilebuilder_tld.key 2> nohub.out &
