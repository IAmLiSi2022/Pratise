import os;
####################################################################################################################
os.system("mv ./src-code-server.py ./src.tar.gz";)
######################  TAR  #######################################################################################
os.system("tar --gzip --extract --file=./src.tar.gz");
######################  WGET  ######################################################################################
os.system("zypper --non-interactive install wget")
url=["https://github.com/coder/code-server/releases/download/v4.9.1/code-server-4.9.1-amd64.rpm","https://github.com/microsoft/vscode-cpptools/releases/download/v1.10.8/cpptools-linux.vsix","https://github.com/microsoft/vscode-python/releases/download/2021.9.1218897484/ms-python-release.vsix","https://github.com/microsoft/vscode-docker/releases/download/v1.23.3/vscode-docker-1.23.3.vsix"]
file=["./code-server-4.9.1-amd64.rpm","./cpptools-linux.vsix","./ms-python-release.vsix","./vscode-docker-1.23.3.vsix"]
empty=""
agent_0="'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61' "
suffix_wget="wget --tries=500 --user-agent="
b=0;
while b<=3:
  a=[suffix_wget,agent_0,url[b]];
  wget=empty.join(a);
  while os.path.exists(file[b])==False:
    print(wget)
    os.system(wget)   
  b=b+1;
######################  ZYPPER & CODE_SERVER  ######################################################################
os.system("zypper --non-interactive install gcc gdb sudo");
os.system("zypper --non-interactive install --allow-unsigned-rpm ./code-server-4.9.1-amd64.rpm");
os.system("code-server --install-extension ./cpptools-linux.vsix");
os.system("code-server  --force --install-extension ./ms-python-release.vsix");
os.system("code-server --install-extension ./vscode-docker-1.23.3.vsix");
######################  CP & RM  ###################################################################################
suffix_cp="cp "
suffix_rm="rm "
path_src=["--recursive ./fonts ","./workbench.web.main.css ","./settings.json ","./config.yaml "]
path_dest=["/usr/lib/code-server/lib/vscode/fonts;","/usr/lib/code-server/lib/vscode/out/vs/workbench/workbench.web.main.css","~/.local/share/code-server/User/settings.json","~/.config/code-server/config.yaml"]
c=0
while c<=3:
  d=[suffix_cp,path_src[c],path_dest[c]]
  copy=empty.join(d)
  print(copy)
  os.system(copy)
  f=[suffix_rm,path_src[c]]
  rm=empty.join(f)
  print(rm)
  os.system(rm)
  c=c+1
g=0
while g<=3:
  h=[suffix_rm,file[g]]
  rm=empty.join(h)
  print(rm)
  os.system(rm)
  g=g+1
print("Done ")
#######################  STARTUP JOBS  ##############################################################################
os.system("cp ./code-server.service /etc/systemd/system/code-server.service");
os.system("systemctl daemon-reload");
os.system("systemctl start code-server");
os.system("systemctl enable code-server");
