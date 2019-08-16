FROM nlxio/outway:latest

ENV NAME my-nlx-inway

COPY C:\nlx-setup\root.crt /certs/
COPY C:\nlx-setup\org.crt /certs/
COPY C:\nlx-setup\org.key /certs/
COPY C:\nlx-setup\service-config.toml /.

ENV DIRECTORY_INSPECTION_ADDRESS=directory-inspection-api.demo.nlx.io:443 
ENV TLS_NLX_ROOT_CERT=/certs/root.crt 
ENV TLS_ORG_CERT=/certs/org.crt 
ENV TLS_ORG_KEY=/certs/org.key 
ENV SERVICE_CONFIG=/service-config.toml 
ENV DISABLE_LOGDB=1 

EXPOSE 443
