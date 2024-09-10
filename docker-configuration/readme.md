A imagem utilizada para rodar o PACs OrthanC está contida neste Dockerfile. 

Uma dificuldade que tive no desenvolvimento desta tarefa foi a de configurar o acesso ao servidor. Não consegui remover a necessidade de autenticação de login e para bloquear o acesso remoto ao servidor por questões de segurança.
No fim, a autenticação ainda é necessária e o usuário e senha são definidos por padrão como dispostos a seguir:
<br>
     <br> usuário: orthanc
     <br> senha: orthanc

Ao executar o comando RUN, inicializando o Container o servidor roda no endereço:
  http://localhost:8042


<img width="1699" alt="image" src="https://github.com/user-attachments/assets/1bf08950-433c-4c8e-a924-b441e25fc7b4">
