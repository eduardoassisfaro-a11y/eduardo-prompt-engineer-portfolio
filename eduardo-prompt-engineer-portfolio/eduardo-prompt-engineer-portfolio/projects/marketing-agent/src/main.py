import json, argparse, pathlib, yaml

def gerar_funnel(briefing):
    # Placeholder simples para demonstrar estrutura
    persona = briefing.get("persona", "público")
    produto = briefing.get("produto", "produto")
    return {
        "topo_funil": [f"Gancho 1 para {persona} sobre {produto}"],
        "meio_funil": [f"Conteúdo educativo sobre {produto}"],
        "fundo_funil": [f"Oferta irresistível do {produto} com CTA"]
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--briefing", required=True)
    args = parser.parse_args()

    data = yaml.safe_load(pathlib.Path(args.briefing).read_text(encoding="utf-8"))
    plano = gerar_funnel(data)
    out = pathlib.Path("out"); out.mkdir(exist_ok=True)
    (out / "funnel.json").write_text(json.dumps(plano, ensure_ascii=False, indent=2), encoding="utf-8")
    print("OK :: out/funnel.json gerado.")

if __name__ == "__main__":
    main()
