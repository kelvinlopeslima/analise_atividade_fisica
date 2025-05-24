# 📊 analise-atividade-fisica-bykelvin

Este pacote permite processar e analisar dados de atividades físicas a partir de arquivos CSV.  
É ideal para gerar resumos semanais, identificar a atividade mais frequente e os dias mais ativos com base nos dados fornecidos.

## Formato tabela

| Coluna        | Tipo          | Descrição                                     |
|---------------|---------------|-----------------------------------------------|
| `data`        | string / date | Data da atividade no formato `YYYY-MM-DD`     |
| `atividade`   | string        | Tipo da atividade física realizada            |
| `duracao_min` | int           | Duração da atividade em minutos               |
| `calorias`    | int           | Quantidade de calorias gastas na atividade 


## Instalação

Você pode instalar o pacote diretamente via `pip`:

```bash
pip install analise-atividade-fisica-bykelvin
