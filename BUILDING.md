In order to get poetry to accept sources in /opt/ I use this trick locally outside of docker

```
sudo git clone https://github.com/meta-introspector/agent-protocol-sdk-python /opt/agent-protocol
  poetry run pip  install -e /opt/agent-protocol/
  poetry lock
```
