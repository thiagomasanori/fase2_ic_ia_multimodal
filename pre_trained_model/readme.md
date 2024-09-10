Os arquivos contém o script que estava sendo utilizado, porém há ainda algum erro na chamada da função para várias imagens. A primeira tentativa foi de aplicar o modelo nos arquivos baixados, e a ideia seria posteriormente aplicar o modelo em dados puxados do PACs Orthanc. 

Até o momento foi possível converter as imagens em .dcm para um numpyarray e depois para um .png com a ajuda da função read_xray_dcm fornecida.

Com a função Image.fromarray(nparray_image) foi possível obter uma imagem como a seguinte:

<img width="702" alt="image" src="https://github.com/user-attachments/assets/b0a96cec-0eae-45ca-a610-cff412841441">
