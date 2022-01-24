
radians = math.radians(float(degrees))

result = {
    'sin': round(math.sin(radians), PRECISION),
    'cos': round(math.cos(radians), PRECISION),
    'tg': round(math.tan(radians), PRECISION),
    'ctg': round(1/math.tan(radians), PRECISION),
    'PI': round(math.pi, PRECISION),
}
