
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Desenvolver um jogo da forca em Python para praticar manipulação de strings, laços de repetição e condicionais. Ao final, o aluno deve conseguir controlar o fluxo completo de uma partida com vitória ou derrota.

## 📝 Tarefas

### 🛠️ Implementar a lógica principal do jogo

#### Descrição
Crie um programa que selecione uma palavra aleatória e permita ao jogador adivinhar letras, exibindo o progresso da palavra ao longo das tentativas.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra aleatória a partir de uma lista predefinida
- Exibir a palavra oculta no formato com sublinhados (exemplo: `_ _ _ _ _`)
- Solicitar uma letra por rodada e atualizar o estado da palavra
- Mostrar quantas tentativas incorretas ainda restam
- Encerrar a partida quando o jogador adivinhar a palavra ou as tentativas acabarem


### 🛠️ Tratar entradas e finalizar a partida com feedback

#### Descrição
Adicione validações simples de entrada e mensagens finais para tornar a experiência do jogo mais clara para o usuário.

#### Requisitos
O programa concluído deve:

- Aceitar apenas uma letra por vez como palpite
- Informar quando a letra já tiver sido usada anteriormente
- Exibir mensagem de vitória quando a palavra for completada
- Exibir mensagem de derrota com a palavra correta quando as tentativas terminarem
- Manter o código organizado e legível, com nomes de variáveis descritivos