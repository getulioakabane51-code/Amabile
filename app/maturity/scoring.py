LEVELS = {
    1: "Experimental",
    2: "Operacional",
    3: "Integrado",
    4: "Data-driven",
    5: "Transformacional",
}

DIMENSIONS = ("strategy", "people", "processes", "data", "governance")


def maturity_level(scores: dict[str, float]) -> tuple[float, int, str]:
    """Calcula média simples de 1 a 5 para um diagnóstico estruturado."""
    missing = [d for d in DIMENSIONS if d not in scores]
    if missing:
        raise ValueError(f"Dimensões ausentes: {', '.join(missing)}")

    values = [float(scores[d]) for d in DIMENSIONS]
    if any(v < 1 or v > 5 for v in values):
        raise ValueError("Cada nota deve estar entre 1 e 5.")

    average = sum(values) / len(values)
    level = min(5, max(1, round(average)))
    return round(average, 2), level, LEVELS[level]
