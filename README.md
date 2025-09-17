# Desafio Prompt Engineering

📄 **Descrição breve**: Exercício prático de Prompt Engineering aplicado a 4 questões de IA.  

---

## 📚 Introdução

O desafio de Prompt Engineering envolve o uso estratégico de técnicas específicas para formular comandos (prompts) que permitam extrair as respostas mais precisas, relevantes e detalhadas de uma ferramenta de IA generativa.  

Essa prática não apenas refina a interação com a IA, mas também explora ao máximo o potencial da tecnologia, adaptando-a a diferentes contextos e necessidades.

Neste desafio, aplicaremos conceitos e metodologias ensinados para construir prompts eficazes, utilizando como exemplo prático o ChatGPT, desenvolvido pela OpenAI.

---

## ⚡ Estrutura do Desafio

O desafio será composto por **4 perguntas distintas**, cada uma com características específicas que exigem a aplicação de técnicas de Prompt Engineering para obter a melhor resposta possível da ferramenta.  

Para cada pergunta, será necessário identificar a técnica mais adequada, considerando fatores como clareza, contexto, detalhamento e relevância do resultado esperado.

---

## 🔎 Questões

1. Utilize uma ferramenta de IA Generativa para saber como o algoritmo de Ray Tracing calcula a cor de um pixel em uma imagem renderizada.  

2. Utilize uma ferramenta de IA Generativa para obter uma resposta completa de como fazer a decomposição numérica de **142.981**.  

3. Utilize uma ferramenta de IA Generativa para obter quais personagens de **As Crônicas de Gelo e Fogo** possuem características inspiradas na filosofia de **Maquiavel**.  

4. Utilizando uma ferramenta de IA generativa, crie um endpoint com **FastAPI** que valide e processe a entrada de um objeto do tipo `Item`.  

   - Estrutura do `Item`:
     - **nome**: `string` com tamanho máximo de 25 caracteres.  
     - **valor**: `float`  
     - **data**: valor do tipo *date*, que não pode ser superior à data atual.  

   - Requisitos:
     - O endpoint deve validar os valores recebidos.  
     - Após a validação, o corpo da requisição (`Item`) deve ser retornado com um novo campo adicional: `uuid`. Este campo deve conter um identificador único gerado dinamicamente.  
