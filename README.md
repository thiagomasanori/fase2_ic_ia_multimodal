# fase2_ic_ia_multimodal
Este repositório contém os arquivos utilizados na 2a etapa do Processo Seletivo para a Iniciação Científica em IA multimodal na Triagem de Imagens de Raios.

A primeira tarefa consistiu em criar e configurar um PACs (Picture Archiving and Communication System) usando o Orthanc no Docker.
  O dockerfile utilizado para a tarefa foi proveniente do repositório: [github.com/jodogne/OrthancDocker](https://github.com/jodogne/OrthancDocker) .
  A imagem utilizada foi "jodogne/orthanc-python" pois com o interpretador do Python 3.7 já estava embarcado no pacote.
  
  O chatGPT foi muito útil para entender o que era um dockerfile, uma imagem e um container do Docker e também o que era um PACs e estes conceitos mais básicos da tarefa. Principalmente a organização das etapas necessárias.

A segunda tarefa consistiu em fazer o upload de arquivos DICOM usando a API Rest do Orthanc com um script em Python.

A terceira tarefa era de aplicar o modelo de classificação nos arquivos DICOM da tarefa anterior, porém não foi concluídos. A ideia era usar a biblioteca [github.com/mlmed/torchxrayvision](https://github.com/mlmed/torchxrayvision/tree/master) , com modelos pré-treinados presentes no repositório.
