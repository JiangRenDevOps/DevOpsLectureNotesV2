#!/bin/bash
set -e

# Install go
snap install go --classic

export PATH=/snap/bin:$PATH

echo 'eval $(go env)' >> /home/vagrant/.bashrc
echo 'export PATH=/snap/bin:$PATH' >> /home/vagrant/.bashrc
echo 'export PATH=$GOPATH/bin:$PATH' >> /home/vagrant/.bashrc

# Install kind
GO111MODULE="on" go get sigs.k8s.io/kind@v0.6.1

# Install kubectl
snap install kubectl --classic
