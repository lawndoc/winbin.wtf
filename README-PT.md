![winbin.wtf](./resources/header.png)

![image](https://user-images.githubusercontent.com/3946126/193678828-94d861a5-784c-4fc3-84ad-558cbf6ee3e4.png)
# (tradução PT-BR)

Repositório que contém o código-fonte do site [WinBin.wtf](https://winbin.wtf). Este é um site de documentação binária do Windows. 
O [site](https://winbin.wtf) tem o objetivo de compensar a falta de documentação da Microsoft sobre os programas binários do Windows.

A especificação estrutural dos diretórios contidos nesse repositórios, segue a instalação padrão do Windows no disco **C:**, dito isto, 
você só precisará inserir o caminho do binário local após a URL [winBin.wtf/](https://winbin.wtf), exemplo:

**Binário no seu Windows:**
<pre>
  C:\Windows\System32
</pre>

**Caminho no site WinBin.wtf**
<pre>
  https://winbin.wtf/Windows/System32/calc.exe/
</pre>


### Escopo

No momento, o escopo deste projetos são apenas os arquivos que vêmm com a instalçaõ básica do Windows Desktop. 
Os itens instalados pelo painel de controle, Programas e Recursos "Ativar ou desativar recursos do Windows" não estão no escopo do projeto neste momento.
Quando documentarmos todso os binários padrões do Windows Desktop, então, poderemos expandir o escopo para os binários opcionais do Windows.


### Contribuição

Há um grande número de binários internos do Windows, portanto, quaisquer contribuições para esta documentação serão apreciadas.
Criei um modelo que **deve ser** usado ao documentar um novo binário. As modificações no modelo devem ser discutidas primeiro abrindo um problema neste repositório.
Adicionar novos campos ao modelo exigirá que modifiquemos retroativamente todos os documentos binários existentes, então esteja preparado para fazer um bom argumento para adicionar um campo.
