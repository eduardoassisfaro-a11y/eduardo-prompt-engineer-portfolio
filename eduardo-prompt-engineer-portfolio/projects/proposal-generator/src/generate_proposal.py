import argparse, json, pathlib

MD_TEMPLATE = """
# Proposta Comercial — {cliente}

**Projeto:** {projeto}

## Escopo
{escopo}

## Prazos
- Entrega: {entrega}

## Investimento
- {moeda} {valor:.2f}

## Condições
{condicoes}

---
*Gerado automaticamente.*
"""

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--briefing", required=True)
    p.add_argument("--schema", required=True)
    args = p.parse_args()

    briefing = json.loads(pathlib.Path(args.briefing).read_text(encoding="utf-8"))
    out = pathlib.Path("out"); out.mkdir(exist_ok=True)

    escopo_md = "".join([f"- {item}\n" for item in briefing.get("escopo", [])])
    cond_md = "".join([f"- {c}\n" for c in briefing.get("condicoes", [])])

    md = MD_TEMPLATE.format(
        cliente=briefing.get("cliente",""),
        projeto=briefing.get("projeto",""),
        escopo=escopo_md,
        entrega=briefing.get("prazos",{}).get("entrega",""),
        moeda=briefing.get("investimento",{}).get("moeda","BRL"),
        valor=float(briefing.get("investimento",{}).get("valor",0)),
        condicoes=cond_md
    )
    (out/"proposta.md").write_text(md, encoding="utf-8")
    print("OK :: out/proposta.md gerado.")

if __name__ == "__main__":
    main()
