from dataclasses import dataclass, field


@dataclass(frozen=True)
class Scenario:
    name: str
    curve_bp: dict[str, float] = field(default_factory=dict)
    ig_spread_bp: float = 0.0
    hy_spread_bp: float = 0.0
    equity_return: float = 0.0
