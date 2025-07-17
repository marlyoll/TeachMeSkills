def unicorns_to_rainbows(unicorns: list[dict]) -> list[str]:
    return [f"🌈 Rainbow unicorn of color {unicorn['color']}" for unicorn in unicorns]

unicorns = [
    {'name': 'Sparkle', 'color': 'pink'},
    {'name': 'Twilight', 'color': 'purple'},
    {'name': 'Glitter', 'color': 'blue'}
]
rainbows = unicorns_to_rainbows(unicorns)
print(rainbows)
